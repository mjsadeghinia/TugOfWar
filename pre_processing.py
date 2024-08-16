# %%
from pathlib import Path

from geometry import create_ellipsoid_geometry, get_cfun_for_altered_compartment
from activation_model import (
    compute_delayed_activations,
    save_activation_as_dolfin_function,
    compute_delayed_activations_single_compartment,
)


# %%
def pre_process(
    outdir, geo_params, segmentation_schema, num_time_step, delay_mode, delay
):
    geo = create_ellipsoid_geometry(
        folder=outdir / "lv",
        geo_params=geo_params,
        segmentation_schema=segmentation_schema,
    )
    delayed_cfun = get_cfun_for_altered_compartment(segmentation_schema)
    delayed_activations = compute_delayed_activations_single_compartment(
        geo.cfun, delayed_cfun, num_time_step=num_time_step, std=delay, mode=delay_mode
    )
    fname = outdir / "activation.xdmf"
    save_activation_as_dolfin_function(geo, delayed_activations, fname)


# %%
geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 4.25,
    "r_long_epi": 5,
    "mesh_size": 1,
}
segmentation_schema = {
    "num_circ_segments": 18,
    "num_long_segments": 6,
}
num_time_step = 500
# %%
delay = 0.05
delay_mode = "delay"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
pre_process(outdir, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

# # %%
# delay = 0.05
# delay_mode = "activation"
# outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
# pre_process(outdir, geo_params, segmentation_schema, num_time_step, delay_mode, delay)

# # %%
# delay = 0.05
# delay_mode = "diastole_time"
# outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
# pre_process(outdir, geo_params, segmentation_schema, num_time_step, delay_mode, delay)
