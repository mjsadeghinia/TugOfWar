from pathlib import Path
import geometry
import argparse

from structlog import get_logger
logger = get_logger()


def create_geo_params_coarse(args):
    """
    Create a dictionary of geometry parameters from the parsed arguments.
    """
    return {
        "r_short_endo": args.r_short_endo,
        "r_short_epi": args.r_short_epi,
        "r_long_endo": args.r_long_endo,
        "r_long_epi": args.r_long_epi,
        "mesh_size": args.coarse_mesh_size,
        "fiber_angle_endo": args.fiber_angle_endo,
        "fiber_angle_epi": args.fiber_angle_epi,
    }
    
    
def create_geo_params_fine(args):
    """
    Create a dictionary of geometry parameters from the parsed arguments.
    """
    return {
        "r_short_endo": args.r_short_endo,
        "r_short_epi": args.r_short_epi,
        "r_long_endo": args.r_long_endo,
        "r_long_epi": args.r_long_epi,
        "mesh_size": args.fine_mesh_size,
        "fiber_angle_endo": args.fiber_angle_endo,
        "fiber_angle_epi": args.fiber_angle_epi,
    }

def main(args=None) -> int:
    # Getting the arguments

    parser = argparse.ArgumentParser()

    # Geometry parameters
    parser.add_argument(
        "-mc",
        "--coarse_mesh_size",
        default=0.5,
        type=float,
        help="The coarse mesh size, approximate length of the edge for tetrahedrons [in cm]",
    )
    parser.add_argument(
        "-mf",
        "--fine_mesh_size",
        default=0.1,
        type=float,
        help="The fine mesh size, approximate length of the edge for tetrahedrons [in cm]",
    )
    parser.add_argument(
        "--r_short_endo",
        default=3,
        type=float,
        help="The short radius of endocardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_short_epi",
        default=3.75,
        type=float,
        help="The short radius of epicardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_long_endo",
        default=4.25,
        type=float,
        help="The long radius of endocardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--r_long_epi",
        default=5,
        type=float,
        help="The long radius of epicardium [in cm] for generating a simplified ellipsoid left ventricle model",
    )
    parser.add_argument(
        "--fiber_angle_endo",
        default=-60,
        type=float,
        help="The fiber angle on the endocardium",
    )
    
    parser.add_argument(
        "--fiber_angle_epi",
        default=60,
        type=float,
        help="The fiber angle on the epicardium",
    )
    
    # Export parameters
    parser.add_argument(
        "-o",
        "--outdir",
        default=Path.cwd() / "output",
        type=Path,
        help="The output directory to save the files.",
    )

    parser.add_argument(
        "-g",
        "--geo_folder",
        default="lv",
        type=str,
        help="The folder containing the geometry",
    )
    args = parser.parse_args(args)
    outdir = args.outdir
    geo_params_coarse = create_geo_params_coarse(args)
    geo_params_fine = create_geo_params_fine(args)
    geo_folder_coarse = outdir / f"{args.geo_folder}_coarse"
    geo_folder_fine = outdir / f"{args.geo_folder}_fine"

    geo_coarse = geometry.create_ellipsoid_geometry(
        folder=geo_folder_coarse,
        geo_params=geo_params_coarse,
    )
    geo_fine = geometry.create_ellipsoid_geometry(
        folder=geo_folder_fine,
        geo_params=geo_params_fine,
    )
    

if __name__ == "__main__":
    main()
