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

def recreate_cfun(geo, segmentation_schema, folder):
    geo_params = {
        "r_short_endo": 3,
        "r_short_epi": 3.75,
        "r_long_endo": 4.25,
        "r_long_epi": 5,
        "mesh_size": 1,
        'fiber_angle_endo': -60,
        'fiber_angle_epi': 60,
    }
    mu_base_endo = -np.arccos(
    geo_params["r_short_epi"] / geo_params["r_long_endo"] / 2
    )   
    geo = segmentation(
        geo,
        geo_params["r_long_endo"],
        geo_params["r_short_endo"],
        mu_base_endo,
        segmentation_schema["num_circ_segments"],
        segmentation_schema["num_long_segments"],
    )
    with XDMFFile((folder / "cfun.xdmf").as_posix()) as xdmf:
        xdmf.write(geo.cfun)
    return geo

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

def compute_active_passive_stress_from_file(displacement_fname, u, heart_model):
    F = dolfin.variable(pulse.kinematics.DeformationGradient(u))
    Cauchy = heart_model.problem.material.CauchyStress(F)
    W_a = heart_model.material.Wactive(F)
    P1_active = dolfin.diff(W_a, F)
    Cauchy_active = pulse.kinematics.InversePiolaTransform(P1_active, F)
    Cauchy_passive = Cauchy - Cauchy_active
    return Cauchy_active, Cauchy_passive

def compute_active_passive_stress_values_from_file(displacement_fname, heart_model, num_time_step: int = 1000):
    Cauchy_active_ff_value = []
    Cauchy_passive_ff_value = []
    V = dolfin.FunctionSpace(heart_model.geometry.mesh, "DG", 0)
    fib0 = heart_model.geometry.f0
    for t in range(num_time_step):
        try:
            u = load_displacement_function_from_file(displacement_fname, t, heart_model.geometry.mesh)
            Cauchy_active, Cauchy_passive = compute_active_passive_stress_from_file(displacement_fname, u, heart_model)
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

    geo_folder = Path(data_folder) / "lv"
    geo = geometry.load_geo_with_cfun(geo_folder)
    geo = recreate_cfun(geo, segmentation_schema, outdir)
    heart_model = load_heart_model(geo)
    
    displacement_fname = Path(data_folder) / "displacement.xdmf"
    stress_active_value, stress_passive_value = compute_active_passive_stress_values_from_file(displacement_fname, heart_model, num_time_step = num_time_step)
    stress_active_compartment = compute_value_compartment(stress_active_value, geo.cfun)
    stress_passive_compartment = compute_value_compartment(stress_passive_value, geo.cfun)
    stress_active_midslice = extract_midslice_compartment_data(stress_active_compartment, segmentation_schema)
    stress_passive_midslice = extract_midslice_compartment_data(stress_passive_compartment, segmentation_schema)
    
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

    E_fname = data_folder / "Green Lagrange Strain.xdmf"
    Eff_value = compute_fiber_strain_values_from_file(
        E_fname, geo.mesh, geo.f0, num_time_step=num_time_step
    )
    Eff_comp = compute_value_compartment(Eff_value, geo.cfun)
    Eff_comp_midslice = extract_midslice_compartment_data(Eff_comp, segmentation_schema)

    Eff_comp_ave, Eff_comp_std = compute_average_std_compartment_value(Eff_comp)
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

    export_results(outdir, Eff_comp_ave, Eff_comp_std, num_time_step)

if __name__ == "__main__":
    main()
