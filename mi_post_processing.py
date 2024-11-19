from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import argparse
from scipy.signal import find_peaks
from scipy.interpolate import splrep, splev

import dolfin
import geometry

from structlog import get_logger
logger = get_logger()

#%%
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

def load_infarct_from_file(
    fname: Path, mesh: dolfin.mesh
):
    fname = Path(fname)
    V = dolfin.FunctionSpace(mesh, "DG", 0)
    u = dolfin.Function(V)
    with dolfin.XDMFFile(fname.as_posix()) as xdmf:
        xdmf.read_checkpoint(u, "RoI", 0)
    return u

def compute_value_compartment(value: list, cfun: dolfin.MeshFunction):
    value_array = np.array(value)
    cfuns = set(cfun.array())
    value_compartments = []
    for c in cfuns:
        num_elem = geometry.get_elems(cfun, c)
        value_compartments.append(value_array[num_elem])
    return value_compartments


def compute_infarct_compartment(infarct_fname, geo):
    
    infarct_function = load_infarct_from_file(infarct_fname, geo.mesh)
    infarct_value = infarct_function.vector()[:]
    infarct_comp_allcells = compute_value_compartment(infarct_value, geo.cfun)
    infarct_comp = np.zeros(len(infarct_comp_allcells))
    for i, value in enumerate(infarct_comp_allcells):
        if np.any(value):
            infarct_comp[i] = 1
            
    return infarct_comp
            
def slice_data(data, slice_no, num_circ_segments):
    n_i = (slice_no-1)*num_circ_segments
    n_f = n_i + num_circ_segments
    if len(data.shape) == 1:
        return data[n_i:n_f]
    elif len(data.shape) == 2:
        return data[:, n_i:n_f]
    else:
        logger.error("Data input has 3 or more dimensions")
        return 0

def extract_circ_results(fname):
    data = np.loadtxt(fname, delimiter=",", skiprows=1)
    ejection_indices = np.where(data[:, 5] > 0.0)[0]
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
 
def peak_detection(data, time, prominence=0.03):
    extended_time, smoothed_data_y = bspline_fit_and_extrapolate(
        time, data, extrapolate_factor=0.1
    )
    ppeaks_ind_data = find_peaks(smoothed_data_y, prominence=prominence)
    npeaks_ind_data = find_peaks(-smoothed_data_y, prominence=prominence)
    return ppeaks_ind_data[0], npeaks_ind_data[0]

def get_flag_value_for_peaks(peaks, mid_ejection_ind):
    # Determine the flag value based on the values in ppeaks[index] relative to mid_ejection_ind
    if peaks.size == 0:
        return 0
    elif np.all(peaks < mid_ejection_ind):
        return 1
    elif np.all(peaks > mid_ejection_ind):
        return 2
    else:
        return 3

def plot_ring(ppeak_flags, infarct_comp_slice, save_path, num_segments_comp=4):
    """
    Plots a ring with N segments, where N is the size of the input arrays.
    Adds a white circle in the center to make it a hollow ring.
    Optionally adds another slice every `num_circ_segments_new` segments with a width of 4.
    
    Parameters:
    - ppeak_flags: 1D numpy array of size N with values 0, 1, 2, or 3.
    - infarct_comp_slice: 1D numpy array of size N with values 0 or 1.
    - save_path: File path to save the plot.
    - num_circ_segments_new: Optional, draw an extra slice every `num_circ_segments_new` segments. Default is 4.
    """
    N = len(ppeak_flags)
    if len(infarct_comp_slice) != N:
        raise ValueError("ppeak_flags and infarct_comp_slice must have the same length.")

    # Angles for the slices
    angles = np.linspace(0, 2 * np.pi, N + 1)

    # Colors for the face based on ppeak_flags
    face_colors = ['grey' if flag == 0 else
                   'yellow' if flag == 1 else
                   'orange' if flag == 2 else
                   'red' for flag in ppeak_flags]

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.axis('off')  # Hide axes
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_yticks([])  # Hide the radial ticks

    # Plot each segment
    for i in range(N):
        theta_start = angles[i]
        theta_end = angles[i + 1]
        color = face_colors[i]
        edge_color = 'red' if infarct_comp_slice[i] == 1 else None

        # Draw the slice
        ax.bar(x=(theta_start + theta_end) / 2, height=1, width=theta_end - theta_start,
               color=color, edgecolor=edge_color, linewidth=2, align='center')

        # Add extra slice every num_circ_segments_new segments
        if i % num_segments_comp == 0:
            theta_end = angles[i + num_segments_comp]
            ax.bar(x=(theta_start + theta_end) / 2, height=1, width=theta_end - theta_start,
                   facecolor='none', edgecolor='black', linewidth=1, align='center')
            
    ax.bar(x=(np.pi), height=.5, width=np.pi*2,
        facecolor='white', edgecolor='black', linewidth=1, align='center')
    ax.bar(x=(np.pi), height=.499, width=np.pi*2,
        facecolor='white', edgecolor='none', linewidth=0, align='center')
    
    # Save the plot
    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()





       
