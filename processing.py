# %%
import numpy as np
import logging
from pathlib import Path
import matplotlib.pyplot as plt
from dolfin import MPI
import pickle

from circ.circulation_model import CirculationModel
from circ.datacollector import DataCollector

from activation_model import compute_delayed_activations
from coupling_solver import circulation_solver
from heart_model import HeartModelPulse
from geometry import load_geo

# %%
# Dimensions
# [ms] [cm] [ml] [kPa]
comm = MPI.comm_world
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

outdir = Path('00_results/dev')


fname  = outdir / 'lv/geo.h5'
geo = load_geo(fname, comm=comm)
fe_model = HeartModelPulse(
        geo=geo,
        bc_params=bc_params,
    )

delayed_activations = []
if comm.rank == 1:  
    fname = outdir / 'a_data.pickle'
    with open(fname, 'rb') as file:
        delayed_activations = pickle.load(file)
MPI.barrier(comm)
delayed_activations = comm.bcast(delayed_activations, root=0)
    
circ_model = CirculationModel(params=circ_params)

# saving initial values
if comm.rank == 1:
    collector = DataCollector(outdir=outdir, problem=fe_model)
    collector.collect(
        time=0,
        pressure=0,
        volume=fe_model.compute_volume(activation_value=0, pressure_value=0),
        activation=0.0,
        flow=circ_model.flow,
        p_ao=circ_model.aortic_pressure,
    )
    
volume = fe_model.initial_loading(atrium_pressure=atrium_pressure)
if comm.rank == 1:
    collector.collect(
        time=0,
        pressure=atrium_pressure,
        volume=volume,
        activation=0.0,
        flow=circ_model.flow,
        p_ao=circ_model.aortic_pressure,
    )
    
t_span = (0.0, 1.0)
t_eval = np.linspace(*t_span, num_time_step)

collector = circulation_solver(
    heart_model=fe_model,
    circulation_model=circ_model,
    activation=delayed_activations,
    time=t_eval[:t_end] * 1000,
    collector=collector,
    start_time=2,
    comm = comm
)    
# %%