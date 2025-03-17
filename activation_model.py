import math
from typing import Dict
from typing import Optional
from typing import Tuple
from pathlib import Path
from structlog import get_logger
import matplotlib.pyplot as plt

import scipy.stats as stats
from tqdm import tqdm
import numpy as np
import scipy.integrate
from scipy.interpolate import interp1d
import dolfin

import geometry

logger = get_logger()


def default_parameters() -> Dict[str, float]:
    r"""Default parameters for the activation model

    Returns
    -------
    Dict[str, float]
        Default parameters

    Notes
    -----
    The default parameters are

    .. math::
        t_{\mathrm{sys}} &= 0.16 \\
        t_{\mathrm{dias}} &= 0.484 \\
        \gamma &= 0.005 \\
        a_{\mathrm{max}} &= 5.0 \\
        a_{\mathrm{min}} &= -30.0 \\
        \sigma_0 &= 150e3 \\
    """
    return dict(
        t_sys=0.16,
        t_dias=0.484,
        gamma=0.005,
        a_max=7,       # Faster rate to reduce IVC duration
        a_min=-11,       # Slower relaxation to increase IVR duraion
        sigma_0=250e3,
    )


def activation_function(
    t_span: Tuple[float, float],
    t_eval: Optional[np.ndarray] = None,
    parameters: Optional[Dict[str, float]] = None,
) -> np.ndarray:
    r"""Active stress model from the Bestel model [3]_.

    Parameters
    ----------
    t_span : Tuple[float, float]
        A tuple representing start and end of time
    parameters : Dict[str, float]
        Parameters used in the model, see :func:`default_parameters`
    t_eval : Optional[np.ndarray], optional
        Time points to evaluate the solution, by default None.
        If not provided, the default points from `scipy.integrate.solve_ivp`
        will be used

    Returns
    -------
    np.ndarray
        An array of activation points

    Notes
    -----
    The active stress is taken from Bestel et al. [3]_, characterized through
    a time-dependent stress function \tau solution to the evolution equation

    .. math::
        \dot{\tau}(t) = -|a(t)|\tau(t) + \sigma_0|a(t)|_+

    being a(\cdot) the activation function and \sigma_0 contractility,
    where each remaining term is described below:

    .. math::
        |a(t)|_+ =& \mathrm{max}\{a(t), 0\} \\
        a(t) :=& \alpha_{\mathrm{max}} \cdot f(t)
        + \alpha_{\mathrm{min}} \cdot (1 - f(t)) \\
        f(t) =& S^+(t - t_{\mathrm{sys}}) \cdot S^-(t - t_{\mathrm{dias}}) \\
        S^{\pm}(\Delta t) =& \frac{1}{2}(1 \pm \mathrm{tanh}(\frac{\Delta t}{\gamma}))

    .. [3] J. Bestel, F. Clement, and M. Sorine. "A Biomechanical Model of Muscle Contraction.
        In: Medical Image Computing and Computer-Assisted Intervention - MICCAI 2001. Springer
        Berlin Heidelberg, 2001, pp. 1159{1161.

    """
    params = default_parameters()
    if parameters is not None:
        params.update(parameters)

    # print(f"Solving active stress model with parameters: {pprint.pformat(params)}")

    f = (
        lambda t: 0.25
        * (1 + math.tanh((t - params["t_sys"]) / params["gamma"]))
        * (1 - math.tanh((t - params["t_dias"]) / params["gamma"]))
    )
    a = lambda t: params["a_max"] * f(t) + params["a_min"] * (1 - f(t))

    def rhs(t, tau):
        return -abs(a(t)) * tau + params["sigma_0"] * max(a(t), 0)

    res = scipy.integrate.solve_ivp(
        rhs,
        t_span,
        [0.0],
        t_eval=t_eval,
        method="Radau",
    )
    return res.y.squeeze()




