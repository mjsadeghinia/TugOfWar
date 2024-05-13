# %%
import numpy as np
import logging
from pathlib import Path
import matplotlib.pyplot as plt

from activation_model import compute_delayed_activations
from coupling_solver import circulation_solver
from circ.circulation_model import CirculationModel
from circ.datacollector import DataCollector
from heart_model import HeartModelPulse
# %%
# Dimensions
# [ms] [cm] [ml] [kPa] 

def main(
    t_end=550, num_time_step=1000, delay=0.01, geo_params={}, circ_params={}, bc_params={}, outdir=Path("results")
):
    logging.getLogger("pulse").setLevel(logging.WARNING)
    t_span = (0, 1)
    fe_model = HeartModelPulse(geo_params=geo_params,bc_params=bc_params)
    delayed_activations = compute_delayed_activations(
        fe_model.geometry.cfun, num_time_step=num_time_step, std=delay
    )
    circ_model = CirculationModel(params=circ_params)
    outname = Path(outdir) / "results.xdmf"
    if outname.is_file():
        outname.unlink()
        outname.with_suffix(".h5").unlink()
    collector = DataCollector(outdir=outdir, problem=fe_model)
    # Increase to atrial pressure
    for pressure in [0.0, 0.2]:
        volume = fe_model.compute_volume(activation_value=0, pressure_value=pressure)
        collector.collect(
            time=0,
            pressure=pressure,
            volume=volume,
            activation=0.0,
            flow=circ_model.flow,
            p_ao=circ_model.aortic_pressure,
        )
    t_eval = np.linspace(*t_span, num_time_step)
    #  we use only the first 700ms, as the relaxation is not yet implemented
    collector = circulation_solver(
        heart_model=fe_model,
        circulation_model=circ_model,
        activation=delayed_activations,
        time=t_eval[:t_end] * 1000,
        collector=collector,
        start_time=2,
    )
    return collector, fe_model, circ_model, delayed_activations


# %%


def plot_strains_aha(Eff, num_time_step=1000, outdir=Path("results")):
    plots_path = outdir / "plots"
    plots_path.mkdir(parents=True, exist_ok=True)

    total_time = len(Eff)
    num_aha_segments = len(Eff[0])
    for n in range(num_aha_segments):
        data = [Eff[t][n] for t in range(total_time)]
        data_array = np.array(data)
        file_path = plots_path / f"strains_aha_{n + 1}.png"

        plt.figure()
        plt.plot(np.linspace(0,len(data)*1000/num_time_step,len(data)),data_array, "k-", linewidth=0.1)
        plt.plot(np.linspace(0,len(data)*1000/num_time_step,len(data)),np.average(data_array, axis=1), "r-", linewidth=1)
        plt.xlabel("Time [ms]")
        plt.ylabel("Green-Lagrange Fiber Strain (-)")
        plt.ylim((-0.35, 0.35))
        plt.savefig(file_path)
        plt.close()


# %%

geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 5,
    "r_long_epi": 5.75,
    "mesh_size": 1,
}
circ_params = {
    "aortic_resistance": 10,
    "systematic_resistance": 10,
    "systematic_compliance": 10,
    "aortic_pressure": 10,
    "diastolic_pressure": 10,
    "initial_pressure": 0.0,
}

bc_params = {
    "pericardium_spring": 0.0001
}

outdir = Path('00_results/forward_1')
collector, fe_model, circ_model, delayed_activations = main(
    num_time_step=500, t_end=260, delay=0.0, geo_params=geo_params, bc_params=bc_params, circ_params=circ_params, outdir=outdir
)
plot_strains_aha(fe_model.E_ff, num_time_step=500, outdir=outdir)
#%%
from forward_problem import filter_volume_changes
from forward_problem import forward_solver

data = collector.read_csv()

data_filtered, delayed_activations_filtered = filter_volume_changes(data, delayed_activations, 1e-3)

fig, ax = plt.subplots(
            1, 1, figsize=(6, 6)
        ) 
ax.scatter(data_filtered["volume"],data_filtered["lv_pressure"])
ax.set_ylabel("Pressure (kPa)")
ax.set_xlabel("Volume (ml)")
ax2 = ax.twinx()
pressures_mmHg = np.array(data_filtered["lv_pressure"]) * 7.50062 #Convert to mmHg
# Plotting the same data but converted on the second y-axis
ax2.plot(data_filtered["volume"], pressures_mmHg, 'r-', alpha=0)  # invisible plot just for axis
ax2.set_ylabel('Pressure (mmHg)')
# %%
geo_params_highres = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 5,
    "r_long_epi": 5.75,
    "mesh_size": 0.5,
}

fe_model_highres = HeartModelPulse(geo_params=geo_params_highres,bc_params=bc_params)
outdir_highres = Path('00_results/forward/highres')
outname = Path(outdir_highres) / "results.xdmf"
if outname.is_file():
    outname.unlink()
    outname.with_suffix(".h5").unlink()
collector_highres = DataCollector(outdir=outdir_highres, problem=fe_model)

forward_solver(fe_model_highres,delayed_activations_filtered,data_filtered["lv_pressure"],data_filtered["time"],collector_highres)
# %%
