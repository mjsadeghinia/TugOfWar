#%%

from pathlib import Path
import argparse

import geometry


#%%
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mesh_size",
        default=2,
        type=float,
        help="The mesh size, approximate lenght of the edge for tetrahedrons [in cm]",
    )
    parser.add_argument(
        "--r_short_endo",
        default=3,
        type=float,
        help="The short radius of endo cardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_short_epi",
        default=3.75,
        type=float,
        help="The short radius of epi cardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_long_endo",
        default=4.25,
        type=float,
        help="The long radius of endo cardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_long_epi",
        default=5,
        type=float,
        help="The long radius of epi cardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "-c",
        "--num_circ_segments",
        default=18,
        type=int,
        help="The numer of circumferential compartments per slice",
    )
    parser.add_argument(
        "-r",
        "--num_long_segments",
        default=6,
        type=int,
        help="The number of slices (longitudinal)",
    )
    
    parser.add_argument(
        "-s",
        "--scenario",
        default='homogenous_compartment',
        type=str,
        help="The scenario for the alteraion of material properties, it can be 'single_compartment', 'homogenous_compartment' (default), or heterogenous_compartment' ",
    )
    
    parser.add_argument(
        "-t",
        "--num_time_step",
        default=500,
        type=float,
        help="The number of time step between 0 and 1",
    )
    parser.add_argument(
        "-o",
        "--outdir",
        default=str(Path.cwd()) + '/output',
        type=str,
        help="The output directory to save the files. ",
    )
    
    args = parser.parse_args()
    
    geo_params = {
    "r_short_endo": args.r_short_endo,
    "r_short_epi": args.r_short_epi,
    "r_long_endo": args.r_long_endo,
    "r_long_epi": args.r_long_epi,
    "mesh_size": args.mesh_size,
    }
    
    segmentation_schema = {
    "num_circ_segments": args.num_circ_segments,
    "num_long_segments": args.num_long_segments,
    }
    num_time_step = args.num_time_step
    outdir = Path(args.outdir)
    outdir.mkdir(exist_ok=True)
    scenario = args.scenario
    geo = geometry.create_ellipsoid_geometry(
        folder=outdir / "lv",
        geo_params=geo_params,
        segmentation_schema=segmentation_schema,
    )
    
#%%   
if __name__ == "__main__":
    main()