def create_activation_function(
    outdir,
    geo,
    segmentation_schema,
    scenario,
    activation_mode,
    activation_variation,
    num_time_step,
    random_flag=True,
):
    try:
        delayed_cfun = geometry.get_cfun_for_altered_compartment(segmentation_schema)
        delayed_activations = compute_delayed_activation(
            scenario,
            geo.cfun,
            delayed_cfun,
            num_time_step=num_time_step,
            std=activation_variation,
            mode=activation_mode,
            random_flag=random_flag,
        )
        fname = outdir / "activation.xdmf"
        save_activation_as_dolfin_function(geo, delayed_activations, fname)
        return fname
    except Exception as e:
        logger.error(f"Failed to create activation function: {e}")
        raise


def compute_delayed_activation(
    scenario,
    cfun,
    delayed_cfun,
    std=0.01,
    random_flag=True,
    t_span=(0.0, 1.0),
    num_time_step=100,
    t_interp=None,
    mode="delay",
):
    # Define a dictionary to map modes to corresponding functions
    scenario_function_map = {
        "single_compartment": compute_delayed_activations_single_compartment,
        "homogenous_compartment": compute_delayed_activations_compartments,
        "heterogenous_compartment": compute_delayed_activations_compartments,
    }

    # Check if the mode is valid and call the corresponding function
    if scenario in scenario_function_map:
        if scenario == "heterogenous_compartment":
            std_compartment = 0.01
        else:
            std_compartment = 0
        return scenario_function_map[scenario](
            cfun,
            delayed_cfun,
            std=std,
            std_compartment=std_compartment,
            random_flag=random_flag,
            t_span=t_span,
            num_time_step=num_time_step,
            t_interp=t_interp,
            mode=mode,
        )
    else:
        raise ValueError(
            f"Invalid mode: {scenario}. Choose from {list(scenario_function_map.keys())}"
        )


def compute_delayed_activations_single_compartment(
    cfun,
    delayed_cfun,
    std=0.01,
    std_compartment=0,
    random_flag=True,
    t_span=(0.0, 1.0),
    num_time_step=100,
    t_interp=None,
    mode="delay",
):
    t_eval = np.linspace(*t_span, num_time_step)
    # normal_activation_params = default_parameters()
    delayed_activations = []
    cfun_num = len(set(cfun.array()))
    segments_num = np.linspace(1, cfun_num, cfun_num)
    for n in tqdm(segments_num, desc="Creating Delayed Activation Curves", ncols=100):
        elems = geometry.get_elems(cfun, n)
        num_elems = len(elems)
        offsets = np.zeros(num_elems)
        if n == delayed_cfun:
            if std == 0:
                logger.warning(
                    "In single compartment the std should be larger than 0.0"
                )
            else:
                offsets += std
        if t_interp is None:
            segment_delayed_activations = np.zeros((len(t_eval), num_elems))
        else:
            segment_delayed_activations = np.zeros((len(t_interp), num_elems))
        for i, offset in enumerate(offsets):
            segment_delayed_activation = compute_segment_delayed_activation(
                mode, offset, t_span, t_eval
            )
            if t_interp is None:
                segment_delayed_activations[:, i] = segment_delayed_activation
            else:
                interp = interp1d(t_eval, segment_delayed_activation)
                segment_delayed_activation_interp = interp(t_interp)
                segment_delayed_activations[:, i] = segment_delayed_activation_interp

        delayed_activations.append(segment_delayed_activations)
    return delayed_activations


