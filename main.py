# %%
import numpy as np
import logging
from pathlib import Path
import matplotlib.pyplot as plt

from circ.circulation_model import CirculationModel
from circ.datacollector import DataCollector

from activation_model import compute_delayed_activations
from coupling_solver import circulation_solver
from utils import data_sampleing, data_plotting
from forward_problem import forward_solver
from heart_model import HeartModelPulse

# %%
# Dimensions
# [ms] [cm] [ml] [kPa]


def main(
    t_end=550,
    num_time_step=1000,
    atrium_pressure=0.2,
    delay=0.01,
    delay_mode="delay",
    geo_params={},
    circ_params={},
    bc_params={},
    geo_folder=None,
    outdir=Path("results"),
    segmentation_schema = None
):
    logging.getLogger("pulse").setLevel(logging.WARNING)
    if geo_folder is None:
        geo_folder = outdir / 'lv'
    fe_model = HeartModelPulse(
        geo_params=geo_params, geo_folder=geo_folder, bc_params=bc_params, segmentation_schema=segmentation_schema
    )
    collector = DataCollector(outdir=outdir, problem=fe_model)
    delayed_activations = compute_delayed_activations(
        fe_model.geometry.cfun, num_time_step=num_time_step, std=delay, mode=delay_mode
    )
    circ_model = CirculationModel(params=circ_params)
    # saving initial values
    collector.collect(
        time=0,
        pressure=0,
        volume=fe_model.compute_volume(activation_value=0, pressure_value=0),
        activation=0.0,
        flow=circ_model.flow,
        p_ao=circ_model.aortic_pressure,
    )
    # Increase to atrial pressure
    volume = fe_model.initial_loading(atrium_pressure=atrium_pressure)
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
    )

    return collector, fe_model, circ_model, delayed_activations


# %%


def plot_data_aha(result_data, num_time_step=1000, plots_path=Path("results"),ylabel_text = '', ylim = None):
    plots_path.mkdir(parents=True, exist_ok=True)

    total_time = len(result_data)
    num_aha_segments = len(result_data[0])
    for n in range(num_aha_segments):
        data = [result_data[t][n] for t in range(total_time)]
        data_array = np.array(data)
        file_path = plots_path / f"strains_aha_{n + 1}.png"

        plt.figure()
        plt.plot(
            np.linspace(0, len(data) * 1000 / num_time_step, len(data)),
            data_array,
            "k-",
            linewidth=0.1,
        )
        plt.plot(
            np.linspace(0, len(data) * 1000 / num_time_step, len(data)),
            np.average(data_array, axis=1),
            "r-",
            linewidth=1,
        )
        plt.xlabel("Time [ms]")
        plt.ylabel(ylabel_text)
        if ylim is not None:
            plt.ylim((-ylim, ylim))
        plt.savefig(file_path)
        plt.close()


# %%

geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 5,
    "r_long_epi": 5.75,
    "mesh_size": 2.5,
}
circ_params = {
    "aortic_resistance": 10,
    "systematic_resistance": 10,
    "systematic_compliance": 10,
    "aortic_pressure": 10,
    "diastolic_pressure": 10,
    "initial_pressure": 0.0,
}

bc_params = {"pericardium_spring": 0.0001}

outdir = Path("00_results/test_no_aha/")

segmentation_schema = {
    "num_circ_segments": 6,
    "num_long_segments": 4,
}

collector, fe_model, circ_model, delayed_activations = main(
    num_time_step=500,
    t_end=260,
    delay=0.01,
    geo_params=geo_params,
    bc_params=bc_params,
    circ_params=circ_params,
    outdir=outdir,
    segmentation_schema=segmentation_schema
)
plot_data_aha(fe_model.E_ff, num_time_step=500, plots_path=outdir / 'strains', ylim=0.35, ylabel_text="Green-Lagrange Fiber Strain (-)")
plot_data_aha(fe_model.myocardial_work, num_time_step=500, plots_path=outdir / 'work', ylabel_text="Myocardial Work ()")
# %%
# data = collector.read_csv()

# data_sampled = data_sampleing(data, 50)
# data_plotting(data_sampled, "ko")

# %%
# fe_model_highres = HeartModelPulse(
#     geo=fe_model.geometry, bc_params=bc_params, geo_refinement=1
# )

# # %%
# outdir_forward = Path("Test/2/Forward_sampled")
# outname = Path(outdir_forward) / "results.xdmf"
# if outname.is_file():
#     outname.unlink()
#     outname.with_suffix(".h5").unlink()
# collector_highres = DataCollector(outdir=outdir_forward, problem=fe_model)

# forward_solver(
#     fe_model_highres,
#     data_sampled["lv_pressure"],
#     data_sampled["time"],
#     0.01,
#     collector_highres,
# )
# # %%
# outdir_forward = Path("00_results/HighRes_mesh_refined/Forward_no_sampling")
# outname = Path(outdir_forward) / "results.xdmf"
# if outname.is_file():
#     outname.unlink()
#     outname.with_suffix(".h5").unlink()
# collector_highres = DataCollector(outdir=outdir_forward, problem=fe_model)

# forward_solver(
#     fe_model_highres,
#     data["lv_pressure"],
#     data["time"],
#     0.01,
#     collector_highres,
# )
# %%
