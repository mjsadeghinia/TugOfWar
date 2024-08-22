# %%

from pathlib import Path
import argparse
import logging
from structlog import get_logger

import geometry

logger = get_logger()


# %%
def parse_arguments(args=None):
    """
    Parse the command-line arguments.
    """
    parser = argparse.ArgumentParser()

    # Geometry parameters
    parser.add_argument(
        "-m",
        "--mesh_size",
        default=2,
        type=float,
        help="The mesh size, approximate length of the edge for tetrahedrons [in cm]",
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

    # Segmentation parameters
    parser.add_argument(
        "-c",
        "--num_circ_segments",
        default=18,
        type=int,
        help="The number of circumferential compartments per slice",
    )
    parser.add_argument(
        "-r",
        "--num_long_segments",
        default=6,
        type=int,
        help="The number of slices (longitudinal)",
    )

    # Scenario and parameters
    valid_scenarios = [
        "single_compartment",
        "homogenous_compartment",
        "heterogenous_compartment",
    ]
    parser.add_argument(
        "-s",
        "--scenario",
        choices=valid_scenarios,
        default="homogenous_compartment",
        type=str,
        help="The scenario for the alteration of material properties. Must be one of: "
             + ", ".join(valid_scenarios),
    )

    valid_params = [
        "activation",
        "passive_stiffness",
        "active_stiffness",
        "fiber_disarray",
    ]
    parser.add_argument(
        "-p",
        "--parameter",
        choices=valid_params,
        default="activation",
        type=str,
        help="The parameter of study to be modified. Must be one of: "
             + ", ".join(valid_params),
    )

    # Additional arguments for 'activation'
    valid_activation_mode = ["delay", "diastole_time", "systole_time", "decay"]
    parser.add_argument(
        "--activation_mode",
        choices=valid_activation_mode,
        type=str,
        help="The mode of activation (required if 'activation' is chosen as parameter).",
    )
    parser.add_argument(
        "--activation_variation",
        type=float,
        help="The amount of activation variation (required if 'activation' is chosen as parameter).",
    )

    # Additional settings
    parser.add_argument(
        "-t",
        "--num_time_step",
        default=500,
        type=float,
        help="The number of time steps between 0 and 1",
    )
    parser.add_argument(
        "-o",
        "--outdir",
        default=str(Path.cwd()) + "/output",
        type=str,
        help="The output directory to save the files.",
    )

    return parser.parse_args(args)

def create_geo_params(args):
    """
    Create a dictionary of geometry parameters from the parsed arguments.
    """
    return {
        "r_short_endo": args.r_short_endo,
        "r_short_epi": args.r_short_epi,
        "r_long_endo": args.r_long_endo,
        "r_long_epi": args.r_long_epi,
        "mesh_size": args.mesh_size,
    }

def create_segmentation_schema(args):
    """
    Create a dictionary of segmentation schema from the parsed arguments.
    """
    return {
        "num_circ_segments": args.num_circ_segments,
        "num_long_segments": args.num_long_segments,
    }

def prepare_output_directory(args):
    """
    Prepare the output directory, ensuring it exists.
    """
    outdir_path = Path(args.outdir)
    outdir_path.mkdir(exist_ok=True)
    return outdir_path

def check_parmas_activation(args):
    """
    Check if all the necessary input is provided otherwise assing a default vaule and issues warning to prevent any unwanted results.
    """
    if args.parameter == "activation":
        if args.activation_mode is None:
            args.activation_mode = "delay"
            logger.warning(
                f"--activation_mode not provided for 'activation'; using default value: {args.activation_mode}"
            )
        if args.activation_variation is None:
            args.activation_variation = 0
            logger.warning(
                f"--activation_variation not provided for 'activation'; using default value: {args.activation_variation}"
            )
    return args


def main(args=None) -> int:
    if args is None:
        args = parse_arguments(args)

    geo_params = create_geo_params(args)

    segmentation_schema = create_segmentation_schema(args)

    outdir = prepare_output_directory(args)
    
    ## Creating Geometry
    geo = geometry.create_ellipsoid_geometry(
        folder=outdir / "lv",
        geo_params=geo_params,
        segmentation_schema=segmentation_schema,
    )

    args = check_parmas_activation(args)
    parameter = args.parameter
    activation_mode = args.activation_mode
    activation_variation = args.activation_variation
    scenario = args.scenario
    num_time_step = args.num_time_step


# %%
if __name__ == "__main__":
    main()
