# %%
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

from activation_model import compute_delayed_activations
from heart_model import HeartModelPulse
import dolfin as df
import ufl_legacy as ufl
import cardiac_geometries


# %%
def load_mesh(fname: Path):
    # Read the mesh
    with df.XDMFFile(fname.as_posix()) as xdmf:
        mesh = df.Mesh()
        xdmf.read(mesh)
    return mesh


def load_fiber_dir(fname: Path, mesh: df.mesh):
    W = df.VectorFunctionSpace(mesh, "CG", 1)
    fib0 = df.Function(W)
    with df.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(fib0, "f0 (partial)")
    return fib0


def load_u(fname: Path, t: float, mesh: df.mesh):
    V = df.VectorFunctionSpace(mesh, "CG", 2)
    u = df.Function(V)
    with df.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(u, "u", t)
    return u


def compute_F(u):
    dim = ufl.domain.find_geometric_dimension(u)
    I = df.Identity(dim)
    F = I + df.grad(u)
    return F


def compute_green_lagrange_strain(F_tot: df.Function, F0: df.Function):
    dim = ufl.domain.find_geometric_dimension(F_tot)
    F = F_tot * df.inv(
        F0
    )  # Here we exclude the initial inflation part for calculation of strain values
    J = df.det(F)
    F_isochoric = pow(J, -1.0 / float(dim)) * F
    C = F_isochoric.T * F_isochoric
    I = df.Identity(dim)
    E = 0.5 * (C - I)
    return E


def compute_fiber_strain(E: df.Function, fib0: df.Function, mesh: df.mesh):
    V = df.FunctionSpace(mesh, "DG", 0)
    Eff = df.project(df.inner(E * fib0, fib0), V)
    return Eff


geo_folder = Path("dev_test/lv")
geo = cardiac_geometries.geometry.Geometry.from_folder(Path("dev_test/lv"))


fname = Path("dev_test/results.xdmf")
u0 = load_u(fname, 0, geo.mesh).copy(deepcopy=True)
F0 = compute_F(u0)

t = 250
Eff_t_values = []

for t in range(278):
    u_t = load_u(fname, t, geo.mesh)
    F_t = compute_F(u_t)
    E_t = compute_green_lagrange_strain(F_t, F0)
    Eff_t = compute_fiber_strain(E_t, geo.f0, geo.mesh)
    Eff_t_values.append(Eff_t.vector()[:])

Eff_t_values = np.array(Eff_t_values)


plt.plot(Eff_t_values[80:, :50])
# %%
deformed_mesh = df.Mesh(geo.mesh)
V = df.VectorFunctionSpace(deformed_mesh, "Lagrange", 2)
U = df.Function(V)
U.vector()[:] = u_t.vector()[:]
df.ALE.move(deformed_mesh, U)


# %%
def valve_time(fname):
    return


list = ["normal", "decay_05", "delay_05", "diastole_05"]
for name in list:
    outdir = Path("02_results") / name
    fname = outdir / "strains.csv"
    outfname = outdir / "strain.png"
    strains = np.loadtxt(fname.as_posix(), delimiter=",")
    plt.plot(strains, "k-", linewidth=0.1)
    plt.xlabel("Time [ms]")
    plt.ylabel("Strains [-]")
    plt.ylim((-0.3, 0.05))
    plt.savefig(outfname)
    plt.close()
    fname = outdir / "myocardial_work.csv"
    outfname = outdir / "myocardial_work.png"
    strains = np.loadtxt(fname.as_posix(), delimiter=",")
    plt.plot(strains, "k-", linewidth=0.1)
    plt.xlabel("Time [ms]")
    plt.ylabel("Myocardial Work [-]")
    plt.savefig(outfname)

# %% plotting the delayed activation processing
delay = 0.0
geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 5,
    "r_long_epi": 5.75,
    "mesh_size": 1,
}
fe_model = HeartModelPulse(geo_params=geo_params)
delayed_activations = compute_delayed_activations(
    fe_model.geometry.cfun, num_time_step=500, std=delay
)
data = delayed_activations[0][0, :]
if delay == 0:
    offsets = np.zeros(len(data))
else:
    offsets = stats.norm.ppf(np.linspace(0.01, 0.99, len(data)), loc=0, scale=delay)
plt.hist(offsets * 1000, align="left")
plt.ylabel("No. of elements")
plt.xlabel("delays [ms]")
plt.xlim([-150, 150])

plt.plot(delayed_activations[0][:, :], "k-", linewidth=0.05)
plt.ylabel("Activation (kPa)")
plt.xlabel("Time (ms)")
