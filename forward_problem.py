from typing import Protocol
import numpy as np
from pathlib import Path
import logging

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
    logging.getLogger("pulse").setLevel(logging.WARNING)
    if collector is None:
        collector = DataCollector(outdir=Path("results"), problem=heart_model)

    delayed_activations = compute_delayed_activations(
        heart_model.geometry.cfun, std=activation_delay, t_interp=np.array(time[1:])/1000
    )

    target_activation = dolfin.Function(heart_model.activation.ufl_function_space())
    aha = heart_model.geometry.cfun

    for pres in pressure[:2]:
        volume = heart_model.compute_volume(activation_value=0, pressure_value=pres)
        collector.collect(
            time=0,
            pressure=pres,
            volume=volume,
            activation=0.0,
            flow=0,
            p_ao=0,
        )


    for i, t in enumerate(time[1:]):
        v_old = heart_model.get_volume()
        for n in range(17):
            target_activation.vector()[get_elems(aha, n + 1)] = delayed_activations[n][i, :]
        a_current_mean = np.mean(target_activation.vector()[:])
        pulse.iterate.iterate(
            heart_model.problem,
            (heart_model.activation),
            (target_activation),
            continuation=False,
        )
        pulse.iterate.iterate(
            heart_model.problem,
            (heart_model.lv_pressure),
            (pressure[i+1]),
            continuation=False,
        )
        p_current = heart_model.get_pressure()
        v_current = heart_model.get_volume()
        logger.info("Computed volume", volume_current=v_current)
        outflow = v_old - v_current 
        collector.collect(
            t,
            a_current_mean,
            v_current,
            p_current,
            outflow,
            0,
        )

        # if p_current < 0.01:
        #     break
    # for time, activation, vol, pres_val, ao_pres_val, flow in zip(time, activation, volume, presures, aortic_pressures, outflows):
    # writer.writerow([time, activation, vol, pres_val,ao_pres_val, flow])

    return collector
