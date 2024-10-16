from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

import dolfin
import geometry
import arg_parser
import argparse
import activation_model
import utils
from segmentation import segmentation
from dolfin import XDMFFile
from heart_model import HeartModelPulse
import pulse

# %%
def load_mesh_from_file(mesh_fname: Path):
    # Read the mesh
    mesh_fname = Path(mesh_fname)
    with dolfin.XDMFFile(mesh_fname.as_posix()) as xdmf:
        mesh = dolfin.Mesh()
        xdmf.read(mesh)
    return mesh


def load_displacement_function_from_file(
    displacement_fname: Path, t: float, mesh: dolfin.mesh
):
    displacement_fname = Path(displacement_fname)
    V = dolfin.VectorFunctionSpace(mesh, "CG", 2)
    u = dolfin.Function(V)
    with dolfin.XDMFFile(displacement_fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(u, "Displacement", t)
    return u

def load_heart_model(geo):
    bc_params = {
        "pericardium_spring": 0.0001,
        "base_spring": 0,
    }
    heart_model = HeartModelPulse(geo=geo, bc_params=bc_params)
    return heart_model

def compute_active_passive_stress(u, heart_model):
    F = dolfin.variable(pulse.kinematics.DeformationGradient(u))
    W_a = heart_model.material.Wactive(F, diff=0)
    P1_active = dolfin.diff(W_a, F)
    Cauchy_active = pulse.kinematics.InversePiolaTransform(P1_active, F)
    W_p = heart_model.passive_strain_energy(F)
    P1_passive = dolfin.diff(W_p, F)
    Cauchy_passive = pulse.kinematics.InversePiolaTransform(P1_passive, F)
    return Cauchy_active, Cauchy_passive

def compute_active_passive_stress_values_from_file(displacement_fname, activation_fname, heart_model, num_time_step: int = 1000):
    Cauchy_active_ff_value = []
    Cauchy_passive_ff_value = []
    V = dolfin.FunctionSpace(heart_model.geometry.mesh, "DG", 0)
    fib0 = heart_model.geometry.f0
    for t in range(num_time_step):
        try:
            u = load_displacement_function_from_file(displacement_fname, t, heart_model.geometry.mesh)
            activation = activation_model.load_activation_function_from_file(activation_fname, t, heart_model.geometry.mesh)
            heart_model.problem.material.activation.vector()[:] = activation.vector()[:]
            heart_model.material.activation.vector()[:] = activation.vector()[:]
            Cauchy_active, Cauchy_passive = compute_active_passive_stress(u, heart_model)
            Cauchy_active_ff = dolfin.project(dolfin.inner(Cauchy_active * fib0, fib0), V)
            Cauchy_passive_ff = dolfin.project(dolfin.inner(Cauchy_passive * fib0, fib0), V)
            Cauchy_active_ff_value.append(Cauchy_active_ff.vector()[:])
            Cauchy_passive_ff_value.append(Cauchy_passive_ff.vector()[:])
        except:
            break
    return Cauchy_active_ff_value, Cauchy_passive_ff_value
    
def compute_value_compartment(value: list, cfun: dolfin.MeshFunction):
    value_array = np.array(value)
    cfuns = set(cfun.array())
    value_compartments = []
    for c in cfuns:
        num_elem = geometry.get_elems(cfun, c)
        value_compartments.append(value_array[:, num_elem])
    return value_compartments


def load_strain_function_from_file(E_fname: Path, t: float, mesh: dolfin.mesh):
    E_fname = Path(E_fname)
    tensor_element = dolfin.TensorElement("DG", mesh.ufl_cell(), 0)
    function_space = dolfin.FunctionSpace(mesh, tensor_element)
    E = dolfin.Function(function_space)
    with dolfin.XDMFFile(E_fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(E, "Green Lagrange Strain", t)
    return E


def compute_fiber_strain(E: dolfin.Function, fib0: dolfin.Function, mesh: dolfin.mesh):
    V = dolfin.FunctionSpace(mesh, "DG", 0)
    Eff = dolfin.project(dolfin.inner(E * fib0, fib0), V)
    return Eff


def compute_fiber_strain_values_from_file(
    E_fname: Path, mesh: dolfin.mesh, fib0, num_time_step: int = 1000
):
    E_fname = Path(E_fname)
    Eff_value = []
    for t in range(num_time_step):
        try:
            E_function = load_strain_function_from_file(E_fname, t, mesh)
            Eff_t = compute_fiber_strain(E_function, fib0, mesh)
            Eff_value.append(Eff_t.vector()[:])
        except:
            break
    return Eff_value


def compute_MW_value_from_file(E_fname, displacement_fname, activation_fname, heart_model, num_time_step=1000):
    MW = []
    V = dolfin.FunctionSpace(heart_model.geometry.mesh, "DG", 0)
    for t in range(num_time_step):
        try:
            activation = activation_model.load_activation_function_from_file(activation_fname, t, heart_model.geometry.mesh)
            heart_model.problem.material.activation.vector()[:] = activation.vector()[:]
            heart_model.material.activation.vector()[:] = activation.vector()[:]
            u = load_displacement_function_from_file(displacement_fname, t, heart_model.geometry.mesh)
            F = pulse.kinematics.DeformationGradient(u)
            S = heart_model.material.SecondPiolaStress(F)
            E = load_strain_function_from_file(E_fname, t, heart_model.geometry.mesh)
            MW_t = dolfin.project(dolfin.inner(S, E), V)
            MW.append(MW_t.vector()[:])
        except:
            break
    return MW
def compute_average_std_compartment_value(values):
    num_compartments = len(values)
    num_time_steps = len(values[0])
    average_compartment_value = np.zeros((num_compartments, num_time_steps))
    std_compartment_value = np.zeros((num_compartments, num_time_steps))
    for i, value in enumerate(values):
        average_compartment_value[i, :] = np.average(value, axis=1)
        std_compartment_value[i, :] = np.std(value, axis=1)
    return average_compartment_value, std_compartment_value


def extract_midslice_compartment_data(data, segmentation_schema):
    ind_i = geometry.get_first_compartment_midslice(segmentation_schema)
    num_compartments = segmentation_schema["num_circ_segments"]
    ind_f = ind_i + num_compartments
    return data[ind_i:ind_f]

def export_results(outdir, data_ave, data_std, num_time_step):
    outdir = Path(outdir)
    num_compartments, num_time_simulation = data_ave.shape
    time_column = np.linspace(0, num_time_simulation/num_time_step, num_time_simulation)
    data_ave_with_time = np.column_stack((time_column, data_ave.T))
    data_std_with_time = np.column_stack((time_column, data_std.T))
    header = ['Normalized time'] + [f'comp.{i+1}' for i in range(num_compartments)]
    np.savetxt(outdir.as_posix()+'/data_ave.csv', data_ave_with_time, delimiter=',',header=','.join(header), fmt='%.8f')
    np.savetxt(outdir.as_posix()+'/data_std.csv', data_std_with_time, delimiter=',',header=','.join(header), fmt='%.8f')

def plot_comapartment_data(
    data,
    num_time_step,
    ylabel="Data",
    xlabel="Normalized Time [-]",
    ylim=None,
    ax=None,
    single_slice=False,
):
    num_compartment, num_time_simulation = data.shape
    t_values = np.linspace(0, num_time_simulation / num_time_step, num_time_simulation)
    if single_slice:
        colors = utils.generate_symmetric_jet_colors(num_compartment)
        linewidth = 0.5
    else:
        colors = [
            (0, 0, 0, 1) for _ in range(num_compartment)
        ]  # use black for all the compartments
        linewidth = 0.1
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    for i in range(num_compartment):
        plt.plot(t_values, data[i], color=colors[i], linewidth=linewidth)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if ylim is not None:
        ax.set_ylim(ylim)
    ax.set_xlim([0, 1])
    ax.grid(True)
    return ax


def plot_and_save_compartment_stresses(
    outdir,
    Eff_comp_midslice,
    stress_active_comp_midslice,
    stress_passive_comp_midslice,
    num_time_step=1000,
    xlabel="Normalized Time [-]",
):
    outdir = Path(outdir)
    Eff = Eff_comp_midslice[5]
    stress_active = stress_active_comp_midslice[5]
    stress_passive = stress_passive_comp_midslice[5]
    
    num_time_simulation, num_cells = Eff.shape
    t_values = np.linspace(0, num_time_simulation / num_time_step, num_time_simulation)
    
    for i in range(num_cells):
        fig, ax1 = plt.subplots()
        ax1.plot(t_values, Eff[:, i], linewidth=0.5, label='Fiber Strain', color='b')
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel('Fiber Strain (-)', color='b')
        ax1.tick_params(axis='y', labelcolor='b')

        # Create a second y-axis for the stress values
        ax2 = ax1.twinx()
        # ax2.plot(t_values, stress_active[:, i]/np.max(stress_active[:, i]), linewidth=0.5, label='Active Stress - Force (kPa)', color='k', linestyle = '-')
        # ax2.plot(t_values, stress_passive[:, i]/np.max(stress_passive[:, i]), linewidth=0.5, label='Passive Stress - Load (kPa)', color='k', linestyle = '--')
        ax2.plot(t_values, stress_active[:, i], linewidth=0.5, label='Active Stress - Force (kPa)', color='k', linestyle = '-')
        ax2.plot(t_values, stress_passive[:, i], linewidth=0.5, label='Passive Stress - Load (kPa)', color='k', linestyle = '--')
        ax2.set_ylabel('Stress (kPa)', color='k')
        ax2.tick_params(axis='y', labelcolor='k')
        # Optional: Add legends
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper left', bbox_to_anchor=(0, 0.9 ))
        ax1.set_ylim((-.3,.15))
        ax2.set_ylim((0,500))
        fname = outdir / f'Cell_{i}.png'
        plt.savefig(fname, dpi=300, bbox_inches='tight')
        plt.close(fig=fig)


def plot_and_save_compartment_MW(
    outdir,
    Eff_comp_midslice,
    MW_comp_midslice,
    num_time_step=1000,
    xlabel="Normalized Time [-]",
):
    outdir = Path(outdir)
    Eff = Eff_comp_midslice[5]
    MW = MW_comp_midslice[5]
    
    num_time_simulation, num_cells = Eff.shape
    t_values = np.linspace(0, num_time_simulation / num_time_step, num_time_simulation)
    
    for i in range(num_cells):
        fig, ax1 = plt.subplots()
        ax1.plot(t_values, Eff[:, i], linewidth=0.5, label='Fiber Strain', color='b')
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel('Fiber Strain (-)', color='b')
        ax1.tick_params(axis='y', labelcolor='b')

        # Create a second y-axis for the stress values
        ax2 = ax1.twinx()
        ax2.plot(t_values, MW[:, i]-MW[0, i], linewidth=0.5, label='Myocardial Work', color='k', linestyle = '-')
        # ax2.plot(t_values[:-1], np.diff(MW[:, i]), linewidth=0.5, label='Myocardial Power', color='k', linestyle = '--')
        ax2.set_ylabel('Myocardial Work (kJ)', color='k')
        ax2.tick_params(axis='y', labelcolor='k')
        # Optional: Add legends
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper left', bbox_to_anchor=(0, 0.9 ))
        ax1.set_ylim((-.3,.15))
        ax2.set_ylim((-50,25))
        fname = outdir / f'Cell_{i}.png'
        plt.savefig(fname, dpi=300, bbox_inches='tight')
        plt.close(fig=fig)

# %%
def main(args=None) -> int:
    # Getting the arguments
    if args is None:
        args = arg_parser.parse_arguments_post(args)

    segmentation_schema = arg_parser.create_segmentation_schema(args)
    activation_fname = args.activation_fname
    data_folder = args.data_folder
    outdir = data_folder / args.outdir
    outdir = arg_parser.prepare_output_directory(outdir)
    num_time_step = args.num_time_step

    try:
        geo_folder = Path(data_folder) / "lv"
        geo = geometry.load_geo_with_cfun(geo_folder)
    except Exception:
        geo_folder = Path(data_folder) / "lv_coarse"
        geo = geometry.load_geo_with_cfun(geo_folder)
    geo = geometry.recreate_cfun(geo, segmentation_schema, outdir)
    heart_model = load_heart_model(geo)
    
    
    activation_fname = Path(data_folder) / activation_fname
    compartment_num = geometry.get_first_compartment_midslice(segmentation_schema)
    activation_model.plot_average_activation_compartments(
        outdir, geo_folder, activation_fname, num_time_step
    )
    activation_model.plot_activation_within_compartment(
        outdir,
        geo_folder,
        activation_fname,
        num_time_step=num_time_step,
        compartment_num=compartment_num,
    )

    
    displacement_fname = Path(data_folder) / "displacement.xdmf"
    stress_active_value, stress_passive_value = compute_active_passive_stress_values_from_file(displacement_fname,activation_fname, heart_model, num_time_step = num_time_step)
    stress_active_compartment = compute_value_compartment(stress_active_value, geo.cfun)
    stress_passive_compartment = compute_value_compartment(stress_passive_value, geo.cfun)
    stress_active_comp_midslice = extract_midslice_compartment_data(stress_active_compartment, segmentation_schema)
    stress_passive_comp_midslice = extract_midslice_compartment_data(stress_passive_compartment, segmentation_schema)
    
    
    E_fname = data_folder / "Green Lagrange Strain.xdmf"
    Eff_value = compute_fiber_strain_values_from_file(
        E_fname, geo.mesh, geo.f0, num_time_step=num_time_step
    )
    Eff_comp = compute_value_compartment(Eff_value, geo.cfun)
    Eff_comp_midslice = extract_midslice_compartment_data(Eff_comp, segmentation_schema)
    Eff_comp_ave, Eff_comp_std = compute_average_std_compartment_value(Eff_comp)
    
    MW_value = compute_MW_value_from_file(E_fname, displacement_fname, activation_fname, heart_model, num_time_step=num_time_step)
    MW_comp = compute_value_compartment(MW_value, geo.cfun)
    MW_ff_comp_midslice = extract_midslice_compartment_data(MW_comp, segmentation_schema)
    
    plot_comapartment_data(
        Eff_comp_ave,
        num_time_step,
        ylabel="Green Lagrange Strain (-)",
        ylim=[-0.25, 0.25],
    )
    fname = outdir / "Green-Lagrange Strains"
    plt.savefig(fname=fname)

    Eff_comp_ave_midslice, Eff_comp_std_midslice = (
        compute_average_std_compartment_value(Eff_comp_midslice)
    )
    plot_comapartment_data(
        Eff_comp_ave_midslice,
        num_time_step,
        ylabel="Green Lagrange Strain (-)",
        single_slice=True,
        ylim=[-0.25, 0.25],
    )
    fname = outdir / "Green-Lagrange Strains Midslice"
    plt.savefig(fname=fname)
    
    outdir_stress = outdir / 'stress'
    outdir_stress.mkdir(exist_ok=True)
    plot_and_save_compartment_stresses(
        outdir_stress,
        Eff_comp_midslice,
        stress_active_comp_midslice,
        stress_passive_comp_midslice,
        num_time_step=num_time_step,
    )

    outdir_work = outdir / 'work'
    outdir_work.mkdir(exist_ok=True)
    plot_and_save_compartment_MW(
        outdir_work,
        Eff_comp_midslice,
        MW_ff_comp_midslice,
        num_time_step=num_time_step,
    )
    
    export_results(outdir, Eff_comp_ave, Eff_comp_std, num_time_step)

if __name__ == "__main__":
    main()
