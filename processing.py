# %%
import numpy as np
from pathlib import Path
import dolfin
import cardiac_geometries

from circ.circulation_model import CirculationModel
from circ.datacollector import DataCollector

from coupling_solver import circulation_solver
from heart_model import HeartModelPulse

# %%
# Dimensions
# [ms] [cm] [ml] [kPa]


def process(
    outdir, num_time_step, t_end, circ_params, bc_params, atrium_pressure, comm=None
):
    if comm is None:
        comm = dolfin.MPI.comm_world
    fname = outdir / "lv/geo.h5"
    geo = cardiac_geometries.geometry.Geometry.from_file(fname.as_posix(), comm=comm)
    heart_model = HeartModelPulse(geo=geo, bc_params=bc_params, comm=comm)

    circulation_model = CirculationModel(params=circ_params)
    collector = DataCollector(outdir=outdir, problem=heart_model)
    # saving initial values
    v = heart_model.compute_volume(activation_value=0, pressure_value=0)
    collector.collect(
        time=0,
        pressure=0,
        volume=v,
        activation=0.0,
        flow=circulation_model.flow,
        p_ao=circulation_model.aortic_pressure,
    )

    volume = heart_model.initial_loading(atrium_pressure=atrium_pressure)
    collector.collect(
        time=0,
        pressure=atrium_pressure,
        volume=volume,
        activation=0.0,
        flow=circulation_model.flow,
        p_ao=circulation_model.aortic_pressure,
    )

    t_span = (0.0, 1.0)
    t_eval = np.linspace(*t_span, num_time_step)
    activation_fname = outdir / "activation.xdmf"

    collector = circulation_solver(
        heart_model=heart_model,
        circulation_model=circulation_model,
        activation_fname=activation_fname,
        time=t_eval[:t_end] * 1000,
        collector=collector,
        start_time=2,
        comm=comm,
    )


# %%
comm = dolfin.MPI.comm_world
circ_params = {
    "aortic_resistance": 5,
    "systematic_resistance": 10,
    "systematic_compliance": 10,
    "aortic_pressure": 10,
    "diastolic_pressure": 10,
    "initial_pressure": 0.0,
}
bc_params = {"pericardium_spring": 0.0001}
atrium_pressure = 1
num_time_step = 500
t_end = 350
# %%
delay = 0.05
delay_mode = "delay"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
process(outdir, num_time_step, t_end, circ_params, bc_params, atrium_pressure)

# %%
delay = 0.05
delay_mode = "activation"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
process(outdir, num_time_step, t_end, circ_params, bc_params, atrium_pressure)

# %%
delay = 0.05
delay_mode = "diastole_time"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
process(outdir, num_time_step, t_end, circ_params, bc_params, atrium_pressure)
