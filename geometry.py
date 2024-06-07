#%% 
import numpy as np
from pathlib import Path
from typing import Union
from structlog import get_logger

import cardiac_geometries
from dolfin import XDMFFile, MPI

from segmentation import segmentation

logger = get_logger()

#%%

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
        
def create_ellipsoid_geometry(folder: Path, geo_params: dict = None, segmentation_schema: dict = None):
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
            fiber_angle_endo=-60,
            fiber_angle_epi=60,
            fiber_space="P_1",
            aha=aha_flag,
        )
        if aha_flag:
            # Trying to force cardiac_geometries to read cfun, containing aha 17 segments
            schema = cardiac_geometries.geometry.Geometry.default_schema()
            cfun_schema = schema["cfun"]._asdict()
            cfun_schema["fname"] = "cfun.xdmf:f"
            schema["cfun"] = cardiac_geometries.geometry.H5Path(**cfun_schema)
            geo = cardiac_geometries.geometry.Geometry.from_folder(
                folder, schema=schema
            )
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
        fname = folder / 'geo'
        geo.save(fname.as_posix())
        return geo

def load_geo(fname: Union[str, Path], comm=None):
    fname = Path(fname)
    geo = cardiac_geometries.geometry.Geometry.from_file(fname.as_posix(), comm = comm)
    return geo

#%%
# comm = dolfin.MPI.comm_world