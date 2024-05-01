#%%
import dolfin.function
import numpy as np
import scipy.stats as stats
import logging
import matplotlib.pyplot as plt
from pathlib import Path
from tqdm import tqdm

import cardiac_geometries
import pulse
import activation_model
from coupling_solver import circulation_solver
from circ.circulation_model import CirculationModel
from circ.datacollector import DataCollector
from heart_model import HeartModelPulse
import dolfin
#%%

num_time_step = 1000

#%% Creating the Finite Element Model of a Simplified LV
def get_ellipsoid_geometry(folder=Path("lv")):
    # Create geometry
    cardiac_geometries.create_lv_ellipsoid(
        folder,
        create_fibers=True,
        aha=True,
        r_short_endo  = 3.0,
        r_short_epi = 3.75,
        r_long_endo = 5.0,
        r_long_epi = 5.75,
        psize_ref = 2.5
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


geometry = get_ellipsoid_geometry()
fe_model=HeartModelPulse(geo=geometry)
target_activation = dolfin.Function(fe_model.activation.ufl_function_space())

# %%
def get_elems(cfun, cfun_num):
    indices=np.where(cfun.array() == cfun_num)[0]
    return indices

def compute_delayed_activations(cfun, devaiation=0.01, aha_segments_num=np.linspace(1,17,17), t_span=(0.0, 1.0), num_time_step=20):
    t_eval = np.linspace(*t_span, num_time_step)
    normal_activation_params = activation_model.default_parameters()
    delayed_activations=[]
    for n in tqdm(aha_segments_num, desc="Creating Delayed Activation Curves", ncols=100):
        elems = get_elems(cfun,n)
        num_elems = len(elems)
        offsets = stats.norm.ppf(np.linspace(0.01, 0.99, num_elems), loc=0, scale=devaiation)
        segment_delayed_activations=np.zeros((len(t_eval),num_elems))
        for i, offset in enumerate(offsets):
            segment_delayed_activation_params = normal_activation_params.copy()
            segment_delayed_activation_params["t_sys"] += offset
            segment_delayed_activation_params["t_dias"] += offset
            segment_delayed_activation = (
            activation_model.activation_function(
                t_span=t_span,
                t_eval=t_eval,
                parameters=segment_delayed_activation_params,
            )
            / 1000.0
        )
            segment_delayed_activations[:,i]=segment_delayed_activation
        delayed_activations.append(segment_delayed_activations)
    return delayed_activations

delayed_activations=compute_delayed_activations(fe_model.geometry.cfun, num_time_step=num_time_step)

#%%
logging.getLogger("pulse").setLevel(logging.WARNING)
circ_model = CirculationModel()

outdir = Path("results")
outname = Path(outdir) / "results.xdmf"
if outname.is_file():
    outname.unlink()
    outname.with_suffix(".h5").unlink()
collector = DataCollector(outdir=outdir, problem=fe_model)

# Increase to atrial pressure
for pressure in [0.0, 0.01]:
    volume = fe_model.compute_volume(activation_value=0, pressure_value=pressure)
    collector.collect(
        time=0,
        pressure=pressure,
        volume=volume,
        activation=0.0,
        flow=circ_model.flow,
        p_ao=circ_model.aortic_pressure,
    )
#%%
t_end = 650
t_span = (0, 1)
t_eval = np.linspace(*t_span, num_time_step)
#  we use only the first 700ms, as the relaxation is not yet implemented
circulation_solver(
    heart_model=fe_model,
    circulation_model=circ_model,
    activation=delayed_activations,
    time=t_eval[:t_end] * 1000,
    collector=collector,
    start_time=2,
)

# %%
# fe_model.geometry.cfun.array().shape
# plt.plot(np.array(fe_model.E_ff)[:,:100])
# # %%
# idx=[]
# for cell in dolfin.cells(fe_model.geometry.mesh):
#     if fe_model.geometry.cfun[cell]==1:
#         idx.append(cell.entities(0))

# # Use Counter to count the frequency of each element
# element_counts = Counter(np.array(idx).flatten())

# # Filter to find elements that appear exactly once
# unique_elements = [element for element, count in element_counts.items() if count == 1]
# unique_elements
# # %%