def compute_delayed_activations_compartments(
    cfun,
    delayed_cfun,
    std=0.01,
    std_compartment=0,
    random_flag=True,
    t_span=(0.0, 1.0),
    num_time_step=100,
    t_interp=None,
    mode="delay",
):
    t_eval = np.linspace(*t_span, num_time_step)
    delayed_activations = []
    cfun_num = len(set(cfun.array()))
    segments_num = np.linspace(1, cfun_num, cfun_num)
    if std == 0:
        offsets = np.zeros(cfun_num)
    else:
        offsets = stats.norm.ppf(np.linspace(0.01, 0.99, cfun_num), loc=0, scale=std)

    for n in tqdm(segments_num, desc="Creating Delayed Activation Curves", ncols=100):
        elems = geometry.get_elems(cfun, n)
        num_elems = len(elems)
        if random_flag:
            if len(offsets) == 1:
                offset = offsets[0]
            else:
                offset_index = np.random.randint(0, len(offsets) - 1)
                offset = offsets[offset_index]
                offsets = np.delete(offsets, offset_index)
        else:
            offset = offsets[int(n - 1)]

        if std_compartment == 0:
            offsets_compartment = np.repeat(offset, num_elems)
        else:
            offsets_compartment = stats.norm.ppf(
                np.linspace(0.01, 0.99, num_elems), loc=offset, scale=std_compartment
            )

        if t_interp is None:
            segment_delayed_activations = np.zeros((len(t_eval), num_elems))
        else:
            segment_delayed_activations = np.zeros((len(t_interp), num_elems))
        for i, offset_compartment in enumerate(offsets_compartment):
            segment_delayed_activation = compute_segment_delayed_activation(
                mode, offset_compartment, t_span, t_eval
            )
            if t_interp is None:
                segment_delayed_activations[:, i] = segment_delayed_activation
            else:
                interp = interp1d(t_eval, segment_delayed_activation)
                segment_delayed_activation_interp = interp(t_interp)
                segment_delayed_activations[:, i] = segment_delayed_activation_interp
        delayed_activations.append(segment_delayed_activations)
    return delayed_activations


def compute_delayed_activations(
    cfun, std=0.01, t_span=(0.0, 1.0), num_time_step=100, t_interp=None, mode="delay"
):
    t_eval = np.linspace(*t_span, num_time_step)
    # normal_activation_params = default_parameters()
    delayed_activations = []
    cfun_num = len(set(cfun.array()))
    segments_num = np.linspace(1, cfun_num, cfun_num)
    for n in tqdm(segments_num, desc="Creating Delayed Activation Curves", ncols=100):
        elems = geometry.get_elems(cfun, n)
        num_elems = len(elems)
        if std == 0:
            offsets = np.zeros(num_elems)
        else:
            offsets = stats.norm.ppf(
                np.linspace(0.01, 0.99, num_elems), loc=0, scale=std
            )
        if t_interp is None:
            segment_delayed_activations = np.zeros((len(t_eval), num_elems))
        else:
            segment_delayed_activations = np.zeros((len(t_interp), num_elems))
        for i, offset in enumerate(offsets):
            segment_delayed_activation = compute_segment_delayed_activation(
                mode, offset, t_span, t_eval
            )
            if t_interp is None:
                segment_delayed_activations[:, i] = segment_delayed_activation
            else:
                interp = interp1d(t_eval, segment_delayed_activation)
                segment_delayed_activation_interp = interp(t_interp)
                segment_delayed_activations[:, i] = segment_delayed_activation_interp

        delayed_activations.append(segment_delayed_activations)
    return delayed_activations


def compute_segment_delayed_activation(mode, offset, t_span, t_eval):
    # Define a dictionary to map modes to corresponding functions
    mode_function_map = {
        "delay": process_delay,
        "activation": process_activation,
        "decay": process_decay,
        "diastole_time": process_diastole_time,
        "systole_time": process_systole_time,
    }

    # Check if the mode is valid and call the corresponding function
    if mode in mode_function_map:
        return mode_function_map[mode](offset, t_span, t_eval)
    else:
        raise ValueError(
            f"Invalid mode: {mode}. Choose from {list(mode_function_map.keys())}"
        )


