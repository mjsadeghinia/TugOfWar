from pathlib import Path
import cardiac_geometries
import numpy as np
import matplotlib.pyplot as plt
import dolfin
import logging
import argparse
import arg_parser
import geometry
import stl
import gmsh
import math
import os
from structlog import get_logger

import beat
import beat.viz
import ORdmm_Land


logger = get_logger()

def load_geo_with_cfun(geo_folder):
    schema = cardiac_geometries.geometry.Geometry.default_schema()
    cfun_schema = schema["cfun"]._asdict()
    cfun_schema["fname"] = "cfun.xdmf:f"
    schema["cfun"] = cardiac_geometries.geometry.H5Path(**cfun_schema)
    geo = cardiac_geometries.geometry.Geometry.from_folder(geo_folder, schema=schema)
    return geo


def refine_geo(geo, geo_refinement):
    mesh, cfun, ffun = geo.mesh, geo.cfun, geo.ffun
    dolfin.parameters["refinement_algorithm"] = "plaza_with_parent_facets"
    for _ in range(geo_refinement):
        mesh = dolfin.adapt(mesh)
        cfun = dolfin.adapt(cfun, mesh)
        ffun = dolfin.adapt(ffun, mesh)

    geo.f0.set_allow_extrapolation(True)
    geo.s0.set_allow_extrapolation(True)
    geo.n0.set_allow_extrapolation(True)

    V_refined = dolfin.FunctionSpace(mesh, geo.f0.function_space().ufl_element())

    f0_refined = dolfin.Function(V_refined)
    f0_refined.interpolate(geo.f0)
    s0_refined = dolfin.Function(V_refined)
    s0_refined.interpolate(geo.s0)
    n0_refined = dolfin.Function(V_refined)
    n0_refined.interpolate(geo.n0)

    geo.mesh = mesh
    geo.cfun = cfun
    geo.ffun = ffun
    geo.f0 = f0_refined
    geo.s0 = s0_refined
    geo.n0 = n0_refined

    return geo
def remesh_surface(stl_fname, mesh_size=1):
    """
    Remeshes a 3D surface mesh from an STL file with a specified mesh size
    and saves the output in STL format with a "_coarse" suffix.

    Parameters:
    - stl_fname: str to the input STL file.
    - mesh_size: float, characteristic length for mesh elements (higher values for coarser mesh).

    Returns:
    - vertices: numpy array of shape (n_nodes, 3)
    - faces: numpy array of shape (n_faces, 3), indices into vertices
    """
    # Check if the file exists
    if not os.path.isfile(stl_fname):
        logger.error(f"Error: File '{stl_fname}' not found.")
        return None, None

    # Initialize Gmsh
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)  # Enable terminal output

    try:
        gmsh.merge(stl_fname)
        # Classify surfaces to create geometry
        angle = 60 # Angle threshold for feature detection in degrees
        force_parametrizable_patches = True
        include_boundary = True
        curve_angle = 180  # For sewing surfaces

        gmsh.model.mesh.classifySurfaces(
            angle * math.pi / 180.0, include_boundary,
            force_parametrizable_patches,
            curve_angle * math.pi / 180.0
        )

        # Create geometry from the classified surfaces
        gmsh.model.mesh.createGeometry()

        # Synchronize the model
        gmsh.model.geo.synchronize()

        # Set the specified mesh size
        gmsh.model.mesh.setSize(gmsh.model.getEntities(0), mesh_size)

        # Generate the 2D mesh
        gmsh.model.mesh.generate(2)

        # Extract nodes and elements
        node_tags, node_coords, _ = gmsh.model.mesh.getNodes()
        vertices = np.array(node_coords).reshape(-1, 3)

        # Create a mapping from node tags to indices
        node_index = {tag: idx for idx, tag in enumerate(node_tags)}

        elementType = 2  # 3-node triangle
        _, element_node_tags = gmsh.model.mesh.getElementsByType(elementType)
        element_node_tags = np.array(element_node_tags).reshape(-1, 3)

        # Map node tags to indices to create faces array
        faces = np.array([[node_index[tag] for tag in tri] for tri in element_node_tags])

        # Save the mesh in STL format
        gmsh.write(stl_fname)
        # Return vertices and faces
        return vertices, faces

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None, None

    finally:
        # Finalize Gmsh
        gmsh.finalize()
        
        
