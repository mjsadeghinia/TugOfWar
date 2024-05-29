#%%
import dolfin
from fenics_plotly import plot

from heart_model import HeartModelPulse

#%%
geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 5,
    "r_long_epi": 5.75,
    "mesh_size": 2.5,
}
bc_params = {"pericardium_spring": 0.0001}

fe_model = HeartModelPulse(geo_params=geo_params, bc_params=bc_params)

#%%
mesh, cfun, ffun = fe_model.geometry.mesh, fe_model.geometry.cfun, fe_model.geometry.ffun 
f0 = fe_model.geometry.f0
num_refinements = 1

print(
    f"Original mesh has {mesh.num_cells()} cells, "
    f"{mesh.num_facets()} facets and "
    f"{mesh.num_vertices()} vertices"
)
dolfin.parameters["refinement_algorithm"] = "plaza_with_parent_facets"
for _ in range(num_refinements):
    mesh_refined = dolfin.adapt(mesh)
    cfun_refined = dolfin.adapt(cfun, mesh_refined)
    ffun_refined = dolfin.adapt(ffun, mesh_refined)
    print(
    f"The mesh has refined with {mesh_refined.num_cells()} cells, "
    f"{mesh_refined.num_facets()} facets and "
    f"{mesh_refined.num_vertices()} vertices"
)
V = dolfin.VectorFunctionSpace(mesh_refined, 'Lagrange',3)
f0_refined = dolfin.Function(V)
f0_refined.interpolate(f0)   

# %%
