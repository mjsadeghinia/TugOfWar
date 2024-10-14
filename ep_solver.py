from pathlib import Path
import cardiac_geometries
import numpy as np
import matplotlib.pyplot as plt
import dolfin
import logging
import argparse
from structlog import get_logger

import beat
import beat.viz
import ORdmm_Land


logger = get_logger()


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

def interpolate(function, geo, geo_coarse):
    function.set_allow_extrapolation(True)
    V_coarse = dolfin.FunctionSpace(geo_coarse.mesh, "DG", 0)
    V = dolfin.FunctionSpace(geo.mesh, "Lagrange", 1)
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

def save_xdmf_mpi(fname, name, t, func, comm):
    with dolfin.XDMFFile(comm, fname) as xdmf:
        xdmf.parameters["functions_share_mesh"] = True
        xdmf.parameters["rewrite_function_mesh"] = False
        xdmf.write_checkpoint(
            func,
            name,
            float(t),
            dolfin.XDMFFile.Encoding.HDF5,
            True,
        )

def solve(outdir, geo_folder_coarse, geo_folder_fine, stimulus_amplitude=1000, mesh_unit="cm"):        
    ep_dir = outdir / "EP"
    ep_dir.mkdir(exist_ok=True, parents=True)

    model = ORdmm_Land.__dict__
    geo_coarse = cardiac_geometries.geometry.Geometry.from_folder(geo_folder_coarse)
    geo = cardiac_geometries.geometry.Geometry.from_folder(geo_folder_fine)
    # geo = refine_geo(geo, refinement)
    # Saving ffun

    V = dolfin.FunctionSpace(geo.mesh, "Lagrange", 1)
    markers = beat.utils.expand_layer(
        V=V,
        mfun=geo.ffun,
        endo_marker=geo.markers["ENDO"][0],
        epi_marker=geo.markers["EPI"][0],
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

    subdomain_geo = dolfin.MeshFunction("size_t", geo.mesh, 2)
    subdomain_geo.set_all(0)
    marker = 1
    subdomain_geo.array()[geo.ffun.array() == geo.markers["ENDO"][0]] = 1
    I_s = beat.stimulation.define_stimulus(
        mesh=geo.mesh,
        chi=chi,
        mesh_unit=mesh_unit,
        time=time,
        subdomain_data=subdomain_geo,
        marker=marker,
        amplitude=stimulus_amplitude,
    )

    M = beat.conductivities.define_conductivity_tensor(
        chi=chi, f0=geo.f0, g_il=0.17, g_it=0.019, g_el=0.62, g_et=0.24
    )

    params = {"preconditioner": "sor", "use_custom_preconditioner": False}
    pde = beat.MonodomainModel(
        time=time,
        C_m=C_m.to(f"uF/{mesh_unit}**2").magnitude,
        mesh=geo.mesh,
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
    V_coarse = dolfin.FunctionSpace(geo_coarse.mesh, "DG", 0)
    Ta_coarse = dolfin.Function(V_coarse)
    State_coarse = dolfin.Function(V_coarse)
    
    fname_state = ep_dir / "state_coarse.xdmf"
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
            Ta_coarse = interpolate(Ta,geo,geo_coarse)
            State_coarse = interpolate(solver.pde.state,geo,geo_coarse)
            save_xdmf(fname_state.as_posix(), "V", t, State_coarse)
            #save_xdmf(fname_Ta.as_posix(), "activation", t, Ta)
            save_xdmf(fname_Ta_coarse.as_posix(), "activation", t, Ta_coarse)
            
        solver.step((t, t + dt))
        i += 1
        t += dt


def main(args=None) -> int:
    comm = dolfin.MPI.comm_world
    # Getting the arguments
    parser = argparse.ArgumentParser()
    
    # Modeling and export parameters
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
    stimulus_amplitude = args.stimulus_amplitude
    outdir = args.outdir
    geo_folder_coarse = outdir / f"{args.geo_folder}_coarse"
    geo_folder_fine = outdir / f"{args.geo_folder}_fine"

    solve(outdir, geo_folder_coarse, geo_folder_fine, stimulus_amplitude=stimulus_amplitude, mesh_unit="cm")


if __name__ == "__main__":
    main()
