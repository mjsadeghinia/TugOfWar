import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt


def data_sampleing(data, n):
    n1 = round(n / 10)
    n2 = round(4 * n / 5)
    n3 = n - (n1 + n2)

    segment_i, segment_f = data_segmenting(data)

    times0, activations0, volumes0, pressures0, aortic_pressures0, outflows0 = (
        filling_phase_sampling(data, segment_i[0], segment_f[0])
    )
    times1, activations1, volumes1, pressures1, aortic_pressures1, outflows1 = (
        isovolumetric_phase_sampling(data, segment_i[1], segment_f[1], n1)
    )
    times2, activations2, volumes2, pressures2, aortic_pressures2, outflows2 = (
        ejection_phase_sampling(data, segment_i[2], segment_f[2], n2)
    )
    times3, activations3, volumes3, pressures3, aortic_pressures3, outflows3 = (
        isovolumetric_phase_sampling(data, segment_i[3], segment_f[3], n3)
    )

    sampled_data = {
        "time": np.concatenate(
            ([data["time"][0]], times0, times1, times2, times3)
        ).tolist(),
        "activation": np.concatenate(
            (
                [data["activation"][0]],
                activations0,
                activations1,
                activations2,
                activations3,
            )
        ).tolist(),
        "volume": np.concatenate(
            ([data["volume"][0]], volumes0, volumes1, volumes2, volumes3)
        ).tolist(),
        "lv_pressure": np.concatenate(
            ([data["lv_pressure"][0]], pressures0, pressures1, pressures2, pressures3)
        ).tolist(),
        "aortic_pressure": np.concatenate(
            (
                [data["aortic_pressure"][0]],
                aortic_pressures0,
                aortic_pressures1,
                aortic_pressures2,
                aortic_pressures3,
            )
        ).tolist(),
        "outflow": np.concatenate(
            ([data["outflow"][0]], outflows0, outflows1, outflows2, outflows3)
        ).tolist(),
    }

    return sampled_data


def data_segmenting(data):
    pressure = np.array(data["lv_pressure"])
    outflow = np.array(data["outflow"])

    # Finding the start of the systole by the time that pressure start increasing. Zero pressure are ommitted
    systole_indice = np.where(np.diff(pressure[np.where(pressure != 0)]) != 0)[0][0]
    # Determine segments based on outflow
    non_zero_outflow_indices = np.where(outflow != 0)[0]
    if len(non_zero_outflow_indices) == 0:
        return {}

    segment_i = [
        1,
        systole_indice,
        non_zero_outflow_indices[0],
        non_zero_outflow_indices[-1] + 1,
    ]
    segment_f = [
        systole_indice - 1,
        non_zero_outflow_indices[0] - 1,
        non_zero_outflow_indices[-1],
        len(outflow),
    ]

    return segment_i, segment_f


def filling_phase_sampling(data, start, end):
    return (
        [data["time"][start], data["time"][end]],
        [data["activation"][start], data["activation"][end]],
        [data["volume"][start], data["volume"][end]],
        [data["lv_pressure"][start], data["lv_pressure"][end]],
        [data["aortic_pressure"][start], data["aortic_pressure"][end]],
        [data["outflow"][start], data["outflow"][end]],
    )


def isovolumetric_phase_sampling(data, start, end, num_samples):
    segment_time = data["time"][start:end]
    segment_activation = data["activation"][start:end]
    segment_volume = data["volume"][start:end]
    segment_pressure = data["lv_pressure"][start:end]
    segment_aortic_pressure = data["aortic_pressure"][start:end]
    segment_outflow = data["outflow"][start:end]

    if len(segment_pressure) < 2 or num_samples < 1:
        return [], [], [], [], []

    mean_volume = np.mean(segment_volume)
    sampled_pressure = np.linspace(
        np.min(segment_pressure) * 1.01, np.max(segment_pressure) * 0.99, num_samples
    )

    time_interp = interp1d(
        segment_pressure, segment_time, kind="linear", fill_value="extrapolate"
    )
    activation_interp = interp1d(
        segment_pressure, segment_activation, kind="linear", fill_value="extrapolate"
    )
    aortic_pressure_interp = interp1d(
        segment_pressure,
        segment_aortic_pressure,
        kind="linear",
        fill_value="extrapolate",
    )
    outflow_interp = interp1d(
        segment_pressure, segment_outflow, kind="linear", fill_value="extrapolate"
    )

    # Create a structured array to reorder based on original time sequence
    sampled_data = np.array(
        list(
            zip(
                time_interp(sampled_pressure),
                activation_interp(sampled_pressure),
                np.full(num_samples, mean_volume),
                sampled_pressure,
                aortic_pressure_interp(sampled_pressure),
                outflow_interp(sampled_pressure),
            )
        ),
        dtype=[
            ("time", float),
            ("activation", float),
            ("volume", float),
            ("lv_pressure", float),
            ("aortic_pressure", float),
            ("outflow", float),
        ],
    )

    # Sort by 'time' to maintain the semblance of the original data order
    sampled_data_sorted = np.sort(sampled_data, order="time")

    return (
        sampled_data_sorted["time"],
        sampled_data_sorted["activation"],
        sampled_data_sorted["volume"],
        sampled_data_sorted["lv_pressure"],
        sampled_data_sorted["aortic_pressure"],
        sampled_data_sorted["outflow"],
    )


