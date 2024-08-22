# %%

from pathlib import Path
import argparse
import logging
from structlog import get_logger

import geometry

logger = get_logger()


# %%
def check_params_data(args):
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
        help="The scenario for the alteraion of material properties, Must be one of: "
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
        help="The parameter of study to be the modified, Must be one of: "
        + ", ".join(valid_params),
    )

    # Add the additional arguments for 'activation'
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
        help="The amount of activation_variation (required if 'activation' is chosen as parameter).",
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
        default=str(Path.cwd()) + "/output",
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

    outdir = Path(args.outdir)
    outdir.mkdir(exist_ok=True)

    ## Creating Geometry
    geo = geometry.create_ellipsoid_geometry(
        folder=outdir / "lv",
        geo_params=geo_params,
        segmentation_schema=segmentation_schema,
    )

    args = check_params_data(args)
    parameter = args.parameter
    activation_mode = args.activation_mode
    activation_variation = args.activation_variation
    scenario = args.scenario
    num_time_step = args.num_time_step


# %%
if __name__ == "__main__":
    main()
