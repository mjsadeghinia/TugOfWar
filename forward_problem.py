from typing import Protocol
import numpy as np
from pathlib import Path
from scipy.interpolate import interp1d, CubicSpline

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

def sample_data(data, n):
    volumes = np.array(data['volume'][1:])
    pressures = np.array(data['lv_pressure'][1:])
    times = np.array(data['time'][1:])
    outflows = np.array(data['outflow'][1:])
    activations = np.array(data['activation'][1:])
    aortic_pressures = np.array(data['aortic_pressure'][1:])

    # Determine segments based on outflow
    non_zero_outflow_indices = np.where(outflows != 0)[0]
    if len(non_zero_outflow_indices) == 0:
        return {}

    start_first_segment = 1
    end_first_segment = non_zero_outflow_indices[0]
    start_second_segment = non_zero_outflow_indices[0]
    end_second_segment = non_zero_outflow_indices[-1] + 1 if non_zero_outflow_indices[-1] < len(outflows) else len(outflows)
    start_third_segment = end_second_segment

    n1 = round(n / 10)
    n2 = round(4 * n / 5)
    n3 = n - (n1 + n2)

    def sample_segment_linear(start, end, num_samples):
        segment_pressures = pressures[start:end]
        segment_times = times[start:end]
        segment_activations = activations[start:end]
        segment_aortic_pressures = aortic_pressures[start:end]
        
        if len(segment_pressures) < 2 or num_samples < 1:
            return [], [], [], [], []

        mean_volume = np.mean(volumes[start:end])
        equal_pressure_points = np.linspace(np.min(segment_pressures), np.max(segment_pressures), num_samples)
        
        time_interp = interp1d(segment_pressures, segment_times, kind='linear', fill_value="extrapolate")
        activation_interp = interp1d(segment_pressures, segment_activations, kind='linear', fill_value="extrapolate")
        aortic_pressure_interp = interp1d(segment_pressures, segment_aortic_pressures, kind='linear', fill_value="extrapolate")

        return (np.full(num_samples, mean_volume),
                equal_pressure_points,
                time_interp(equal_pressure_points),
                activation_interp(equal_pressure_points),
                aortic_pressure_interp(equal_pressure_points))

    def sample_segment_cubic(start, end, num_samples):
        segment_volumes = volumes[start:end]
        segment_pressures = pressures[start:end]
        segment_times = times[start:end]
        segment_activations = activations[start:end]
        segment_aortic_pressures = aortic_pressures[start:end]

        sorted_indices = np.argsort(segment_volumes)
        segment_volumes_sorted = segment_volumes[sorted_indices]
        segment_pressures_sorted = segment_pressures[sorted_indices]
        segment_times_sorted = segment_times[sorted_indices]
        segment_activations_sorted = segment_activations[sorted_indices]
        segment_aortic_pressures_sorted = segment_aortic_pressures[sorted_indices]

        if len(segment_pressures_sorted) < 2 or num_samples < 1:
            return [], [], [], [], []

        sampled_volumes = np.linspace(np.min(segment_volumes_sorted), np.max(segment_volumes_sorted), num_samples)
        pressure_interp = CubicSpline(segment_volumes_sorted, segment_pressures_sorted)
        time_interp = CubicSpline(segment_volumes_sorted, segment_times_sorted)
        activation_interp = CubicSpline(segment_volumes_sorted, segment_activations_sorted)
        aortic_pressure_interp = CubicSpline(segment_volumes_sorted, segment_aortic_pressures_sorted)

        return (sampled_volumes,
                pressure_interp(sampled_volumes),
                time_interp(sampled_volumes),
                activation_interp(sampled_volumes),
                aortic_pressure_interp(sampled_volumes))

    volumes1, pressures1, times1, activations1, aortic_pressures1 = sample_segment_linear(start_first_segment, end_first_segment, n1)
    volumes2, pressures2, times2, activations2, aortic_pressures2 = sample_segment_cubic(start_second_segment, end_second_segment, n2)
    volumes3, pressures3, times3, activations3, aortic_pressures3 = sample_segment_linear(start_third_segment, len(pressures), n3)

    sampled_data = {
        "time": np.concatenate(([times[0]], times1, times2, times3)).tolist(),
        "activation": np.concatenate(([activations[0]], activations1, activations2, activations3)).tolist(),
        "volume": np.concatenate(([volumes[0]], volumes1, volumes2, volumes3)).tolist(),
        "lv_pressure": np.concatenate(([pressures[0]], pressures1, pressures2, pressures3)).tolist(),
        "aortic_pressure": np.concatenate(([aortic_pressures[0]], aortic_pressures1, aortic_pressures2, aortic_pressures3)).tolist(),
        "outflow": np.concatenate(([outflows[0]], np.full(len(times1)+len(times2)+len(times3), 0))).tolist()  # Assuming outflow is not interpolated and kept static
    }

    return sampled_data

def get_elems(cfun, cfun_num):
    indices = np.where(cfun.array() == cfun_num)[0]
    return indices


def forward_solver(
    heart_model: HeartModel,
    activation_delay: float,
    pressure: np.ndarray,
    time: np.ndarray,
    collector: DataCollector | None = None,
    start_time: int = 0,
):
   
    if collector is None:
        collector = DataCollector(outdir=Path("results"), problem=heart_model)

    delayed_activations = compute_delayed_activations(
        fe_model.geometry.cfun, num_time_step=num_time_step, std=delay
    )
    
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