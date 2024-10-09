from pathlib import Path
import cardiac_geometries
import numpy as np
import matplotlib.pyplot as plt
import dolfin
import logging
import argparse
import arg_parser
import geometry

import beat
import beat.viz
import ORdmm_Land


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


def solve(outdir, geo_folder, stimulus_amplitude=1000, mesh_unit="cm"):
    ep_dir = outdir / "EP"
    ep_dir.mkdir(exist_ok=True, parents=True)

    model = ORdmm_Land.__dict__
    # data = load_geo_with_cfun(geo_folder)
    data_coarse = cardiac_geometries.geometry.Geometry.from_folder(geo_folder)
    data = cardiac_geometries.geometry.Geometry.from_folder(geo_folder)
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
        amplitude=1000.0,
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

    fname = ep_dir / "state.xdmf"
    if fname.exists():
        fname.unlink()

    fname_Ta = ep_dir / "activation.xdmf"
    if fname.exists():
        fname.unlink()

    i = 0
    while t < T + 1e-12:
        if i % 20 == 0:
            v = solver.pde.state.vector().get_local()
            print(f"Solve for {t=:.2f}, {v.max() =}, {v.min() = }")
            with dolfin.XDMFFile(dolfin.MPI.comm_world, fname.as_posix()) as xdmf:
                xdmf.parameters["functions_share_mesh"] = True
                xdmf.parameters["rewrite_function_mesh"] = False
                xdmf.write_checkpoint(
                    solver.pde.state,
                    "V",
                    float(t),
                    dolfin.XDMFFile.Encoding.HDF5,
                    True,
                )
            arr = Ta.vector().get_local().copy()
            for marker in solver.ode._marker_values:
                monitor_values = model["monitor_values"](
                    t, solver.ode.values(marker=marker), solver.ode.parameters[marker]
                )
                arr[solver.ode._inds[marker]] = monitor_values[Ta_index]
            Ta.vector().set_local(arr)
            with dolfin.XDMFFile(dolfin.MPI.comm_world, fname_Ta.as_posix()) as xdmf:
                xdmf.parameters["functions_share_mesh"] = True
                xdmf.parameters["rewrite_function_mesh"] = False
                xdmf.write_checkpoint(
                    Ta,
                    "activation",
                    float(t),
                    dolfin.XDMFFile.Encoding.HDF5,
                    True,
                )
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