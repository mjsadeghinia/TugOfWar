from typing import Protocol
import numpy as np
from pathlib import Path

from structlog import get_logger

from circ.datacollector import DataCollector
import dolfin
import pulse

logger = get_logger()


class HeartModel(Protocol):
    def compute_volume(self, activation: float, pressure: float) -> float: ...

    def get_pressure(self) -> float: ...

    def get_volume(self) -> float: ...

    def save(self, t: float, outdir: Path) -> None: ...

import numpy as np

def filter_volume_changes(data, delayed_activations, tolerance):
    filtered_data = {
        "time": [],
        "activation": [],
        "volume": [],
        "lv_pressure": [],
        "aortic_pressure": [],
        "outflow": []
    }
    delayed_activations_filtered = []

    if not data["volume"]:
        return filtered_data, delayed_activations_filtered

    # Adding the first row of data
    filtered_data["time"].append(data["time"][0])
    filtered_data["activation"].append(data["activation"][0])
    filtered_data["volume"].append(data["volume"][0])
    filtered_data["lv_pressure"].append(data["lv_pressure"][0])
    filtered_data["aortic_pressure"].append(data["aortic_pressure"][0])
    filtered_data["outflow"].append(data["outflow"][0])

    # Prepare to filter activations
    for activation_array in delayed_activations:
        delayed_activations_filtered.append([activation_array[0]])

    last_volume = data["volume"][0]

    for i in range(1, len(data["volume"])):
        current_volume = data["volume"][i]
        if abs(current_volume - last_volume) >= tolerance:
            filtered_data["time"].append(data["time"][i])
            filtered_data["activation"].append(data["activation"][i])
            filtered_data["volume"].append(current_volume)
            filtered_data["lv_pressure"].append(data["lv_pressure"][i])
            filtered_data["aortic_pressure"].append(data["aortic_pressure"][i])
            filtered_data["outflow"].append(data["outflow"][i])
            
            # Append corresponding activations
            for index, activation_array in enumerate(delayed_activations):
                delayed_activations_filtered[index].append(activation_array[i])

        last_volume = current_volume

    # Convert lists of activations to numpy arrays
    for index in range(len(delayed_activations_filtered)):
        delayed_activations_filtered[index] = np.array(delayed_activations_filtered[index])

    return filtered_data, delayed_activations_filtered

def get_elems(cfun, cfun_num):
    indices = np.where(cfun.array() == cfun_num)[0]
    return indices


def forward_solver(
    heart_model: HeartModel,
    activation: np.ndarray,
    pressure: np.ndarray,
    time: np.ndarray,
    collector: DataCollector | None = None,
    start_time: int = 0,
):
   
    if collector is None:
        collector = DataCollector(outdir=Path("results"), problem=heart_model)

    target_activation = dolfin.Function(heart_model.activation.ufl_function_space())
    aha = heart_model.geometry.cfun

    for i, t in enumerate(time):
        p_old = heart_model.get_pressure()
        v_old = heart_model.get_volume()
        for n in range(17):
            target_activation.vector()[get_elems(aha, n + 1)] = activation[n][i, :]
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
    # for time, activation, vol, pres_val, ao_pres_val, flow in zip(time, activation, volumes, presures, aortic_pressures, outflows):
    # writer.writerow([time, activation, vol, pres_val,ao_pres_val, flow])

    return collector