def process_delay(offset, t_span, t_eval):
    normal_activation_params = default_parameters()
    segment_delayed_activation_params = normal_activation_params.copy()
    segment_delayed_activation_params["t_sys"] += offset
    segment_delayed_activation_params["t_dias"] += offset
    segment_delayed_activation = (
        activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=segment_delayed_activation_params,
        )
        / 1000.0
    )
    return segment_delayed_activation


def process_activation(offset, t_span, t_eval):
    segment_delayed_activation_params = default_parameters()
    segment_delayed_activation_params["a_max"] += (
        segment_delayed_activation_params["a_max"] * offset
    )
    segment_delayed_activation = (
        activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=segment_delayed_activation_params,
        )
        / 1000.0
    )
    return segment_delayed_activation


def process_decay(offset, t_span, t_eval):
    segment_delayed_activation_params = default_parameters()
    segment_delayed_activation_params["a_min"] += (
        segment_delayed_activation_params["a_min"] * offset
    )
    segment_delayed_activation = (
        activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=segment_delayed_activation_params,
        )
        / 1000.0
    )
    return segment_delayed_activation


def process_diastole_time(offset, t_span, t_eval):
    segment_delayed_activation_params = default_parameters()
    segment_delayed_activation_params["t_dias"] += offset
    segment_delayed_activation = (
        activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=segment_delayed_activation_params,
        )
        / 1000.0
    )
    # we normalize sigma_0 based on max value so that the peak force is the same.
    a_max = np.max(segment_delayed_activation)
    segment_delayed_activation_params["sigma_0"] *= 200 / a_max
    segment_delayed_activation = (
        activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=segment_delayed_activation_params,
        )
        / 1000.0
    )
    return segment_delayed_activation


def process_systole_time(offset, t_span, t_eval):
    segment_delayed_activation_params = default_parameters()
    segment_delayed_activation_params["t_sys"] += offset
    segment_delayed_activation = (
        activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=segment_delayed_activation_params,
        )
        / 1000.0
    )
    # we normalize sigma_0 based on max value so that the peak force is the same.
    a_max = np.max(segment_delayed_activation)
    segment_delayed_activation_params["sigma_0"] *= 200 / a_max
    segment_delayed_activation = (
        activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=segment_delayed_activation_params,
        )
        / 1000.0
    )
    return segment_delayed_activation


