# %%

from pathlib import Path
import numpy as np
from structlog import get_logger
import dolfin
import ast

import arg_parser
import geometry
import activation_model 

from circ.circulation_model import CirculationModel
from circ.datacollector import DataCollector

from coupling_solver import circulation_solver
from heart_model import HeartModelPulse

logger = get_logger()


# %%
def model_initialization(heart_model, circulation_model, collector):
    target_activation = dolfin.Function(heart_model.activation.ufl_function_space())
    target_activation.vector()[:] = 0
    v = heart_model.compute_volume(activation_value=target_activation, pressure_value=0)
    collector.collect(
        time=0,
        pressure=0,
        volume=v,
        activation=0.0,
        flow=circulation_model.flow,
        p_ao=circulation_model.aortic_pressure,
    )
    return v


def main(args=None) -> int:
    # Getting the arguments
    if args is None:
        args = arg_parser.parse_arguments(args)
    else:
        args = arg_parser.update_arguments(args)

    geo_params = arg_parser.create_geo_params(args)
    segmentation_schema = arg_parser.create_segmentation_schema(args)
    outdir = arg_parser.prepare_output_directory(args.outdir)
    args = arg_parser.check_parmas_activation(args)
    parameter = args.parameter
    activation_mode = args.activation_mode
    activation_variation = args.activation_variation
    bc_params = arg_parser.create_bc_params(args)
    circ_params = arg_parser.create_circ_params(args)
    scenario = args.scenario
    num_time_step = args.num_time_step
    postprocessing_flag = args.postprocessing
    ep_flag = args.ep                               # Flag for using ep driven activation
    randomized_flag = args.rn                       # Flag for using randomization for inducing further lsl
    comp_randomized_flag = args.crn                 # Flag for using randomization at compartments level
    comp_randomized_std = args.crn_std              # The std for the compartment randomization distribution in seconds
    mi_flag = args.mi                               # Flag for adding infarct
    mi_severity = args.mi_severity                  # Severity of MI; 1 = no contractile element 0 = normal tissue
    infarct_stiffness_percent = args.mi_stiffness   # Stiffness increase of MI region in percent, default 20
    iz_radius = args.iz_radius                      # The number of cfun for infarct zone
    bz_thickness = args.bz_thickness                # The number of cfun for border  zone
    mi_center = ast.literal_eval(args.mi_center)
    micomp_flag = args.micomp
    infarct = None
    infarct_comp = args.infarct_comp
    
    activation_fname = outdir / "activation.xdmf"
    if ep_flag:
        EP_folder = outdir / "EP"
        if not EP_folder.exists():
            arg_parser.copy_epdir_to_outdir(args.epdir, outdir)
        geo_folder = outdir / "lv_coarse"
        geo = geometry.load_geo_with_cfun(geo_folder)
        if mi_flag:
            if micomp_flag:
                RoI = activation_model.create_compartment_infarct(outdir, geo, infarct_comp, save_flag = True, varname= "RoI", fname="RoI")
            else:
                # Creating a region of interest by assuing mi_severity = 1 just for showing the region of interest
                RoI = activation_model.create_infarct(outdir, geo, mi_center, 1, iz_radius, bz_thickness, save_flag=True, varname= "RoI", fname="RoI")
        if not activation_fname.exists():
            geo = geometry.recreate_cfun(geo, segmentation_schema, geo_folder)
            activation_fname = activation_model.create_ep_activation_function(
                outdir,
                geo,
                segmentation_schema,
                scenario,
                activation_mode,
                activation_variation,
                num_time_step,
                mi_flag,
                mi_center,
                mi_severity,
                iz_radius,
                bz_thickness,
                micomp_flag,
                infarct_comp,
                randomized_flag,
                comp_randomized_flag,
                comp_randomized_std
            )
    else:
        ## Creating Geometry
        geo = geometry.create_ellipsoid_geometry(
            folder=outdir / "lv",
            geo_params=geo_params,
            segmentation_schema=segmentation_schema,
        )
        if not activation_fname.exists():
            ## Creating Activation
            activation_fname = activation_model.create_activation_function(
                outdir,
                geo,
                segmentation_schema,
                scenario,
                activation_mode,
                activation_variation,
                num_time_step,
                random_flag=True,
            )
    outdir_activations = outdir / "Activations"
    outdir_activations.mkdir(exist_ok=True)
    activation_model.plot_ep_activation_all_compartments(segmentation_schema, outdir_activations, geo_folder, activation_fname, num_time_step=500)        
    # Model Generation
    # Creating a stiff_region by assuing mi_severity = 1 and bz_thickness=0, i.e. no borderzone
    if micomp_flag:
        StiffRegion = activation_model.create_compartment_infarct(outdir, geo, infarct_comp, save_flag = True, varname= "StiffRegion", fname="StiffRegion")
    else:
        StiffRegion = activation_model.create_infarct(outdir, geo, mi_center, 1.0, iz_radius, 0.0, save_flag=True, varname= "StiffRegion", fname="StiffRegion")
    heart_model = HeartModelPulse(geo=geo, bc_params=bc_params, infarct = StiffRegion, infarct_stiffness_percent=infarct_stiffness_percent)
    circulation_model = CirculationModel(params=circ_params)
    collector = DataCollector(outdir=outdir, problem=heart_model)

    # Initializing the model with zero pressure and activaiton
    v = model_initialization(heart_model, circulation_model, collector)

    # Initial loading of the model to atrium pressure with zero activation
    atrium_pressure = args.atrium_pressure
    volume = heart_model.initial_loading(atrium_pressure=atrium_pressure)
    collector.collect(
        time=1,
        pressure=atrium_pressure,
        volume=volume,
        activation=0.0,
        flow=circulation_model.flow,
        p_ao=circulation_model.aortic_pressure,
    )

    # Solving for the model for the time span of 0 to 1. The model stops if the pressure<0.5
    t_span = (0.0, 1.0)
    t_eval = np.linspace(*t_span, num_time_step)
    collector = circulation_solver(
        heart_model=heart_model,
        circulation_model=circulation_model,
        activation_fname=activation_fname,
        time=t_eval * 1000,
        collector=collector,
        start_time=2,
    )


# %%
if __name__ == "__main__":
    main()
