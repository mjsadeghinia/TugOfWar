from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

import dolfin
import ufl_legacy as ufl
import cardiac_geometries
from geometry import get_cfun_for_altered_compartment, get_cfun_for_adjacent_compartment



# %%
def load_mesh(fname: Path):
    # Read the mesh
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        mesh = dolfin.Mesh()
        xdmf.read(mesh)
    return mesh

def load_geo_with_cfun(geo_folder):
    schema = cardiac_geometries.geometry.Geometry.default_schema()
    cfun_schema = schema["cfun"]._asdict()
    cfun_schema["fname"] = "cfun.xdmf:f"
    schema["cfun"] = cardiac_geometries.geometry.H5Path(**cfun_schema)
    geo = cardiac_geometries.geometry.Geometry.from_folder(geo_folder, schema=schema)
    return geo

def load_fiber_dir(fname: Path, mesh: dolfin.mesh):
    W = dolfin.VectorFunctionSpace(mesh, "CG", 1)
    fib0 = dolfin.Function(W)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(fib0, "f0 (partial)")
    return fib0


def load_u(fname: Path, t: float, mesh: dolfin.mesh):
    V = dolfin.VectorFunctionSpace(mesh, "CG", 2)
    u = dolfin.Function(V)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(u, "u", t)
    return u


def compute_F(u):
    dim = ufl.domain.find_geometric_dimension(u)
    I = dolfin.Identity(dim)
    F = I + dolfin.grad(u)
    return F


def compute_green_lagrange_strain(F_tot: dolfin.Function, F0: dolfin.Function):
    dim = ufl.domain.find_geometric_dimension(F_tot)
    F = F_tot * dolfin.inv(
        F0
    )  # Here we exclude the initial inflation part for calculation of strain values
    J = dolfin.det(F)
    F_isochoric = pow(J, -1.0 / float(dim)) * F
    C = F_isochoric.T * F_isochoric
    I = dolfin.Identity(dim)
    E = 0.5 * (C - I)
    return E


def compute_fiber_strain(E: dolfin.Function, fib0: dolfin.Function, mesh: dolfin.mesh):
    V = dolfin.FunctionSpace(mesh, "DG", 0)
    Eff = dolfin.project(dolfin.inner(E * fib0, fib0), V)
    return Eff


def compute_compartment_fiber_strain(geo, u_t, compartment_indices, F0=dolfin.Identity(3)):
    F_t = compute_F(u_t)
    E_t = compute_green_lagrange_strain(F_t, F0)
    Eff_t = compute_fiber_strain(E_t, geo.f0, geo.mesh)
    Eff_t_ave = Eff_t.vector()[:]
    return Eff_t_ave
#%%
def main(outdir, num_time_step, segmentation_schema):
    geo_folder = Path(outdir) / 'lv'
    geo =  load_geo_with_cfun(geo_folder)
    
    results_fname = Path(outdir) / "results.xdmf"
    u0 = load_u(results_fname, 0, geo.mesh).copy(deepcopy=True)
    F0 = compute_F(u0)

    Eff_value = np.zeros((num_time_step,geo.mesh.num_cells()))

    for t in tqdm(range(num_time_step), desc="Calculating fiber strain", ncols=100):
        u_t = load_u(results_fname, t, geo.mesh)
        F_t = compute_F(u_t)
        E_t = compute_green_lagrange_strain(F_t, F0)
        Eff_t = compute_fiber_strain(E_t, geo.f0, geo.mesh)
        Eff_value[t,:] = Eff_t.vector()[:]
        
    altered_compartment_cfun = get_cfun_for_altered_compartment(segmentation_schema)
    compartments_indices = get_cfun_for_adjacent_compartment(altered_compartment_cfun, segmentation_schema, geo)
    for indices in compartments_indices:
        Eff_compartment = Eff_value[:,indices]
        Eff_compartment_ave = np.average(Eff_compartment, axis=1)
        plt.plot(Eff_compartment)
        plt.plot(Eff_compartment_ave)
        
#%%
outdir = Path("00_results/multi_core")
segmentation_schema = {
    "num_circ_segments": 7,
    "num_long_segments": 6,
}
num_time_step = 500
#%%