def save_activation_as_dolfin_function(geo, delayed_activations, fname):
    V = dolfin.FunctionSpace(geo.mesh, "DG", 0)
    delayed_activations_function = dolfin.Function(V)
    segments = geo.cfun
    if fname.exists():
        fname.unlink()

    for t in range(len(delayed_activations[0])):
        num_segments = len(set(segments.array()))
        for n in range(num_segments):
            delayed_activations_function.vector()[geometry.get_elems(segments, n + 1)] = (
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


def plot_activation_single_compartment(
    mode, offset, num_time_step, t_span=(0, 1), outdir=None
):
    t_eval = np.linspace(*t_span, num_time_step)
    segment_normal_activation = compute_segment_delayed_activation(
        mode, 0, t_span, t_eval
    )
    segment_delayed_activation = compute_segment_delayed_activation(
        mode, offset, t_span, t_eval
    )
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(
        t_eval,
        segment_normal_activation,
        label="Normal Segements Activation",
        color="k",
    )
    ax.plot(
        t_eval,
        segment_delayed_activation,
        label="Delayed Segements Activation",
        color="r",
    )
    ax.legend()
    plt.xlabel("Normalized Time [-]")
    plt.ylabel("Myocard. Force Generation per Unit area (kPa)")
    if outdir is None:
        plt.show()
    else:
        outdir = Path(outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        fname = outdir / "activation_plot.png"
        fig.savefig(fname=fname)


def load_activation_function_from_file(
    activation_fname: Path, t: float, mesh: dolfin.mesh
):
    activation_fname = Path(activation_fname)
    element = dolfin.FiniteElement("DG", mesh.ufl_cell(), 0)
    function_space = dolfin.FunctionSpace(mesh, element)
    activation_function = dolfin.Function(function_space)
    activation_function.vector()[:] = 0
    with dolfin.XDMFFile(activation_fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(activation_function, "activation", t)
    return activation_function


def load_activation_values_from_file(
    activation_fname: Path, mesh: dolfin.mesh, num_time_step: int = 1000
):
    a_value = []
    for t in range(num_time_step):
        try:
            activation_function = load_activation_function_from_file(
                activation_fname, t, mesh
            )
            a_value.append(activation_function.vector()[:])
        except:
            break
    return a_value


def load_activation_compartment_from_file(
    geo_folder, activation_fname, num_time_step: int = 1000
):
    geo_folder = Path(geo_folder)
    activation_fname = Path(activation_fname)
    geo = geometry.load_geo_with_cfun(geo_folder)
    activation_values = load_activation_values_from_file(
        activation_fname, geo.mesh, num_time_step
    )
    activation_values_array = np.array(activation_values)
    cfuns = set(geo.cfun.array())
    activation_compartments = []
    for cfun in cfuns:
        num_elem = geometry.get_elems(geo.cfun, cfun)
        activation_compartments.append(activation_values_array[:, num_elem])

    return activation_compartments


def plot_average_activation_compartments(
    outdir: str, geo_folder: str, activation_fname: str, num_time_step: int = 1000
):
    outdir = Path(outdir)
    activation_compartments = load_activation_compartment_from_file(
        geo_folder, activation_fname, num_time_step
    )
    t_end = activation_compartments[0].shape[0]
    t_values = np.linspace(0, t_end / num_time_step, t_end)
    fig, ax = plt.subplots(figsize=(8, 6))
    for activation in activation_compartments:
        activation_average = np.average(activation, axis=1)
        ax.plot(t_values, activation_average, "k", linewidth=0.03)
        ax.set_xlabel("Normalized time (-)")
        ax.set_ylabel("Activation Parameter (kPa)")
        ax.set_xlim([0, 1])
    fname = outdir / "activations"
    fig.savefig(fname=fname)
    plt.close(fig)


def plot_activation_within_compartment(
    outdir: str,
    geo_folder: str,
    activation_fname: str,
    compartment_num: int = 0,
    num_time_step: int = 1000,
):
    outdir = Path(outdir)
    activation_compartments = load_activation_compartment_from_file(
        geo_folder, activation_fname, num_time_step
    )
    t_end = activation_compartments[0].shape[0]
    t_values = np.linspace(0, t_end / num_time_step, t_end)
    fig, ax = plt.subplots(figsize=(8, 6))
    num_elem = activation_compartments[compartment_num].shape[1]
    for n in range(num_elem):
        activation = activation_compartments[compartment_num][:,n]
        ax.plot(t_values, activation, "k", linewidth=0.03)
        ax.set_xlabel("Normalized time (-)")
        ax.set_ylabel("Activation Parameter (kPa)")
        ax.set_xlim([0, 1])
    fname = outdir / f"Activation_compartment_{compartment_num}"
    fig.savefig(fname=fname)
    plt.close(fig)

def load_action_potential_function_from_file(
    membrane_potential_fname: Path, t: float, mesh: dolfin.mesh
):
    membrane_potential_fname = Path(membrane_potential_fname)
    element = dolfin.FiniteElement("DG", mesh.ufl_cell(), 0)
    function_space = dolfin.FunctionSpace(mesh, element)
    membrane_potential_function = dolfin.Function(function_space)
    membrane_potential_function.vector()[:] = 0
    with dolfin.XDMFFile(membrane_potential_fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(membrane_potential_function, "MP", t)
    return membrane_potential_function


def load_membrane_potential_values_from_file(
    membrane_potential_fname: Path, mesh: dolfin.mesh, num_time_step: int = 1000
):
    MP_value = []
    for t in range(num_time_step):
        try:
            membrane_potential_function = load_action_potential_function_from_file(
                membrane_potential_fname, t, mesh
            )
            MP_value.append(membrane_potential_function.vector()[:])
        except:
            break
    return MP_value


def load_membrane_potential_compartment_from_file(
    geo_folder, membrane_potential_fname, num_time_step: int = 1000
):
    geo_folder = Path(geo_folder)
    membrane_potential_fname = Path(membrane_potential_fname)
    geo = geometry.load_geo_with_cfun(geo_folder)
    membrane_potential_values = load_membrane_potential_values_from_file(
        membrane_potential_fname, geo.mesh, num_time_step
    )
    membrane_potential_array = np.array(membrane_potential_values)
    cfuns = set(geo.cfun.array())
    membrane_potential_compartments = []
    for cfun in cfuns:
        num_elem = geometry.get_elems(geo.cfun, cfun)
        membrane_potential_compartments.append(membrane_potential_array[:, num_elem])

    return membrane_potential_compartments

def cmpute_ep_activation(
    outdir,
    geo,
    segmentation_schema,
    scenario,
    activation_mode,
    activation_variation,
    num_time_step,
    randomized_flag,
    comp_randomized_flag,
    comp_randomized_std
):
    activations = []
    t_eval = np.linspace(0, 1, num_time_step)
    geo_folder = outdir / "lv_coarse"
    ep_folder = outdir / "EP"
    membrane_potential_fname = ep_folder / "membrane_potential_coarse.xdmf"
    membrane_potential_compartments = load_membrane_potential_compartment_from_file(geo_folder, membrane_potential_fname, num_time_step=num_time_step)
    comp_num = len(membrane_potential_compartments)
    offsets = stats.norm.ppf(np.linspace(0.01, 0.99, comp_num), loc=0.10, scale=comp_randomized_std) #100 ms +- comp_randomized_std second std
    #plt.hist(offsets*1000, label='STD 50 ms')
    #plt.savefig('Comparment Delay Dist.png')   
    #breakpoint()
    for n, MPs in tqdm(enumerate(membrane_potential_compartments), total=len(membrane_potential_compartments), desc="Creating Activation Curves for Compartments", ncols=100): 
        elems = geometry.get_elems(geo.cfun, n+1)
        num_elems = len(elems)
        segment_activations = np.zeros((len(t_eval), num_elems))
        
        if comp_randomized_flag:
            offset_index = np.random.randint(0, len(offsets))
            offset = offsets[offset_index]
            offsets = np.delete(offsets, offset_index)
        else:
            offset = 0.10
        
        for i, cell_MP in enumerate(MPs.T):
            t_span=(0.0, 1.0)
            ind = np.where(cell_MP>37)[0][0]
            activation_params = default_parameters()
            if activation_mode == 'decay':
                activation_params["a_min"] =  activation_variation
            if activation_mode == 'rate':
                activation_params["a_max"] = activation_variation
                activation_params["a_min"] =  -25
            
            sys_duration = activation_params["t_dias"] - activation_params["t_sys"]
            activation_params["t_sys"] = t_eval[ind]
            
            if randomized_flag:
                activation_params["a_min"] *= (np.random.random() + 0.5)         # [0.5-1.5] 50% increase or decrease
                activation_params["sigma_0"] *= (np.random.random()/2.5 + 0.8)   # [0.8-1.2] 20% increase or decrease
                activation_params["t_sys"]  *= (np.random.random() + 0.5)        # [0.5-1.5] 50% increase or decrease  
            
            activation_params["t_sys"]  += offset                            # Added compartments offset, in case of cnr = False, it adds only the fixed average value 
            
            activation_params["t_dias"] = activation_params["t_sys"] + sys_duration
            segment_activations[:, i] = (
                    activation_function(
                        t_span=t_span,
                        t_eval=t_eval,
                        parameters=activation_params,
                    )
                    / 1000.0
                )
        activations.append(segment_activations)

    return activations

class Infarct_expression(dolfin.UserExpression):
    def __init__(self, center, mi_severity, iz_radius, bz_thickness, **kwargs):
        super().__init__(**kwargs)
        self.center = center
        self.mi_severity = mi_severity
        self.iz_radius = iz_radius
        self.bz_radius = iz_radius + bz_thickness

    def eval(self, value, x):
        if self.mi_severity == 0.0:
            value[0] = 0.0
            return

        dx = x[0] - self.center[0]
        dy = x[1] - self.center[1]
        dz = x[2] - self.center[2]
        distance = np.sqrt(dx**2 + dy**2 + dz**2)

        # Apply thresholding
        if distance < self.iz_radius:
            value[0] = self.mi_severity
        elif distance > self.bz_radius:
            value[0] = 0.0
        else:
            denominator = self.iz_radius - self.bz_radius
            if denominator == 0.0:
                value[0] = 0.0
            else:
                normalized_value = (distance - self.bz_radius) / denominator
                value[0] = normalized_value * self.mi_severity

    def value_shape(self):
        return ()
    
def create_infarct(outdir, geo, mi_center, mi_severity, iz_radius, bz_thickness, save_flag = True, varname = "infarct", fname = "infarct"):
    V = dolfin.FunctionSpace(geo.mesh, "DG", 0)
    # center=(-1.47839,3.52203e-16,3.15815)
    infarct_expr = Infarct_expression(mi_center, mi_severity, iz_radius, bz_thickness)
    infarct = dolfin.interpolate(infarct_expr, V)
    if save_flag:
        with dolfin.XDMFFile((outdir / f"{fname}.xdmf").as_posix()) as xdmf:
            xdmf.write_checkpoint(
                infarct,
                varname,
                0.0,
                dolfin.XDMFFile.Encoding.HDF5,
                True,
            )
    return infarct

def create_compartment_infarct(outdir, geo, comp_list, save_flag = True, varname = "infarct", fname = "infarct"):
    V = dolfin.FunctionSpace(geo.mesh, "DG", 0)
    infarct = dolfin.Function(V)
    infarct.vector()[:] = 0
    segments = geo.cfun
    num_segments = len(set(segments.array()))
    cfuns = set(geo.cfun.array())
    for c in comp_list:
        num_elem = geometry.get_elems(geo.cfun, c)
        infarct.vector()[num_elem] = 1
    
    if save_flag:
        with dolfin.XDMFFile((outdir / f"{fname}.xdmf").as_posix()) as xdmf:
            xdmf.write_checkpoint(
                infarct,
                varname,
                0.0,
                dolfin.XDMFFile.Encoding.HDF5,
                True,
            )
    return infarct


def save_mi_activation_as_dolfin_function(geo, delayed_activations, infarct, fname):
    V = dolfin.FunctionSpace(geo.mesh, "DG", 0)
    delayed_activations_function = dolfin.Function(V)
    segments = geo.cfun
    if fname.exists():
        fname.unlink()

    for t in range(len(delayed_activations[0])):
        num_segments = len(set(segments.array()))
        for n in range(num_segments):
            delayed_activations_function.vector()[geometry.get_elems(segments, n + 1)] = (
                delayed_activations[n][t, :]
            )
        delayed_activations_function.vector()[:] *= (1-infarct.vector()[:]) 
        with dolfin.XDMFFile(fname.as_posix()) as xdmf:
            xdmf.write_checkpoint(
                delayed_activations_function,
                "activation",
                float(t + 1),
                dolfin.XDMFFile.Encoding.HDF5,
                True,
            )

def create_ep_activation_function(
    outdir,
    geo,
    segmentation_schema,
    scenario,
    activation_mode,
    activation_variation,
    num_time_step,
    mi_flag,
    mi_center,
    mi_severity,
    iz_radius,
    bz_thickness,
    micomp_flag,
    infarct_comp,
    randomized_flag,
    comp_randomized_flag,
    comp_randomized_std
    
):
    try:
        activations = cmpute_ep_activation(
            outdir,
            geo,
            segmentation_schema,
            scenario,
            activation_mode,
            activation_variation,
            num_time_step,
            randomized_flag,
            comp_randomized_flag,
            comp_randomized_std
        )
        fname = outdir / "activation.xdmf"
        if mi_flag:
            if micomp_flag:
                infarct = create_compartment_infarct(outdir, geo, infarct_comp)
            else:
                infarct = create_infarct(outdir, geo, mi_center, mi_severity, iz_radius, bz_thickness)
            save_mi_activation_as_dolfin_function(geo, activations, infarct, fname)
        else:
            save_activation_as_dolfin_function(geo, activations, fname)
            
        geo_folder = outdir / "lv_coarse"
        plot_ep_activation_within_compartment(outdir, geo_folder, fname, num_time_step=500)
        EP_activation_fname = outdir / "EP/activation_coarse.xdmf"
        plot_ep_activation_within_compartment(outdir, geo_folder, EP_activation_fname, num_time_step=500, fname_prefix="EP_Activation")
        membrane_potential_fname = outdir / "EP/membrane_potential_coarse.xdmf"
        plot_membrane_potential_within_compartment(outdir, geo_folder, membrane_potential_fname, num_time_step=500)
        return fname
    except Exception as e:
        logger.error(f"Failed to create activation function: {e}")
        raise
    
    
def plot_ep_activation_within_compartment(
    outdir: str,
    geo_folder: str,
    activation_fname: str,
    compartment_num: int = 0,
    num_time_step: int = 1000,
    fname_prefix: str = 'Activation',
):
    outdir = Path(outdir)
    activation_compartments = load_activation_compartment_from_file(
        geo_folder, activation_fname, num_time_step
    )
    t_end = activation_compartments[0].shape[0]
    t_values = np.linspace(0, t_end / num_time_step, t_end)
    fig, ax = plt.subplots(figsize=(8, 6))
    num_elem = activation_compartments[compartment_num].shape[1]
    for n in range(num_elem):
        activation = activation_compartments[compartment_num][:,n]
        ax.plot(t_values, activation, "k", linewidth=0.03)
        ax.set_xlabel("Normalized time (-)")
        ax.set_ylabel("Activation Parameter (kPa)")
        ax.set_xlim([0, 1])
    ax.grid(True)
    fname = outdir / f"{fname_prefix}_compartment_{compartment_num}"
    fig.savefig(fname=fname)
    plt.close(fig)
    
    
def plot_membrane_potential_within_compartment(
    outdir: str,
    geo_folder: str,
    membrane_potential_fname: str,
    compartment_num: int = 0,
    num_time_step: int = 1000,
):
    outdir = Path(outdir)
    membrane_potential_compartments = load_membrane_potential_compartment_from_file(
        geo_folder, membrane_potential_fname, num_time_step=num_time_step
    )
    t_end = membrane_potential_compartments[0].shape[0]
    t_values = np.linspace(0, t_end / num_time_step, t_end)
    fig, ax = plt.subplots(figsize=(8, 6))
    num_elem = membrane_potential_compartments[compartment_num].shape[1]
    for n in range(num_elem):
        activation = membrane_potential_compartments[compartment_num][:,n]
        ax.plot(t_values, activation, "k", linewidth=0.03)
        ax.set_xlabel("Normalized time (-)")
        ax.set_ylabel("Transmembrane Potential (mV)")
        ax.set_xlim([0, 1])
    ax.grid(True)
    fname = outdir / f"Membrane_Potential_compartment_{compartment_num}"
    fig.savefig(fname=fname)
    plt.close(fig)