from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

import dolfin
import pulse
from geometry import load_geo_with_cfun, get_cfun_for_altered_compartment, get_cfun_for_adjacent_compartment



# %%
def load_mesh(fname: Path):
    # Read the mesh
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        mesh = dolfin.Mesh()
        xdmf.read(mesh)
    return mesh

def load_u(fname: Path, t: float, mesh: dolfin.mesh):
    V = dolfin.VectorFunctionSpace(mesh, "CG", 2)
    u = dolfin.Function(V)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(u, "Displacement", t)
    return u

def load_E(fname: Path, t: float, mesh: dolfin.mesh):
    tensor_element = dolfin.TensorElement("DG", mesh.ufl_cell(), 0)
    function_space = dolfin.FunctionSpace(mesh, tensor_element)
    E = dolfin.Function(function_space)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(E, "Green Lagrange Strain", t)
    return E

def compute_fiber_strain(E: dolfin.Function, fib0: dolfin.Function, mesh: dolfin.mesh):
    V = dolfin.FunctionSpace(mesh, "DG", 0)
    Eff = dolfin.project(dolfin.inner(E * fib0, fib0), V)
    return Eff

#%%
def main(outdir, num_time_step, segmentation_schema):
    geo_folder = Path(outdir) / 'lv'
    geo =  load_geo_with_cfun(geo_folder)
    
    E_fname = outdir / "Green Lagrange Strain.xdmf"
    Eff_value = np.zeros((num_time_step,geo.mesh.num_cells()))
    Eff_value = []
    for t in range(num_time_step):
        try: 
            E_t = load_E(E_fname, t, geo.mesh)
            Eff_t = compute_fiber_strain(E_t, geo.f0, geo.mesh)
            # Eff_value[t,:] = Eff_t.vector()[:]
            Eff_value.append(Eff_t.vector()[:])
        except:
            break
    
    t_tot = len(Eff_value)
    Eff_value_arr = np.array(Eff_value)
        
    altered_compartment_cfun = get_cfun_for_altered_compartment(segmentation_schema)
    compartments_indices = get_cfun_for_adjacent_compartment(altered_compartment_cfun, segmentation_schema, geo)
    for indices in compartments_indices:
        Eff_compartment = Eff_value_arr[:,indices]
        Eff_compartment_ave = np.average(Eff_compartment, axis=1)
        plt.plot(Eff_compartment)
        plt.plot(Eff_compartment_ave)
        
#%%
outdir = Path("00_results/dev")
segmentation_schema = {
    "num_circ_segments": 7,
    "num_long_segments": 6,
}
num_time_step = 500
#%%