def generate_3d_mesh_from_seperate_stl(mesh_epi, mesh_endo, mesh_base, output_mesh_filename,  MeshSizeMin=None, MeshSizeMax=None):
    # Initialize Gmsh
    gmsh.initialize()
    gmsh.model.add("3D Mesh")
    gmsh.option.setNumber("General.Verbosity", 0)

    # Merge the STL files
    gmsh.merge(mesh_epi)
    gmsh.merge(mesh_endo)
    gmsh.merge(mesh_base)

    gmsh.model.mesh.removeDuplicateNodes()
    gmsh.model.mesh.create_geometry()
    gmsh.model.mesh.create_topology()
    surfaces = gmsh.model.getEntities(2)
    
    gmsh.model.geo.addSurfaceLoop([s[1] for s in surfaces], 1)
    vol = gmsh.model.geo.addVolume([1], 1)
    
    physical_groups = {
        "Epi": [1],
        "Endo": [2],
        "Base": [3],
    }
    for name, tag in physical_groups.items():
        p = gmsh.model.addPhysicalGroup(2, tag)
        gmsh.model.setPhysicalName(2, p, name)

    p = gmsh.model.addPhysicalGroup(3, [vol], 9)
    gmsh.model.setPhysicalName(3, p, "Wall")

    if MeshSizeMin is not None:
        gmsh.option.setNumber('Mesh.MeshSizeMin', MeshSizeMin)
    if MeshSizeMax is not None:
        gmsh.option.setNumber('Mesh.MeshSizeMax', MeshSizeMax)
            
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(3)
    # Save the mesh to the specified file
    gmsh.write(output_mesh_filename)
    # Finalize Gmsh
    gmsh.finalize()
    
    
def export_facet_as_stl(geo, facet_number, fname):
    vertices = []
    triangles = []
    vertex_map = {}  # To map old node numbers to new ones
    next_vertex_id = 0  # Counter for new vertices

    facets = dolfin.facets(geo.mesh)
    # Iterate over the facets of the mesh
    for facet in facets:
        if geo.ffun[facet] == facet_number:
            # Get the original global node numbers for this facet
            nodes_number = facet.entities(0)
            # Array to store the local (new) node numbers for this facet
            local_triangle = []
            # Iterate over each node in the facet
            for node in nodes_number:
                if node not in vertex_map:
                    # If the node is not yet mapped, add it to vertices and map it
                    vertex_map[node] = next_vertex_id
                    vertices.append(geo.mesh.coordinates()[node])
                    next_vertex_id += 1

                # Add the mapped vertex to the local triangle
                local_triangle.append(vertex_map[node])

            # Append the triangle (facet) to the triangles list
            triangles.append(local_triangle)
    
    # Convert the vertices and triangles to numpy arrays for STL export
    vertices = np.array(vertices)
    triangles = np.array(triangles)
    stl_mesh = stl.mesh.Mesh(np.zeros(triangles.shape[0], dtype=stl.mesh.Mesh.dtype))
    # Assign vertices and triangles to the STL mesh
    for i, triangle in enumerate(triangles):
        for j in range(3):  # Loop over the three vertices of the triangle
            stl_mesh.vectors[i][j] = vertices[triangle[j]]
    
    # Save the STL file
    stl_mesh.save(fname)

    
def refine_goe_gmsh(geo, outdir, surface_mesh_size=.2, MeshSizeMin=.1, MeshSizeMax=.3):
    geo_folder = outdir / 'lv_refined'
    geo_folder.mkdir(exist_ok = True)
    epi_stl_fname = geo_folder / 'epi.stl'
    endo_stl_fname = geo_folder / 'endo.stl'
    base_stl_fname = geo_folder / 'base.stl'
    export_facet_as_stl(geo, 7, epi_stl_fname.as_posix())
    export_facet_as_stl(geo, 6, endo_stl_fname.as_posix())
    export_facet_as_stl(geo, 5, base_stl_fname.as_posix())
    remesh_surface(epi_stl_fname.as_posix(), mesh_size=surface_mesh_size)
    remesh_surface(endo_stl_fname.as_posix(), mesh_size=surface_mesh_size)
    remesh_surface(base_stl_fname.as_posix(), mesh_size=surface_mesh_size)
    breakpoint()
    output_mesh_filename = geo_folder / '3D_Mesh.stl'
    generate_3d_mesh_from_seperate_stl(epi_stl_fname.as_posix(), endo_stl_fname.as_posix(), base_stl_fname.as_posix(), output_mesh_filename,  MeshSizeMin=MeshSizeMin, MeshSizeMax=MeshSizeMax)
    return

