from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

import dolfin
from geometry import (
    load_geo_with_cfun,
    get_cfun_for_altered_compartment,
    get_cfun_for_adjacent_compartment,
)
from utils import generate_symmetric_jet_colors, plot_ring_with_white_center


# %%
def load_mesh(fname: Path):
    # Read the mesh
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        mesh = dolfin.Mesh()
        xdmf.read(mesh)
    return mesh


def load_u(fname: Path, t: float, mesh: dolfin.mesh):
    V = dolfin.VectorFunctionSpace(mesh, "CG", 2)
    u = dolfin.Function(V)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(u, "Displacement", t)
    return u


def load_E(fname: Path, t: float, mesh: dolfin.mesh):
    tensor_element = dolfin.TensorElement("DG", mesh.ufl_cell(), 0)
    function_space = dolfin.FunctionSpace(mesh, tensor_element)
    E = dolfin.Function(function_space)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(E, "Green Lagrange Strain", t)
    return E


def compute_fiber_strain(E: dolfin.Function, fib0: dolfin.Function, mesh: dolfin.mesh):
    V = dolfin.FunctionSpace(mesh, "DG", 0)
    Eff = dolfin.project(dolfin.inner(E * fib0, fib0), V)
    return Eff


# %%
def plot_strain_result(
    x,
    ax=None,
    data_label="value",
    ylabel="y",
    color="blue",
    style="-",
    ylim=None,
    t_end=1,
    alpha=0.3,
):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))

    averages = x.mean(axis=1)
    std_dev = x.std(axis=1)
    upper_bound = averages + std_dev
    lower_bound = averages - std_dev

    T_tot = x.shape[0]
    x_values = np.linspace(0, t_end, T_tot)

    ax.plot(x_values, averages, label=data_label, color=color, linestyle=style)
    ax.fill_between(x_values, lower_bound, upper_bound, color=color, alpha=alpha)
    ax.set_xlabel("Normalized time (-)")
    ax.set_ylabel(ylabel)

    if ylim is not None:
        ax.set_ylim(ylim)
    ax.set_xlim([0, 1])
    ax.grid(True)
    if ax is None:
        plt.show()
    return ax


# %%
def main(outdir, num_time_step, segmentation_schema):
    geo_folder = Path(outdir) / "lv"
    geo = load_geo_with_cfun(geo_folder)

    E_fname = outdir / "Green Lagrange Strain.xdmf"
    Eff_value = np.zeros((num_time_step, geo.mesh.num_cells()))
    Eff_value = []
    for t in range(num_time_step):
        try:
            E_t = load_E(E_fname, t, geo.mesh)
            Eff_t = compute_fiber_strain(E_t, geo.f0, geo.mesh)
            Eff_value.append(Eff_t.vector()[:])
        except:
            break

    t_tot = len(Eff_value)
    Eff_value_arr = np.array(Eff_value)

    altered_compartment_cfun = get_cfun_for_altered_compartment(segmentation_schema)
    compartments_indices = get_cfun_for_adjacent_compartment(
        altered_compartment_cfun, segmentation_schema, geo
    )

    num_compartments = segmentation_schema["num_circ_segments"]
    colors = generate_symmetric_jet_colors(num_compartments)
    style = "-"
    plots_folder = Path(outdir) / "plots"
    plots_folder.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 6))
    ylim = [np.min(Eff_value_arr), np.max(Eff_value_arr)]
    for i, indices in enumerate(compartments_indices):
        Eff_compartment = Eff_value_arr[:, indices]
        if i > int(num_compartments / 2):
            style = "--"
        plot_strain_result(
            Eff_compartment,
            ax,
            data_label="Compartment no. " + str(i),
            ylabel="Strain (-)",
            color=colors[i],
            style=style,
            ylim=ylim,
            t_end=t_tot / num_time_step,
            alpha=0,
        )

        fig2, ax2 = plt.subplots(figsize=(8, 6))
        plot_strain_result(
            Eff_compartment,
            ax2,
            data_label="Compartment no. " + str(i),
            ylabel="Strain (-)",
            color=colors[i],
            style=style,
            ylim=ylim,
            t_end=t_tot / num_time_step,
        )
        ax2.legend()
        fname = plots_folder / f"Green-Lagrange Strain {i}"
        fig2.savefig(fname=fname)
        fig2.clear()
    ax.legend()
    fname = plots_folder / "Green-Lagrange Strains"
    fig.savefig(fname=fname)
    fig.clear()


# %%
segmentation_schema = {
    "num_circ_segments": 18,
    "num_long_segments": 6,
}
num_time_step = 500

# %%
delay = 0
delay_mode = "delay"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema)

# %%
delay = 0.05
delay_mode = "delay"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema)
# %%
delay = 0.05
delay_mode = "diastole_time"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema)
# %%
delay = 1
delay_mode = "decay"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema)
# %%
delay = 0.05
delay_mode = "systole_time"
outdir = Path("00_results/Level I/") / f"{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema)
# %%
# Saving a ring for presentation purposes
fig, ax = plt.subplots(figsize=(5, 5))
plot_ring_with_white_center(
    segmentation_schema["num_circ_segments"], ax=ax, section_num_flag=True
)
outdir = Path("00_results/Level I/")
fname = Path(outdir) / "Segments.png"
fig.savefig(fname=fname)
# %%