def ejection_phase_sampling(data, start, end, num_samples):
    segment_time = np.array(data["time"][start:end])
    segment_activation = np.array(data["activation"][start:end])
    segment_volume = np.array(data["volume"][start:end])
    segment_pressure = np.array(data["lv_pressure"][start:end])
    segment_aortic_pressure = np.array(data["aortic_pressure"][start:end])
    segment_outflow = np.array(data["outflow"][start:end])

    # Sorting for volumes as required by CubicSpline function
    sorted_indices = np.argsort(segment_volume)
    segment_volumes_sorted = segment_volume[sorted_indices]
    segment_pressure_sorted = segment_pressure[sorted_indices]
    segment_time_sorted = segment_time[sorted_indices]
    segment_activation_sorted = segment_activation[sorted_indices]
    segment_aortic_pressure_sorted = segment_aortic_pressure[sorted_indices]

    if len(segment_pressure_sorted) < 2 or num_samples < 1:
        return [], [], [], [], []

    sampled_volumes = np.linspace(
        np.min(segment_volumes_sorted), np.max(segment_volumes_sorted), num_samples
    )
    pressure_interp = CubicSpline(segment_volumes_sorted, segment_pressure_sorted)
    time_interp = CubicSpline(segment_volumes_sorted, segment_time_sorted)
    activation_interp = CubicSpline(segment_volumes_sorted, segment_activation_sorted)
    aortic_pressure_interp = CubicSpline(
        segment_volumes_sorted, segment_aortic_pressure_sorted
    )
    outflow_interp = CubicSpline(segment_volumes_sorted, segment_outflow)

    # Create a structured array to reorder based on original time sequence
    sampled_data = np.array(
        list(
            zip(
                time_interp(sampled_volumes),
                activation_interp(sampled_volumes),
                sampled_volumes,
                pressure_interp(sampled_volumes),
                aortic_pressure_interp(sampled_volumes),
                outflow_interp(sampled_volumes),
            )
        ),
        dtype=[
            ("time", float),
            ("activation", float),
            ("volume", float),
            ("lv_pressure", float),
            ("aortic_pressure", float),
            ("outflow", float),
        ],
    )

    # Sort by 'time' to maintain the semblance of the original data order
    sampled_data_sorted = np.sort(sampled_data, order="time")

    return (
        sampled_data_sorted["time"],
        sampled_data_sorted["activation"],
        sampled_data_sorted["volume"],
        sampled_data_sorted["lv_pressure"],
        sampled_data_sorted["aortic_pressure"],
        sampled_data_sorted["outflow"],
    )


def data_plotting(data, style="ro"):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # Create a figure and two subplots
    axs[0, 0].plot(data["time"], data["activation"], style)
    axs[0, 0].set_ylabel("Activation (kPa)")
    axs[0, 0].set_xlabel("Time (ms)")
    axs[0, 1].plot(data["volume"], data["lv_pressure"], style)
    axs[0, 1].set_ylabel("Pressure (kPa)")
    axs[0, 1].set_xlabel("Volume (ml)")
    ax2 = axs[0, 1].twinx()
    pressures_mmHg = np.array(data["lv_pressure"]) * 7.50062  # Convert to mmHg
    # Plotting the same data but converted on the second y-axis
    ax2.plot(
        data["volume"], pressures_mmHg, style, alpha=0
    )  # invisible plot just for axis
    ax2.set_ylabel("Pressure (mmHg)")
    axs[1, 0].plot(data["time"], data["outflow"], style)
    axs[1, 0].set_ylabel("Outflow (ml/s)")
    axs[1, 0].set_xlabel("Time (ms)")
    axs[1, 1].plot(data["time"], data["lv_pressure"], style, label="LV Pressure")
    axs[1, 1].plot(
        data["time"], data["aortic_pressure"], style, label="Aortic Pressure"
    )
    axs[1, 1].legend()
    axs[1, 1].set_ylabel("Pressure (kPa)")
    axs[1, 1].set_xlabel("Time (ms)")
    ax4 = axs[1, 1].twinx()
    ax4.plot(
        data["time"], pressures_mmHg, style, alpha=0
    )  # invisible plot just for axis
    ax4.set_ylabel("Pressure (mmHg)")


def generate_symmetric_jet_colors(n, reverse=False):
    if n % 2 == 0:
        num_colors = n // 2
    else:
        num_colors = (n - 1) // 2 + 1
    
    cmap_name = 'jet_r' if reverse else 'jet'
    cmap = plt.get_cmap(cmap_name)
    base_colors = [cmap(i / (num_colors - 1)) for i in range(num_colors)]
    
    if n % 2 == 0:
        final_colors = base_colors + base_colors[::-1]
    else:
        final_colors = base_colors + base_colors[-2::-1]
    
    return final_colors

def plot_ring_with_white_center(n, ax=None, inner_radius=0.7, reverse=False):
    colors = generate_symmetric_jet_colors(n, reverse)
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))  
    
    # Generate the circular sectors
    theta = np.linspace(0, 360, n+1)
    start_index = n // 2 if n % 2 == 0 else (n - 1) // 2 + 1
    for i in range(n):
        wedge = Wedge(center=(0, 0), r=.85, theta1=theta[i], theta2=theta[i+1], 
                      width=1-inner_radius, facecolor=colors[i], edgecolor='black')
        ax.add_patch(wedge)
        
        # Calculate the position for the text
        text_angle = (theta[i] + theta[i+1]) / 2
        text_x = 0.7 * np.cos(np.radians(text_angle))
        text_y = 0.7 * np.sin(np.radians(text_angle))
        
        # Calculate the number to display, starting from the middle segment
        number_to_display = (i + start_index) % n
        ax.text(text_x, text_y, str(number_to_display), ha='center', va='center', fontsize=12, color='white', weight='bold')
    
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')