class Interpolator:
    def __init__(self, src: dolfin.FunctionSpace, dst: dolfin.FunctionSpace) -> None:
        self.transfer_matrix = dolfin.PETScDMCollection.create_transfer_matrix(src, dst).mat()

    def assign(self, src: dolfin.Function, dst: dolfin.Function) -> None:
        x = dolfin.as_backend_type(src.vector()).vec()
        a, temp = self.transfer_matrix.getVecs()
        self.transfer_matrix.mult(x, temp)
        dst.vector().vec().aypx(0.0, temp)
        dst.vector().apply("")

        # Remember to free memory allocated by petsc: https://gitlab.com/petsc/petsc/-/issues/1309
        x.destroy()
        a.destroy()
        temp.destroy()

def interpolate(function, data, data_coarse):
    V_coarse = dolfin.FunctionSpace(data_coarse.mesh, "DG", 0)
    V = dolfin.FunctionSpace(data.mesh, "Lagrange", 1)
    function_coarse = dolfin.Function(V_coarse)
    interpolator_dg0 = Interpolator(V, V_coarse)
    interpolator_dg0.assign(function, function_coarse)
    return function_coarse

def compute_activation(Ta, Ta_index, ode, model, t):
    arr = Ta.vector().get_local().copy()
    for marker in ode._marker_values:
        monitor_values = model["monitor_values"](
            t, ode.values(marker=marker), ode.parameters[marker]
        )
        arr[ode._inds[marker]] = monitor_values[Ta_index]
    Ta.vector().set_local(arr)
    return Ta

def save_xdmf(fname, name, t, func):
    with dolfin.XDMFFile(fname) as xdmf:
        xdmf.parameters["functions_share_mesh"] = True
        xdmf.parameters["rewrite_function_mesh"] = False
        xdmf.write_checkpoint(
            func,
            name,
            float(t),
            dolfin.XDMFFile.Encoding.HDF5,
            True,
        )


def solve(outdir, geo_folder, stimulus_amplitude=1000, mesh_unit="cm"):
    ep_dir = outdir / "EP"
    ep_dir.mkdir(exist_ok=True, parents=True)

    model = ORdmm_Land.__dict__
    # data = load_geo_with_cfun(geo_folder)
    data_coarse = cardiac_geometries.geometry.Geometry.from_folder(geo_folder)
    data = cardiac_geometries.geometry.Geometry.from_folder(geo_folder)
    #data = geometry.load_geo_with_cfun(geo_folder)
    refine_goe_gmsh(data, outdir)
    data = refine_geo(data, 2)
    # Saving ffun
    fname = ep_dir / "ffun_refined.xdmf"
    with dolfin.XDMFFile(fname.as_posix()) as infile:
        infile.write(data.ffun)

    V = dolfin.FunctionSpace(data.mesh, "Lagrange", 1)
    markers = beat.utils.expand_layer(
        V=V,
        mfun=data.ffun,
        endo_marker=data.markers["ENDO"][0],
        epi_marker=data.markers["EPI"][0],
        endo_size=0.3,
        epi_size=0.3,
    )

    # parameters
    init_states = {
        0: model["init_state_values"](),
        1: model["init_state_values"](),
        2: model["init_state_values"](),
    }
    # endo = 0, epi = 1, M = 2
    parameters = {
        0: model["init_parameter_values"](amp=0.0, celltype=2),
        1: model["init_parameter_values"](amp=0.0, celltype=0),
        2: model["init_parameter_values"](amp=0.0, celltype=1),
    }
    fun = {
        0: model["forward_generalized_rush_larsen"],
        1: model["forward_generalized_rush_larsen"],
        2: model["forward_generalized_rush_larsen"],
    }
    v_index = {
        0: model["state_index"]("v"),
        1: model["state_index"]("v"),
        2: model["state_index"]("v"),
    }

    # Surface to volume ratio
    chi = 140.0 * beat.units.ureg("mm**-1")
    # Membrane capacitance
    C_m = 0.01 * beat.units.ureg("uF/mm**2")

    time = dolfin.Constant(0.0)

    subdomain_data = dolfin.MeshFunction("size_t", data.mesh, 2)
    subdomain_data.set_all(0)
    marker = 1
    subdomain_data.array()[data.ffun.array() == data.markers["ENDO"][0]] = 1
    I_s = beat.stimulation.define_stimulus(
        mesh=data.mesh,
        chi=chi,
        mesh_unit=mesh_unit,
        time=time,
        subdomain_data=subdomain_data,
        marker=marker,
        amplitude=stimulus_amplitude,
    )

    M = beat.conductivities.define_conductivity_tensor(
        chi=chi, f0=data.f0, g_il=0.17, g_it=0.019, g_el=0.62, g_et=0.24
    )

    params = {"preconditioner": "sor", "use_custom_preconditioner": False}
    pde = beat.MonodomainModel(
        time=time,
        C_m=C_m.to(f"uF/{mesh_unit}**2").magnitude,
        mesh=data.mesh,
        M=M,
        I_s=I_s,
        params=params,
    )

    ode = beat.odesolver.DolfinMultiODESolver(
        v_ode=dolfin.Function(V),
        v_pde=pde.state,
        markers=markers,
        num_states={i: len(s) for i, s in init_states.items()},
        fun=fun,
        init_states=init_states,
        parameters=parameters,
        v_index=v_index,
    )

    T = 500
    t = 0.0
    dt = 0.05
    solver = beat.MonodomainSplittingSolver(pde=pde, ode=ode)

    beat_logger = logging.getLogger("beat")
    beat_logger.setLevel(logging.WARNING)

    Ta = dolfin.Function(pde.V)
    Ta_index = model["monitor_index"]("Ta")
    V_coarse = dolfin.FunctionSpace(data_coarse.mesh, "DG", 0)
    Ta_coarse = dolfin.Function(V_coarse)

    fname_state = ep_dir / "state.xdmf"
    if fname_state.exists():
        fname_state.unlink()

    fname_Ta = ep_dir / "activation.xdmf"
    if fname_Ta.exists():
        fname_Ta.unlink()

    fname_Ta_coarse = ep_dir / "activation_coarse.xdmf"
    if fname_Ta_coarse.exists():
        fname_Ta_coarse.unlink()
        
    i = 0
    while t < T + 1e-12:
        if i % 20 == 0:
            v = solver.pde.state.vector().get_local()
            print(f"Solve for {t=:.2f}, {v.max() =}, {v.min() = }")
            Ta = compute_activation(Ta, Ta_index, ode, model, t)
            Ta_coarse = interpolate(Ta,data,data_coarse)
            save_xdmf(fname_state.as_posix(), "V", t, solver.pde.state)
            save_xdmf(fname_Ta.as_posix(), "activation", t, Ta)
            save_xdmf(fname_Ta_coarse.as_posix(), "activation", t, Ta_coarse)
            
        solver.step((t, t + dt))
        i += 1
        t += dt


