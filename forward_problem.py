from typing import Protocol
import numpy as np
from pathlib import Path

from structlog import get_logger

from circ.datacollector import DataCollector
from activation_model import compute_delayed_activations

import dolfin
import pulse

logger = get_logger()


class HeartModel(Protocol):
    def compute_volume(self, activation: float, pressure: float) -> float: ...

    def get_pressure(self) -> float: ...

    def get_volume(self) -> float: ...

    def save(self, t: float, outdir: Path) -> None: ...


def get_elems(cfun, cfun_num):
    indices = np.where(cfun.array() == cfun_num)[0]
    return indices


def forward_solver(
    heart_model: HeartModel,
    pressure: np.ndarray,
    time: np.ndarray,
    activation_delay: float,
    collector: DataCollector | None = None,
    start_time: int = 0,
):
    if collector is None:
        collector = DataCollector(outdir=Path("results"), problem=heart_model)

    delayed_activations = compute_delayed_activations(
        heart_model.geometry.cfun, std=activation_delay, t_interp=time
    )

    target_activation = dolfin.Function(heart_model.activation.ufl_function_space())
    aha = heart_model.geometry.cfun

    for i, t in enumerate(time):
        v_old = heart_model.get_volume()
        for n in range(17):
            target_activation.vector()[get_elems(aha, n + 1)] = delayed_activations[n][i, :]
        a_current_0 = target_activation.vector()[0]
        pulse.iterate.iterate(
            heart_model.problem,
            (heart_model.activation, heart_model.lv_pressure),
            (target_activation, pressure[i]),
            continuation=False,
        )

        p_current = heart_model.get_pressure()
        v_current = heart_model.get_volume()
        outflow = v_current - v_old
        collector.collect(
            t + start_time,
            a_current_0,
            v_current,
            p_current,
            outflow,
            0,
        )

        if p_current < 0.01:
            break
    # for time, activation, vol, pres_val, ao_pres_val, flow in zip(time, activation, volume, presures, aortic_pressures, outflows):
    # writer.writerow([time, activation, vol, pres_val,ao_pres_val, flow])

    return collector