#%%
def parse_arguments(args=None):
    parser = argparse.ArgumentParser()
    # Segmentation parameters
    parser.add_argument(
        "-c",
        "--num_circ_segments",
        default=72,
        type=int,
        help="The number of circumferential compartments per slice",
    )
    parser.add_argument(
        "-l",
        "--num_long_segments",
        default=6,
        type=int,
        help="The number of slices (longitudinal)",
    )
    
    parser.add_argument(
        "-s",
        "--slice_nums",
        default=5,
        type=int,
        nargs='+',
        help="The number of slice to be processed",
    )
    
    parser.add_argument(
        "-n",
        "--num_segments_comp",
        default=4,
        type=int,
        help="The number of compartment for post processing segmentation",
    )
    
    # Output folder
    parser.add_argument(
        "-o",
        "--outdir",
        default="72_6",
        type=Path,
        help="The output directory in the folder_data",
    )
    # Data folder
    parser.add_argument(
        "-f",
        "--data_folder",
        default=Path("/home/shared/01_results_24_11_21/test2"),
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

def main(args=None) -> int:
    if args is None:
        args = parse_arguments()
    prominence = args.prominence
    data_folder = args.data_folder
    outdir = data_folder / f"{args.outdir}"
    num_long_segments = args.num_long_segments
    num_circ_segments = args.num_circ_segments
    num_segments_comp = args.num_segments_comp

    slice_nums = args.slice_nums
    
    
    try:
        geo_folder = Path(data_folder) / "lv"
        geo = geometry.load_geo_with_cfun(geo_folder)
    except Exception:
        geo_folder = Path(data_folder) / "lv_coarse"
        geo = geometry.load_geo_with_cfun(geo_folder)

    # loading circulation data
    fname = data_folder / "results_data.csv"
    ejection_fraction, AVO_ind, AVC_ind, mid_ejection_ind, MVO_index, MVC_index = (
        extract_circ_results(fname)
    )
    
    
    infarct_fname = data_folder / "RoI.xdmf"   
    if not infarct_fname.exists():
        infarct_comp = np.zeros(int(num_circ_segments*num_long_segments))
    else:    
        infarct_comp = compute_infarct_compartment(infarct_fname, geo)
    
    # loading strain data in fiber direction and slicing
    outdir = data_folder / f"{args.outdir}"
    data_ave, data_std = load_results(outdir)
    time = data_ave[:, 0]
    Eff_ave = data_ave[:, 1:]
    for slice_num in slice_nums:
        Eff_ave_slice = slice_data(Eff_ave, slice_num, num_circ_segments)
        
        ppeak_flags = []
        npeak_flags = []
        for i in range(num_circ_segments):
            data = Eff_ave_slice[:,i]
            ppeaks, npeaks = peak_detection(data, time, prominence=prominence)
            ppeak_flag = get_flag_value_for_peaks(ppeaks, mid_ejection_ind)
            npeak_flag = get_flag_value_for_peaks(npeaks, mid_ejection_ind)
            ppeak_flags.append(ppeak_flag)
            npeak_flags.append(npeak_flag)
            
        infarct_comp_slice = slice_data(infarct_comp, slice_num, num_circ_segments)
        fname = outdir / f'mi_slice_{slice_num}'
        plot_ring(ppeak_flags, infarct_comp_slice, fname.as_posix(), num_segments_comp=num_segments_comp)
        calculate_segment_towi(ppeak_flags, infarct_comp_slice, num_segments_comp)
    
if __name__ == "__main__":
    main()