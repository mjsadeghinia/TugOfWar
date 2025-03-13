import argparse
from pathlib import Path
from structlog import get_logger
import shutil

logger = get_logger()


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
        default=0.5,
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

    # flag for using EP based modeling
    parser.add_argument(
        "-ep",
        action="store_true",
        help="The flag for whether using electrophysiology model or not",
    )
    
    # flag for using randomization to induce further LSL
    parser.add_argument(
        "-rn",
        action="store_true",
        help="The flag for whether using randomization to induce further LSL or not",
    )
    
    
    # flag for using randomization to induce further LSL
    parser.add_argument(
        "-crn",
        action="store_true",
        help="The flag for whether using randomization at compartments level or not",
    )
    
    
    # flag for using EP based modeling
    parser.add_argument(
        "-mi",
        action="store_true",
        help="The flag for whether adding Infarct region or not (ONLY IN EP MODEL)",
    )
    
    # flag for using EP based modeling
    parser.add_argument(
        "-micomp",
        action="store_true",
        help="The flag for whether adding Infarct as an compartment (hardcoded) or based on mi center",
    )
    
    parser.add_argument(
        "--infarct_comp",
        default=5,
        type=int,
        nargs='+',
        help="The number of slice to be processed",
    )
    
    parser.add_argument(
        "--mi_center",
        default="(-1.47839,3.52203e-16,3.15815)",
        type=str,
        help="The center of infarct zone (tuple)",
    )
    
    parser.add_argument(
        "--mi_severity",
        default=1,
        type=float,
        help="Severity of MI; 1 = no contractile element 0 = normal tissue",
    )
    
    parser.add_argument(
        "--mi_stiffness",
        default=20,
        type=float,
        help="Stiffness increase (a in Holzapfel-Ogden Model) of MI region in percent, default 20",
    )
    
    # flag for using EP based modeling
    parser.add_argument(
        "--iz_radius",
        default=0.8,
        type=float,
        help="The radius of the infarct zone",
    )
    
     # flag for using EP based modeling
    parser.add_argument(
        "--bz_thickness",
        default=0.0,
        type=float,
        help="The thickness of border zone",
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
    valid_activation_mode = ["delay", "diastole_time", "systole_time", "decay", "peak", "rate"]
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
        default=30,
        type=float,
        help="The systematic resistance in the circulation model.",
    )
    parser.add_argument(
        "--systematic_compliance",
        default=5,
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
        default=0.0001,
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
        "--postprocessing",
        default=True,
        type=bool,
        help="The flag for postprocessing",
    )
    
    parser.add_argument(
        "--epdir",
        default="/home/shared/00_EP_results",
        type=str,
        help="The directory to EP simulation files including EP, lv_coarse, and lv_fine folders.",
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
        "fiber_angle_endo": args.fiber_angle_endo,
        "fiber_angle_epi": args.fiber_angle_epi,
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


def prepare_output_directory(outdir):
    """
    Prepare the output directory, ensuring it exists.
    """
    outdir_path = Path(outdir)
    outdir_path.mkdir(exist_ok=True, parents=True)
    return outdir_path


def copy_epdir_to_outdir(epdir, outdir):
    epdir = Path(epdir)
    for item in epdir.iterdir():
        if item.is_dir():
            destination_path = outdir / item.name
            if not destination_path.exists():
                shutil.copytree(item, destination_path)
                
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

def parse_arguments_post(args=None):
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
    # activation file name
    parser.add_argument(
        "--activation_fname",
        default="activation.xdmf",
        type=str,
        help="The file name of activation",
    )
    # Data folder
    parser.add_argument(
        "-f",
        "--data_folder",
        default=Path.cwd(),
        type=Path,
        help="The directory of the data to be post processed",
    )
    # Output folder
    parser.add_argument(
        "-o",
        "--outdir",
        default='plots',
        type=Path,
        help="The output directory in the folder_data",
    )
    # Additional settings
    parser.add_argument(
        "-t",
        "--num_time_step",
        default=500,
        type=float,
        help="The number of time steps between 0 and 1",
    )
    return parser.parse_args(args)
    