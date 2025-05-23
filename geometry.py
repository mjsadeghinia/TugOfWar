# %%
import numpy as np
from pathlib import Path
from typing import Union
from structlog import get_logger

import cardiac_geometries
from dolfin import XDMFFile

from segmentation import segmentation

logger = get_logger()

# %%


def get_default_geo_params():
    """
    Default geometrical parameter for the left ventricle
    """
    return {
        "r_short_endo": 3,
        "r_short_epi": 3.75,
        "r_long_endo": 4.25,
        "r_long_epi": 5,
        "mesh_size": 1,
        'fiber_angle_endo': -60,
        'fiber_angle_epi': 60,
    }


def get_geo_params(geo_params):
    # Use provided geo_params or default ones if not provided
    default_geo_params = get_default_geo_params()
    geo_params = (
        {
            key: geo_params.get(key, default_geo_params[key])
            for key in default_geo_params
        }
        if geo_params
        else default_geo_params
    )
    return geo_params


def create_ellipsoid_geometry(
    folder: Path, geo_params: dict = None, segmentation_schema: dict = None
):
    """
    Generates the ellipsoid geometry based on cardiac_geometries, for info look at caridiac_geometries.

    Parameters:
    folder (Path): The directory to save or read the geometry.
    geo_params (dict): Geometric properties for the ellipsoid model.

    Returns:
    A geometry object compatible with the pulse.MechanicsProblem.
    """
    geo_params = get_geo_params(geo_params)

    if segmentation_schema is None:
        aha_flag = True
    else:
        aha_flag = False

    cardiac_geometries.mesh.create_lv_ellipsoid(
        outdir=folder,
        r_short_endo=geo_params["r_short_endo"],
        r_short_epi=geo_params["r_short_epi"],
        r_long_endo=geo_params["r_long_endo"],
        r_long_epi=geo_params["r_long_epi"],
        psize_ref=geo_params["mesh_size"],
        mu_apex_endo=-np.pi,
        mu_base_endo=-np.arccos(
            geo_params["r_short_epi"] / geo_params["r_long_endo"] / 2
        ),
        mu_apex_epi=-np.pi,
        mu_base_epi=-np.arccos(
            geo_params["r_short_epi"] / geo_params["r_long_epi"] / 2
        ),
        create_fibers=True,
        fiber_angle_endo=geo_params["fiber_angle_endo"],
        fiber_angle_epi=geo_params["fiber_angle_epi"],
        fiber_space="P_1",
        aha=aha_flag,
    )
    if aha_flag:
        # Trying to force cardiac_geometries to read cfun, containing aha 17 segments
        schema = cardiac_geometries.geometry.Geometry.default_schema()
        cfun_schema = schema["cfun"]._asdict()
        cfun_schema["fname"] = "cfun.xdmf:f"
        schema["cfun"] = cardiac_geometries.geometry.H5Path(**cfun_schema)
        geo = cardiac_geometries.geometry.Geometry.from_folder(folder, schema=schema)
    else:
        geo = cardiac_geometries.geometry.Geometry.from_folder(folder)
        mu_base_endo = -np.arccos(
            geo_params["r_short_epi"] / geo_params["r_long_endo"] / 2
        )
        geo = segmentation(
            geo,
            geo_params["r_long_endo"],
            geo_params["r_short_endo"],
            mu_base_endo,
            segmentation_schema["num_circ_segments"],
            segmentation_schema["num_long_segments"],
        )
        with XDMFFile((folder / "cfun.xdmf").as_posix()) as xdmf:
            xdmf.write(geo.cfun)
    # geo = cardiac_geometries.geometry.Geometry.from_folder(folder)
    fname = folder / "geo"
    geo.save(fname.as_posix())
    return geo


def load_geo(fname: Union[str, Path], comm=None):
    fname = Path(fname)
    geo = cardiac_geometries.geometry.Geometry.from_file(fname.as_posix(), comm=comm)
    return geo

def load_geo_with_cfun(geo_folder):
    schema = cardiac_geometries.geometry.Geometry.default_schema()
    cfun_schema = schema["cfun"]._asdict()
    cfun_schema["fname"] = "cfun.xdmf:f"
    schema["cfun"] = cardiac_geometries.geometry.H5Path(**cfun_schema)
    geo = cardiac_geometries.geometry.Geometry.from_folder(geo_folder, schema=schema)
    return geo

def recreate_cfun(geo, segmentation_schema, folder):
    geo_params = {
        "r_short_endo": 3,
        "r_short_epi": 3.75,
        "r_long_endo": 4.25,
        "r_long_epi": 5,
        "mesh_size": 1,
        'fiber_angle_endo': -60,
        'fiber_angle_epi': 60,
    }
    mu_base_endo = -np.arccos(
    geo_params["r_short_epi"] / geo_params["r_long_endo"] / 2
    )   
    geo = segmentation(
        geo,
        geo_params["r_long_endo"],
        geo_params["r_short_endo"],
        mu_base_endo,
        segmentation_schema["num_circ_segments"],
        segmentation_schema["num_long_segments"],
    )
    with XDMFFile((folder / "cfun.xdmf").as_posix()) as xdmf:
        xdmf.write(geo.cfun)
    return geo

def get_cfun_for_altered_compartment(segmentation_schema):
    return (int(segmentation_schema["num_long_segments"]/2)-1)*segmentation_schema["num_circ_segments"]+1

def get_first_compartment_midslice(segmentation_schema):
    return (int(segmentation_schema["num_long_segments"]/2)-1)*segmentation_schema["num_circ_segments"]+1

def get_cfun_for_iz_compartment(segmentation_schema, infarct_zone_len = 4):
    #infarct_zone_len = 4 cell function as IZ
    ind_1_slice = get_first_compartment_midslice(segmentation_schema)
    ind_i_mi = ind_1_slice + segmentation_schema["num_circ_segments"]/4 - infarct_zone_len/2
    ind_f_mi = ind_i_mi + infarct_zone_len - 1 
    return int(ind_i_mi), int(ind_f_mi)
    
def get_cfun_for_bz_compartment(ind_i_mi, ind_f_mi, border_zone_len = 3):
    # border zones compartments
    # border_zone_len = 3 cell function as BZ
    ind_i_bz_1 = ind_i_mi -  border_zone_len
    ind_f_bz_1 = ind_i_mi - 1 
    ind_i_bz_2 = ind_i_mi + 1 
    ind_f_bz_2 = ind_i_mi + border_zone_len 
    return int(ind_i_bz_1), int(ind_f_bz_1), int(ind_i_bz_2), int(ind_f_bz_2)
    
    
    
def get_cfun_for_adjacent_compartment(cfun_num, segmentation_schema, geo):
    n = segmentation_schema["num_circ_segments"]
    compartments_indices = []
    for _ in range(n):
        cfun_num += 1
        compartment_indices = np.where(geo.cfun.array() == cfun_num)[0]
        compartments_indices.append(compartment_indices)
    return compartments_indices

def get_elems(cfun, cfun_num):
    indices = np.where(cfun.array() == cfun_num)[0]
    return indices