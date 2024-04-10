
#%%
from pathlib import Path

import cardiac_geometries
import pulse
import dolfin
import numpy as np
import matplotlib.pyplot as plt


import pressure_model
import activation_model

#%%

def create_infarct(V, center_1=(0, 4, 4), center_2=(-6, 0, 0)) -> dolfin.Function:
    expr = dolfin.Expression(
        "(exp(-(pow(x[0] - x1, 2) + pow(x[1] - y1, 2) + pow(x[2] - z1, 2)) / pow(sigma1, 2)) + exp(-(pow(x[0] - x1, 2) + pow(x[1] + y1, 2) + pow(x[2] - z1, 2)) / pow(sigma1, 2)) +exp(-(pow(x[0] - x1, 2) + pow(x[1] - y1, 2) + pow(x[2] + z1, 2)) / pow(sigma1, 2)) + exp(-(pow(x[0] - x1, 2) + pow(x[1] + y1, 2) + pow(x[2] + z1, 2)) / pow(sigma1, 2)) + exp(-(pow(x[0] - x2, 2) + pow(x[1] - y2, 2) + pow(x[2] - z2, 2)) / pow(sigma2, 2)))/100",
        degree=1,
        x1=center_1[0],
        y1=center_1[1],
        z1=center_1[2],
        sigma1=4.0,
        x2=center_2[0],
        y2=center_2[1],
        z2=center_2[2],
        sigma2=7.0,
    )
    f = dolfin.interpolate(expr, V)
    return f


def get_ellipsoid_geometry(folder=Path("lv")):
    if not folder.is_dir():
        # Create geometry
        cardiac_geometries.create_lv_ellipsoid(
            folder,
            create_fibers=True,
        )

    # Trying to force cardiac_geometries to read cfun, containing aha 17 segments
    schema = cardiac_geometries.geometry.Geometry.default_schema()
    cfun_schema = schema['cfun']._asdict()
    cfun_schema['fname'] = 'cfun.xdmf:f'
    schema['cfun'] = cardiac_geometries.geometry.H5Path(**cfun_schema)

    geo = cardiac_geometries.geometry.Geometry.from_folder(folder, schema=schema)
    marker_functions = pulse.MarkerFunctions(cfun=geo.cfun, ffun=geo.ffun)
    microstructure = pulse.Microstructure(f0=geo.f0, s0=geo.s0, n0=geo.n0)
    return pulse.HeartGeometry(
        mesh=geo.mesh,
        markers=geo.markers,
        marker_functions=marker_functions,
        microstructure=microstructure,
    )


def plot_pressure_and_activationInOne(
    pressure,
    normal_activation,
    delayed_activation,
    t_eval,
    outdir,
):
    fig, ax = plt.subplots(2, 1, sharex=True)
    ax[0].plot(t_eval, pressure, label="Pressure")
    ax[0].set_ylabel("Pressure [kPa]")

    ax[1].plot(t_eval, normal_activation, label="Normal Activation")
    ax[1].plot(t_eval, delayed_activation, label="Delayed Activation")
    ax[1].set_ylabel("Activation [-]")
    ax[1].legend()
    ax[1].set_xlabel("Time [s]")
    fig.savefig(outdir / "pressure_and_activation.png")

    np.save(outdir / "t_eval.npy", t_eval)
    np.save(outdir / "pressure.npy", pressure)
    np.save(outdir / "normal_activation.npy", normal_activation)
    np.save(outdir / "delayed_activation.npy", delayed_activation)
#%
delay = 0.0
threshold = 0.5
geometry = get_ellipsoid_geometry()
t_span = (0.0, 1.0)
t_eval = np.linspace(*t_span, 20)

delay = 0.0
outdir = Path("results") / f"delay_{delay}"
outdir.mkdir(exist_ok=True, parents=True)

