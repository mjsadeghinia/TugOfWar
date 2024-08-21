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

def load_activation(fname: Path, t: float, mesh: dolfin.mesh):
    element = dolfin.FiniteElement("DG", mesh.ufl_cell(), 0)
    function_space = dolfin.FunctionSpace(mesh, element)
    activation = dolfin.Function(function_space)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(activation, "Activation", t)
    return activation

def compute_fiber_strain(E: dolfin.Function, fib0: dolfin.Function, mesh: dolfin.mesh):
    V = dolfin.FunctionSpace(mesh, "DG", 0)
    Eff = dolfin.project(dolfin.inner(E * fib0, fib0), V)
    return Eff

def find_all_compartments_indices(cfun):
    compartments_indices = []
    cfun_num = len(set(cfun.array()))
    for n in range(cfun_num):
        compartment_indices = np.where(cfun.array() == n + 1 )[0]
        compartments_indices.append(compartment_indices)
    return compartments_indices

def compute_all_strain_ave_std(compartments_indices, Eff_value_arr):
    Eff_ave = []
    Eff_std = []
    for indices in compartments_indices:
        Eff_compartment = Eff_value_arr[:, indices]
        Eff_ave.append(Eff_compartment.mean(axis=1))
        Eff_std.append(Eff_compartment.std(axis=1))
    return Eff_ave, Eff_std


def export_all_strain_ave_std(Eff_ave, Eff_std, results_folder,scenario,delay,delay_mode,num_time_step, plot_flag=False):
    stacked_array = np.column_stack(Eff_ave)
    rows = stacked_array.shape[0]
    time_columns = np.linspace(0, rows/num_time_step, rows)
    final_array = np.column_stack((time_columns, stacked_array))
    # Create the header
    num_columns = stacked_array.shape[1]
    header = ['Normalized time'] + [f'comp.{i+1}' for i in range(num_columns)]
    outdir = Path(f"{results_folder}/strain curves/")
    outdir.mkdir(parents=True, exist_ok=True)
    fname = outdir / f'{scenario}_{delay_mode}_{delay}.csv'
    np.savetxt(fname, final_array, delimiter=',',header=','.join(header), fmt='%.8f')
    
    if plot_flag:
        time = final_array[:, 0]
        fig, ax = plt.subplots(figsize=(8, 6))
        for i in range(1, num_columns + 1):
            ax.plot(time, final_array[:, i], label=f'comp.{i}', color='black', linewidth=0.1)
        ax.set_xlabel("Normalized time (-)")
        ax.set_ylabel('Strain (-)')
        ax.set_xlim([0, 1])
        fname = outdir / f'{scenario}_{delay_mode}_{delay}.png'
        ax.set_ylim([-.3, .2])
        fig.savefig(fname=fname)
        plt.close(fig)
        
    stacked_array = np.column_stack(Eff_std)
    rows = stacked_array.shape[0]
    final_array = np.column_stack((time_columns, stacked_array))
    fname = outdir / f'{scenario}_{delay_mode}_{delay}_std.csv'
    np.savetxt(fname, final_array, delimiter=',',header=','.join(header), fmt='%.8f')

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
def main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode):
    geo_folder = Path(outdir) / "lv"
    geo = load_geo_with_cfun(geo_folder)

    E_fname = outdir / "Green Lagrange Strain.xdmf"
    Eff_value = []
    for t in range(num_time_step):
        try:
            E_t = load_E(E_fname, t, geo.mesh)
            Eff_t = compute_fiber_strain(E_t, geo.f0, geo.mesh)
            Eff_value.append(Eff_t.vector()[:])
        except:
            break
        
    # a_fname = outdir / "Activation_results.xdmf"
    # a_value = []
    # for t in range(num_time_step):
    #     try:
    #         a_t = load_activation(a_fname, t, geo.mesh)
    #         a_value.append(a_t.vector()[:])
    #     except:
    #         break

    t_tot = len(Eff_value)
    Eff_value_arr = np.array(Eff_value)
    
    # Exporting all the strain curve average per compartment
    all_compartments_indices = find_all_compartments_indices(geo.cfun)
    Eff_ave,  Eff_std = compute_all_strain_ave_std(all_compartments_indices, Eff_value_arr)
    export_all_strain_ave_std(Eff_ave, Eff_std, results_folder,scenario,delay,delay_mode, num_time_step, plot_flag=True)
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
    combined_Eff_value_arr = [item for sublist in compartments_indices for item in sublist]
    ylim = [np.min(Eff_value_arr[:, combined_Eff_value_arr]), np.max(Eff_value_arr[:, combined_Eff_value_arr])]
    rounded_ylim = [np.floor(ylim[0]*100)/100, np.ceil(ylim[1]*100)/100]

    handles = []
    labels = []
    for i, indices in enumerate(compartments_indices):
        Eff_compartment = Eff_value_arr[:, indices]
        if i > int(num_compartments / 2):
            style = "--"
        ax = plot_strain_result(
            Eff_compartment,
            ax,
            data_label="Compartment no. " + str(i),
            ylabel="Strain (-)",
            color=colors[i],
            style=style,
            ylim=rounded_ylim,
            t_end=t_tot / num_time_step,
            alpha=0,
        )

        # Collect the current handle for the legend
        line = ax.get_lines()[-1]  # Get the last line added to the axis
        handles.append(line)
        labels.append("Compartment no. " + str(i))
        
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        plot_strain_result(
            Eff_compartment,
            ax2,
            data_label="Compartment no. " + str(i),
            ylabel="Strain (-)",
            color=colors[i],
            style=style,
            ylim=rounded_ylim,
            t_end=t_tot / num_time_step,
        )
        ax2.legend()
        fname = plots_folder / f"Green-Lagrange Strain {i}"
        fig2.savefig(fname=fname)
        plt.close(fig2)
    # Select every 6th plot for the legend
    selected_handles = handles[::6]
    selected_labels = labels[::6]

    # Add the legend to the main axis with the selected handles and labels
    ax.legend(selected_handles, selected_labels)
    fname = plots_folder / "Green-Lagrange Strains"
    fig.savefig(fname=fname)
    plt.close(fig)


