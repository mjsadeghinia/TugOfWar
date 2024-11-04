# %%
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import argparse
from structlog import get_logger

from scipy.signal import find_peaks
from scipy.interpolate import splrep, splev

logger = get_logger()

# %%
def load_results(outdir, num_time_step=500, fname_suffix = ""):
    outdir = Path(outdir)
    if not fname_suffix=="":
        fname_suffix = f"_{fname_suffix}"
    data_ave = np.loadtxt(
        outdir.as_posix() + f"/data_ave{fname_suffix}.csv", delimiter=",", skiprows=1
    )
    data_std = np.loadtxt(
        outdir.as_posix() + f"/data_ave{fname_suffix}.csv", delimiter=",", skiprows=1
    )
    return data_ave, data_std


def bspline_fit_and_extrapolate(data_x, data_y, extrapolate_factor=0.1):
    # Fit B-spline to the data
    tck = splrep(data_x, data_y, s=0)
    # Extend the time series by 10%
    extended_time = np.linspace(
        data_x.min(),
        data_x.max() * (1 + extrapolate_factor),
        len(data_x) + int(len(data_x) * extrapolate_factor),
    )
    # Evaluate the B-spline over the extended time range
    smoothed_data_y = splev(extended_time, tck)

    return extended_time, smoothed_data_y


def extract_circ_results(fname):
    data = np.loadtxt(fname, delimiter=",", skiprows=1)
    ejection_indices = np.where(data[:, 5] > 0.1)[0]
    # MVO and MVC is found based on ejection (outflow)
    AVO_index = ejection_indices[0]
    AVC_index = ejection_indices[-1]
    mid_ejection_ind = ejection_indices[int(len(ejection_indices) / 2)]

    # MVO and MVC is found based on atrium pressure with threshold of 1kpa
    MVC_index = np.min(np.where(data[:, 3] > 1)[0])
    MVO_index = np.max(np.where(data[AVC_index:, 3] < 1)[0]) + AVC_index

    EDV = data[AVO_index - 1, 2]
    ESV = data[AVC_index + 1, 2]
    ejection_fraction = (EDV - ESV) / EDV

    return (
        ejection_fraction,
        AVO_index,
        AVC_index,
        mid_ejection_ind,
        MVO_index,
        MVC_index,
    )


def calculate_tow_index(ppeaks_ind, mid_ejection_ind=150):
    total_count = len(ppeaks_ind)
    tow_count = 0
    esl_count = 0
    lsl_count = 0
    both_count = 0

    for ppeak in ppeaks_ind:
        if ppeak.size > 0:
            tow_count += 1
            before_mid_ejection = np.any(ppeak < mid_ejection_ind)
            after_mid_ejection = np.any(ppeak >= mid_ejection_ind)

            if before_mid_ejection and after_mid_ejection:
                both_count += 1
            elif before_mid_ejection:
                esl_count += 1
            elif after_mid_ejection:
                lsl_count += 1
    try:
        tow_indices_percent = [
            tow_count / total_count * 100,
            esl_count / tow_count * 100,
            lsl_count / tow_count * 100,
            both_count / tow_count * 100,
        ]
    except ZeroDivisionError:
        tow_indices_percent = [0, 0, 0, 0]

    return tow_indices_percent


def export_results(outdir, ejection_fraction, tow_indices_percent,prominence, fname_suffix=""):
    outdir = Path(outdir)
    data = tow_indices_percent
    data.insert(0, ejection_fraction * 100)
    header = [
        "Ejection Fraction (%)",
        "Tug of War Index (%)",
        "ESL (%)",
        " LSL (%)",
        "Both (%)",
    ]
    if not fname_suffix=="":
        fname_suffix = f"_{fname_suffix}"
    np.savetxt(
        outdir.as_posix() + f"/00_tow_index_{prominence}{fname_suffix}.csv",
        np.array(data).reshape(1, -1),
        delimiter=",",
        header=",".join(header),
        fmt="%.2f",
    )


