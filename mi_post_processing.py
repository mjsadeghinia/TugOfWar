from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import argparse

import dolfin
import geometry

from structlog import get_logger
logger = get_logger()

#%%

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
        "--slice",
        default=0,
        type=int,
        help="The number of slice to be processed",
    )
    
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

    slice = args.slice
    
    
    try:
        geo_folder = Path(data_folder) / "lv"
        geo = geometry.load_geo_with_cfun(geo_folder)
    except Exception:
        geo_folder = Path(data_folder) / "lv_coarse"
        geo = geometry.load_geo_with_cfun(geo_folder)
        
    infarct_fname = data_folder / "RoI.xdmf"
    infarct_comp = compute_infarct_compartment(infarct_fname, geo)
   

if __name__ == "__main__":
    main()