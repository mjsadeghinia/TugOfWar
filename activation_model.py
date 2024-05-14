import math
from typing import Dict
from typing import Optional
from typing import Tuple

import scipy.stats as stats
from tqdm import tqdm
import numpy as np
import scipy.integrate
from scipy.interpolate import CubicSpline


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
        a_max=5.0,
        a_min=-30.0,
        sigma_0=300e3,
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


def get_elems(cfun, cfun_num):
    indices = np.where(cfun.array() == cfun_num)[0]
    return indices


def compute_delayed_activations(
    cfun,
    std=0.01,
    aha_segments_num=np.linspace(1, 17, 17),
    t_span=(0.0, 1.0),
    num_time_step=100,
    t_interp=None,
):
    t_eval = np.linspace(*t_span, num_time_step)
    normal_activation_params = default_parameters()
    delayed_activations = []
    for n in tqdm(
        aha_segments_num, desc="Creating Delayed Activation Curves", ncols=100
    ):
        elems = get_elems(cfun, n)
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
            if t_interp is None:
                segment_delayed_activations[:, i] = segment_delayed_activation
            else:
                interp = CubicSpline(t_eval, segment_delayed_activation)
                segment_delayed_activation_interp = interp(t_interp)
                segment_delayed_activations[:, i] = segment_delayed_activation_interp

        delayed_activations.append(segment_delayed_activations)
    return delayed_activations