# %%
geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 4.25,
    "r_long_epi": 5,
    "mesh_size": .5,
}
segmentation_schema = {
    "num_circ_segments": 72,
    "num_long_segments": 6,
}
num_time_step = 500
results_folder = "01_results_24_08_19/"
#%%
scenario = 'single_compartment'
delay = 0
delay_mode = "delay"
outdir = Path(results_folder) / f"{scenario}/{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode)

delay = 0.05
delay_mode = "delay"
outdir = Path(results_folder) / f"{scenario}/{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode)

delay = 0.03
delay_mode = "diastole_time"
outdir = Path(results_folder) / f"{scenario}/{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode)

scenario = 'homogenous_compartment'

delay = 0.05
delay_mode = "delay"
outdir = Path(results_folder) / f"{scenario}/{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode)

delay = 0.03
delay_mode = "diastole_time"
outdir = Path(results_folder) / f"{scenario}/{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode)

scenario = 'heterogenous_compartment'

delay = 0.05
delay_mode = "delay"
outdir = Path(results_folder) / f"{scenario}/{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode)

delay = 0.03
delay_mode = "diastole_time"
outdir = Path(results_folder) / f"{scenario}/{delay_mode}_{delay}"
main(outdir, num_time_step, segmentation_schema, results_folder, scenario, delay, delay_mode)

# %%
# Saving a ring for presentation purposes
fig, ax = plt.subplots(figsize=(5, 5))
plot_ring_with_white_center(
    segmentation_schema["num_circ_segments"], ax=ax, section_num_flag=True
)
outdir = Path(results_folder) 
fname = Path(outdir) / "Segments.png"
fig.savefig(fname=fname)
# %%
