# %%

from pathlib import Path
import argparse
import logging
from structlog import get_logger

import geometry
import activation_model

from circ.circulation_model import CirculationModel
from circ.datacollector import DataCollector

from coupling_solver import circulation_solver
from heart_model import HeartModelPulse

logger = get_logger()


# %%
def update_arguments(args):
    # If args is provided, merge with defaults
    default_args = parse_arguments()
    # Convert to namespace and update the defaults with provided args
    default_args = vars(default_args)
    for key, value in vars(args).items():
        if value is not None:
            default_args[key] = value
    args = argparse.Namespace(**default_args)
    return args


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

    # Arguments for circulation model
    parser.add_argument(
        "--aortic_resistance",
        default=5,
        type=float,
        help="The aortic resistance in the circulation model.",
    )
    parser.add_argument(
        "--systematic_resistance",
        default=10,
        type=float,
        help="The systematic resistance in the circulation model.",
    )
    parser.add_argument(
        "--systematic_compliance",
        default=10,
        type=float,
        help="The systematic compliance in the circulation model.",
    )
    parser.add_argument(
        "--aortic_pressure",
        default=10,
        type=float,
        help="The pressure requires to open the aortic valve.",
    )
    parser.add_argument(
        "--diastolic_pressure",
        default=10,
        type=float,
        help="The pressure at the prepheries defined as boundary condition.",
    )

    # Arguments for HeartModel boundary conditions
    parser.add_argument(
        "--pericardium_spring",
        default=0.0001,
        type=float,
        help="HeartModel BC: The stiffness of the spring on the pericardium.",
    )
    parser.add_argument(
        "--base_spring",
        default=0,
        type=float,
        help="HeartModel BC: The stiffness of the spring at the base.",
    )

    # Additional arguments for HeartModel
    parser.add_argument(
        "--atrium_pressure",
        default=1,
        type=float,
        help="HeartModel: The pressure for initial loading of HeartModel.",
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


def create_bc_params(args):
    """
    Create a dictionary of B.C. parameters from the parsed arguments.
    """
    return {
        "pericardium_spring": args.pericardium_spring,
        "base_spring": args.base_spring,
    }


def create_circ_params(args):
    """
    Create a dictionary of geometry parameters from the parsed arguments.
    """
    return {
        "aortic_resistance": args.aortic_resistance,
        "systematic_resistance": args.systematic_resistance,
        "systematic_compliance": args.systematic_compliance,
        "aortic_pressure": args.aortic_pressure,
        "diastolic_pressure": args.diastolic_pressure,
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


def create_activation_function(
    outdir,
    geo,
    segmentation_schema,
    scenario,
    activation_mode,
    activation_variation,
    num_time_step,
    random_flag=True,
):
    try:
        delayed_cfun = geometry.get_cfun_for_altered_compartment(segmentation_schema)
        delayed_activations = activation_model.compute_delayed_activation(
            scenario,
            geo.cfun,
            delayed_cfun,
            num_time_step=num_time_step,
            std=activation_variation,
            mode=activation_mode,
            random_flag=random_flag,
        )
        fname = outdir / "activation.xdmf"
        activation_model.save_activation_as_dolfin_function(
            geo, delayed_activations, fname
        )
        return fname
    except Exception as e:
        logger.error(f"Failed to create activation function: {e}")
        raise


def main(args=None) -> int:
    if args is None:
        args = parse_arguments(args)
    else:
        args = update_arguments(args)

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

    fname = create_activation_function(
        outdir,
        geo,
        segmentation_schema,
        scenario,
        activation_mode,
        activation_variation,
        num_time_step,
        random_flag=True,
    )

    bc_params = create_bc_params(args)
    heart_model = HeartModelPulse(geo=geo, bc_params=bc_params)

    circ_params = create_circ_params(args)
    circulation_model = CirculationModel(params=circ_params)

    collector = DataCollector(outdir=outdir, problem=heart_model)


# %%
if __name__ == "__main__":
    main()
