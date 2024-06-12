# %%
import numpy as np

# import logging
from pathlib import Path

# import pickle
import dolfin

from geometry import create_ellipsoid_geometry
from activation_model import compute_delayed_activations

# %%
geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 4.25,
    "r_long_epi": 5,
    "mesh_size": 2,
}

outdir = Path("00_results/dev")

segmentation_schema = {
    "num_circ_segments": 7,
    "num_long_segments": 6,
}

num_time_step = 500
delay = 0.03
delay_mode = "delay"
# %%
geo = create_ellipsoid_geometry(
    folder=outdir / "lv", geo_params=geo_params, segmentation_schema=segmentation_schema
)

# %%
delayed_activations = compute_delayed_activations(
    geo.cfun, num_time_step=num_time_step, std=delay, mode=delay_mode
)

fname = outdir / "activation.xdmf"
V = dolfin.FunctionSpace(geo.mesh, "DG", 0)
delayed_activations_function = dolfin.Function(V)
segments = geo.cfun


def get_elems(cfun, cfun_num):
    indices = np.where(cfun.array() == cfun_num)[0]
    return indices


for t in range(len(delayed_activations[0])):
    num_segments = len(set(segments.array()))
    for n in range(num_segments):
        delayed_activations_function.vector()[get_elems(segments, n + 1)] = (
            delayed_activations[n][t, :]
        )
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.write_checkpoint(
            delayed_activations_function,
            "activation",
            float(t + 1),
            dolfin.XDMFFile.Encoding.HDF5,
            True,
        )

# %%
