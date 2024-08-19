# %%
from pathlib import Path

from geometry import create_ellipsoid_geometry, get_cfun_for_altered_compartment
from activation_model import (
    plot_activation_single_compartment,
    save_activation_as_dolfin_function,
    compute_delayed_activation,
)


# %%
def pre_process(
    outdir, scenario, geo_params, segmentation_schema, num_time_step, delay_mode, delay, random_flag = True
):
    geo = create_ellipsoid_geometry(
        folder=outdir / "lv",
        geo_params=geo_params,
        segmentation_schema=segmentation_schema,
    )
    delayed_cfun = get_cfun_for_altered_compartment(segmentation_schema)
    delayed_activations = compute_delayed_activation(
        sceanrio, geo.cfun, delayed_cfun, num_time_step=num_time_step, std=delay, mode=delay_mode, random_flag=random_flag
    )
    fname = outdir / "activation.xdmf"
    save_activation_as_dolfin_function(geo, delayed_activations, fname)


# %%
geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 4.25,
    "r_long_epi": 5,
    "mesh_size": 0.35,
}
segmentation_schema = {
    "num_circ_segments": 72,
    "num_long_segments": 6,
}
num_time_step = 500
results_folder = "00_results/dev_mpi/"
sceanrio = 'single_compartment'
# %%
delay = 0
delay_mode = "delay"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)
# %%
delay = 0.05
delay_mode = "delay"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

# %%
sceanrio = 'homogenous_compartment'
delay = 0.05
delay_mode = "delay"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

# %%
sceanrio = 'heterogenous_compartment'
delay = 0.05
delay_mode = "delay"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

# %%
sceanrio = 'single_compartment'

delay = 0.03
delay_mode = "diastole_time"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

delay = 1
delay_mode = "decay"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

delay = 0.03
delay_mode = "systole_time"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

# %%
sceanrio = 'homogenous_compartment'

delay = 0.03
delay_mode = "diastole_time"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

delay = 1
delay_mode = "decay"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

delay = 0.03
delay_mode = "systole_time"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

# %%
sceanrio = 'heterogenous_compartment'

delay = 0.03
delay_mode = "diastole_time"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

delay = 1
delay_mode = "decay"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

delay = 0.03
delay_mode = "systole_time"
outdir = Path(results_folder) / f"{sceanrio}/{delay_mode}_{delay}"
plot_activation_single_compartment(delay_mode, delay, num_time_step, outdir=outdir)
pre_process(outdir, sceanrio, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