def plot_hist_tow(all_ppeaks, num_bins=50, x_range=(0, 1)):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(all_ppeaks, range=x_range, bins=num_bins, histtype="stepfilled")
    plt.grid(True)
    ax.set_xlabel("Normalized Time [-]")
    ax.set_ylabel("Number of p-peaks")
    # ax.set_ylim(x_range)
    return ax


def plot_data_with_extrapolation_and_peaks(
    data_x, data_y, extended_time, smoothed_data_y, ppeaks_ind_data, npeaks_ind_data
):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_x, data_y, "k--", label="Raw data")
    ax.plot(extended_time, smoothed_data_y, "k", label="B-Spline Smoothed Data")
    ax.scatter(
        extended_time[ppeaks_ind_data],
        smoothed_data_y[ppeaks_ind_data],
        color="blue",
        label="Positive Peaks",
    )
    ax.scatter(
        extended_time[npeaks_ind_data],
        smoothed_data_y[npeaks_ind_data],
        color="red",
        label="Negative Peaks",
    )
    # Shade the extrapolated region
    ax.axvspan(
        data_x.max(),
        extended_time.max(),
        color="grey",
        alpha=0.3,
        label="Extrapolated Region",
    )
    ax.set_xlabel("Normalized Time [-]")
    ax.set_ylabel("Strain in Fiber Direction [-]")
    ax.set_ylim([-0.3, 0.25])
    plt.legend(loc="lower left")
    plt.grid(True)
    return ax


def plot_valve_events_time(ax, time, AVO_index, AVC_index, MVO_index, MVC_index):
    y_min, y_max = ax.get_ylim()
    y_loc = (y_max) / 2
    plt.axvline(x=time[AVO_index], color="k", linestyle="--")
    plt.text(time[AVO_index - 5], y_loc, "AVO", rotation=90, verticalalignment="center")
    plt.axvline(x=time[AVC_index], color="k", linestyle="--")
    plt.text(time[AVC_index - 5], y_loc, "AVC", rotation=90, verticalalignment="center")
    plt.axvline(x=time[MVO_index], color="k", linestyle="--")
    plt.text(time[MVO_index - 5], y_loc, "MVO", rotation=90, verticalalignment="center")
    plt.axvline(x=time[MVC_index], color="k", linestyle="--")
    plt.text(time[MVC_index - 5], y_loc, "MVC", rotation=90, verticalalignment="center")


# %%
def parse_arguments(args=None):
    parser = argparse.ArgumentParser()
    # Segmentation parameters
    # Output folder
    parser.add_argument(
        "-o",
        "--outdir",
        default="peak_detection",
        type=Path,
        help="The output directory in the folder_data",
    )
    # Data folder
    parser.add_argument(
        "-f",
        "--data_folder",
        default=Path.cwd(),
        type=Path,
        help="The directory of the data to be post processed",
    )
    parser.add_argument(
        "-p",
        "--prominence",
        default=0.03,
        type=float,
        help="The prominence for the peak detection algorithm",
    )
    return parser.parse_args(args)