pressure = (
    pressure_model.pressure_function(
        t_span=t_span,
        t_eval=t_eval,
        parameters=pressure_model.default_parameters(),
    )
    / 1000.0
)
normal_activation_params = activation_model.default_parameters()
delayed_activation_params = normal_activation_params.copy()
delayed_activation_params["t_sys"] += delay
delayed_activation_params["t_dias"] += delay
normal_activation = (
    activation_model.activation_function(
        t_span=t_span,
        t_eval=t_eval,
        parameters=normal_activation_params,
    )
    / 1000.0
)
delayed_activation = (
    activation_model.activation_function(
        t_span=t_span,
        t_eval=t_eval,
        parameters=delayed_activation_params,
    )
    / 1000.0
)
plot_pressure_and_activationInOne(
    pressure,
    normal_activation=normal_activation,
    delayed_activation=delayed_activation,
    t_eval=t_eval,
    outdir=outdir,
)
V = dolfin.FunctionSpace(geometry.mesh, "CG", 1)

infarct = create_infarct(V=V)
with dolfin.XDMFFile((outdir / "infarct.xdmf").as_posix()) as xdmf:
    xdmf.write_checkpoint(
        infarct,
        "infarct",
        0.0,
        dolfin.XDMFFile.Encoding.HDF5,
        False,
    )
#%%
# Find the delayed activation dofs
delayed_dofs = infarct.vector().get_local() > threshold
target_activation = dolfin.Function(V)
activation = dolfin.Function(V)

# Create the model
matparams = pulse.HolzapfelOgden.default_parameters()
material = pulse.HolzapfelOgden(
    activation=activation,
    active_model="active_stress",
    parameters=matparams,
    f0=geometry.f0,
    s0=geometry.s0,
    n0=geometry.n0,
)

# LV Pressure
lvp = dolfin.Constant(0.0)
lv_marker = geometry.markers["ENDO"][0]
lv_pressure = pulse.NeumannBC(traction=lvp, marker=lv_marker, name="lv")
neumann_bc = [lv_pressure]

# Add spring term at the epicardium of stiffness 1.0 kPa/cm^2 to represent pericardium
base_spring = 1.0
robin_bc = [
    pulse.RobinBC(
        value=dolfin.Constant(base_spring),
        marker=geometry.markers["EPI"][0],
    ),
]

# Fix the basal plane in the longitudinal direction
# 0 in V.sub(0) refers to x-direction, which is the longitudinal direction
def fix_basal_plane(W):
    V = W if W.sub(0).num_sub_spaces() == 0 else W.sub(0)
    bc = dolfin.DirichletBC(
        V.sub(0),
        dolfin.Constant(0.0),
        geometry.ffun,
        geometry.markers["BASE"][0],
    )
    return bc

dirichlet_bc = (fix_basal_plane,)

# Collect boundary conditions
bcs = pulse.BoundaryConditions(
    dirichlet=dirichlet_bc,
    neumann=neumann_bc,
    robin=robin_bc,
)

outname = Path(outdir) / "results.xdmf"
if outname.is_file():
    outname.unlink()
    outname.with_suffix(".h5").unlink()
#%%

# Create the problem
problem = pulse.MechanicsProblem(geometry, material, bcs)
vols = []
breakpoint()
for i, (pi, a_normal, a_delayed) in enumerate(
    zip(pressure, normal_activation, delayed_activation),
):
    print(f"\nSolving for pressure {pi} kPa")
    print(f"Activation normal {a_normal}")
    print(f"Activation delayed {a_delayed}")

    # Update the activation
    target_activation.vector()[:] = a_normal
    target_activation.vector()[delayed_dofs] = a_delayed

    # Solve the problem
    pulse.iterate.iterate(problem, lvp, pi)
    pulse.iterate.iterate(problem, activation, target_activation)

    # Get the solution
    u, p = problem.state.split(deepcopy=True)
    volume = geometry.cavity_volume(u=u)
    vols.append(volume)
    np.save(outdir / "volumes.npy", vols)

    with dolfin.XDMFFile(outname.as_posix()) as xdmf:
        xdmf.write_checkpoint(u, "u", float(i), dolfin.XDMFFile.Encoding.HDF5, True)

#%%

outdir = Path("results") / f"delay_{delay}"
volumes = np.load(outdir / "volumes.npy")
pressure = np.load(outdir / "pressure.npy")
fig, ax = plt.subplots()
ax.plot(volumes, pressure)
ax.set_xlabel("Volume [ml]")
ax.set_ylabel("Pressure [kPa]")
fig.savefig(outdir / "pv.png")