def main(args=None) -> int:
    # Getting the arguments

    parser = argparse.ArgumentParser()

    # Geometry parameters
    parser.add_argument(
        "-m",
        "--mesh_size",
        default=0.5,
        type=float,
        help="The mesh size, approximate length of the edge for tetrahedrons [in cm]",
    )
    parser.add_argument(
        "--r_short_endo",
        default=3,
        type=float,
        help="The short radius of endocardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_short_epi",
        default=3.75,
        type=float,
        help="The short radius of epicardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_long_endo",
        default=4.25,
        type=float,
        help="The long radius of endocardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_long_epi",
        default=5,
        type=float,
        help="The long radius of epicardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    # Segmentation parameters
    parser.add_argument(
        "-c",
        "--num_circ_segments",
        default=72,
        type=int,
        help="The number of circumferential compartments per slice",
    )
    parser.add_argument(
        "-l",
        "--num_long_segments",
        default=6,
        type=int,
        help="The number of slices (longitudinal)",
    )

    # Modeling and export parameters
    parser.add_argument(
        "-r",
        "--refinement",
        default=1,
        type=int,
        help="The number of refinement for the mesh",
    )
    parser.add_argument(
        "-s",
        "--stimulus_amplitude",
        default=1000,
        type=float,
        help="The amplitude of the stimulus",
    )

    parser.add_argument(
        "-o",
        "--outdir",
        default=Path.cwd() / "output",
        type=Path,
        help="The output directory to save the files.",
    )

    parser.add_argument(
        "-g",
        "--geo_folder",
        default="lv",
        type=str,
        help="The folder containing the geometry",
    )
    args = parser.parse_args(args)
    geo_params = arg_parser.create_geo_params(args)
    segmentation_schema = arg_parser.create_segmentation_schema(args)

    ## Creating Geometry
    outdir = args.outdir
    geo_folder = outdir / args.geo_folder
    geo = geometry.create_ellipsoid_geometry(
        folder=geo_folder,
        geo_params=geo_params,
        segmentation_schema=segmentation_schema,
    )
    
    solve(outdir, geo_folder, mesh_unit="cm")


if __name__ == "__main__":
    main()