# %%
def main(args=None) -> int:
    if args is None:
        args = parse_arguments()
    prominence = args.prominence
    data_folder = args.data_folder
    outdir = data_folder / f"{args.outdir}"
    outdir_plots = data_folder / f"{args.outdir}/plots_{prominence}"
    outdir_plots.mkdir(exist_ok=True, parents=True)

    # loading circulation data
    fname = data_folder / "results_data.csv"
    ejection_fraction, AVO_ind, AVC_ind, mid_ejection_ind, MVO_index, MVC_index = (
        extract_circ_results(fname)
    )

    # loading strain data in fiber direction and postprocessing
    data_ave, data_std = load_results(outdir)
    time = data_ave[:, 0]
    Eff_ave = data_ave[:, 1:]
    npeaks_ind = []
    ppeaks_ind = []
    for i, data in enumerate(Eff_ave.T):
        extended_time, smoothed_data_y = bspline_fit_and_extrapolate(
            time, data, extrapolate_factor=0.1
        )
        ppeaks_ind_data = find_peaks(smoothed_data_y, prominence=prominence)
        npeaks_ind_data = find_peaks(-smoothed_data_y, prominence=prominence)
        ppeaks_ind.append(ppeaks_ind_data[0])
        npeaks_ind.append(npeaks_ind_data[0])
        ax = plot_data_with_extrapolation_and_peaks(
            time,
            data,
            extended_time,
            smoothed_data_y,
            ppeaks_ind_data[0],
            npeaks_ind_data[0],
        )
        plot_valve_events_time(ax, time, AVO_ind, AVC_ind, MVO_index, MVC_index)
        fname = outdir_plots / f"comp_{i}.png"
        plt.savefig(fname=fname)
        plt.close()

    tow_indices_percent = calculate_tow_index(
        ppeaks_ind, mid_ejection_ind=mid_ejection_ind
    )
    export_results(outdir, ejection_fraction, tow_indices_percent,prominence)
    all_ppeaks_arr = [arr for arr in ppeaks_ind if arr.size > 0]
    if len(all_ppeaks_arr) > 0:
        all_ppeaks_ind = np.concatenate(all_ppeaks_arr)
        all_ppeaks = extended_time[all_ppeaks_ind]
        fname = outdir / f"00_tow_histogram_{prominence}.png"
        ax = plot_hist_tow(all_ppeaks, x_range=(0, np.max(extended_time)))
        ax.axvspan(
            time.max(),
            extended_time.max(),
            color="grey",
            alpha=0.3,
            label="Extrapolated Region",
        )
        plot_valve_events_time(
            ax, extended_time, AVO_ind, AVC_ind, MVO_index, MVC_index
        )
        plt.savefig(fname=fname)
        plt.close()
        
        
    # loading strain data in circ direction and postprocessing
    outdir_plots = data_folder / f"{args.outdir}/plots_circ_{prominence}"
    outdir_plots.mkdir(exist_ok=True, parents=True)
    
    data_ave, data_std = load_results(outdir, fname_suffix='circ')
    time = data_ave[:, 0]
    Ecc_ave = data_ave[:, 1:]
    npeaks_ind = []
    ppeaks_ind = []
    for i, data in enumerate(Ecc_ave.T):
        extended_time, smoothed_data_y = bspline_fit_and_extrapolate(
            time, data, extrapolate_factor=0.1
        )
        ppeaks_ind_data = find_peaks(smoothed_data_y, prominence=prominence)
        npeaks_ind_data = find_peaks(-smoothed_data_y, prominence=prominence)
        ppeaks_ind.append(ppeaks_ind_data[0])
        npeaks_ind.append(npeaks_ind_data[0])
        ax = plot_data_with_extrapolation_and_peaks(
            time,
            data,
            extended_time,
            smoothed_data_y,
            ppeaks_ind_data[0],
            npeaks_ind_data[0],
        )
        plot_valve_events_time(ax, time, AVO_ind, AVC_ind, MVO_index, MVC_index)
        fname = outdir_plots / f"comp_{i}.png"
        plt.savefig(fname=fname)
        plt.close()

    tow_indices_percent = calculate_tow_index(
        ppeaks_ind, mid_ejection_ind=mid_ejection_ind
    )
    export_results(outdir, ejection_fraction, tow_indices_percent,prominence, fname_suffix='circ')
    all_ppeaks_arr = [arr for arr in ppeaks_ind if arr.size > 0]
    if len(all_ppeaks_arr) > 0:
        all_ppeaks_ind = np.concatenate(all_ppeaks_arr)
        all_ppeaks = extended_time[all_ppeaks_ind]
        fname = outdir / f"00_tow_histogram_circ_{prominence}.png"
        ax = plot_hist_tow(all_ppeaks, x_range=(0, np.max(extended_time)))
        ax.axvspan(
            time.max(),
            extended_time.max(),
            color="grey",
            alpha=0.3,
            label="Extrapolated Region",
        )
        plot_valve_events_time(
            ax, extended_time, AVO_ind, AVC_ind, MVO_index, MVC_index
        )
        plt.savefig(fname=fname)
        plt.close()



# %%
if __name__ == "__main__":
    main()
