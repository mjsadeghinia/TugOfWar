# %%
# import dolfin.function
import numpy as np
from pathlib import Path
from structlog import get_logger
from typing import Union

import cardiac_geometries
import pulse
import dolfin

logger = get_logger()


# %%
class HeartModelPulse:
    def __init__(
        self,
        geo: pulse.HeartGeometry = None,
        geo_refinement: int = None,
        geo_params: dict = None,
        geo_folder: Path = Path("lv"),
        bc_params: dict = None,
    ):
        """
        Initializes the heart model with given geometrical parameters and folder for geometrical data.

        Parameters:
        geo_params (dict, optional): Dictionary of geometric parameters.
        geo_folder (Path): Path object indicating the folder where geometry data is stored.
        """

        if geo is None:
            self._get_geo_params(geo_params)
            self.geometry = self.get_ellipsoid_geometry(geo_folder, self.geo_params)
            if geo_refinement is not None:
                geo_refined = self.refine_geo(self.geometry, geo_refinement)
                self.geometry = geo_refined
        else:
            self.geometry = geo
            if geo_refinement is not None:
                geo_refined = self.refine_geo(self.geometry, geo_refinement)
                self.geometry = geo_refined

        V = dolfin.FunctionSpace(self.geometry.mesh, "DG", 0)
        self.lv_pressure = dolfin.Constant(0.0, name="LV Pressure")
        self.activation = dolfin.Function(V, name="Activation")

        self.E_ff = []

        self.material = self.get_material_model()
        self._get_bc_params(bc_params)
        self.bcs = self.apply_bcs()
        self.problem = pulse.MechanicsProblem(self.geometry, self.material, self.bcs)
        self.problem.solve()

    def compute_volume(
        self, activation_value: Union[float, np.ndarray], pressure_value: float
    ) -> float:
        """
        Computes the volume of the heart model based on activation and pressure values.

        Parameters:
        activation_value (float): The activation value to be applied.
        pressure_value (float): The pressure value to be applied.

        Returns:
        float: The computed volume of the heart model.
        """
        # logger.info(
        #     "Computing volume",
        #     activation_value=activation_value,
        #     pressure_value=pressure_value,
        # )
        # It is very important to turn off continuation, other wise you would get division by zero, when one or both parameter is the same

        # if not (
        #     np.isclose(float(self.activation), activation_value)
        #     and np.isclose(float(self.lv_pressure), pressure_value)
        #  ):
        # pulse.iterate.iterate(
        #     self.problem,
        #     (self.activation, self.lv_pressure),
        #     (activation_value, pressure_value),
        #     continuation=False,
        # )
        pulse.iterate.iterate(self.problem, self.activation, activation_value)
        pulse.iterate.iterate(self.problem, self.lv_pressure, pressure_value)

        volume_current = self.problem.geometry.cavity_volume(
            u=self.problem.state.sub(0)
        )
        logger.info("Computed volume", volume_current=volume_current)
        return volume_current

    def dVdp(
        self, activation_value: Union[float, np.ndarray], pressure_value: float
    ) -> float:
        """
        Computes dV/dP, with V is the volume of the model and P is the pressure.
        The derivation is computed as the change of volume due to a small change in the pressure at a given pressure.
        After computation the problem is reset to its initial state.

        NB! We use problem.solve() instead of pulse.iterate.iterate, as the pressure change is small and iterate may fail.

        Parameters:
        activation_value (float): The activation value to be applied.
        pressure_value (float): The pressure value to be applied.

        Returns:
        float: The computed dV/dP .
        """
        logger.info(
            "Computing dV/dP",
            activation_value=activation_value.vector()[0],
            pressure_value=pressure_value,
        )
        # Backing up the problem
        state_backup = self.problem.state.copy(deepcopy=True)
        pressure_backup = float(self.lv_pressure)
        activation_backup = self.activation
        # Update the problem with the give activation and pressure and store the initial State of the problem
        self.assign_state_variables(activation_value, pressure_value)
        self.problem.solve()
        p_i = self.get_pressure()
        v_i = self.get_volume()

        # small change in pressure and computing the volume
        p_f = p_i * (1 + 0.001)
        # breakpoint()
        self.lv_pressure.assign(p_f)
        self.problem.solve()
        v_f = self.get_volume()

        dV_dP = (v_f - v_i) / (p_f - p_i)
        logger.info("Computed dV/dP", dV_dP=dV_dP)

        # reset the problem to its initial state
        self.problem.state.assign(state_backup)
        self.assign_state_variables(activation_backup, pressure_backup)

        return dV_dP

    def get_pressure(self) -> float:
        return float(self.lv_pressure)

    def get_volume(self) -> float:
        return self.problem.geometry.cavity_volume(u=self.problem.state.sub(0))

    def save(self, t: float, outdir: Path = Path("results")):
        """
        Saves the current state of the heart model at a given time to a specified file.

        Parameters:
        t (float): The time at which to save the model state.
        outname (Path): The file path to save the model state.
        """
        fname = outdir / "results.xdmf"
        if np.isclose(t, 0.0):
            fname.unlink(missing_ok=True)
            fname.with_suffix(".h5").unlink(missing_ok=True)

        results_u, _ = self.problem.state.split(deepcopy=True)
        results_u.t = t
        with dolfin.XDMFFile(fname.as_posix()) as xdmf:
            xdmf.write_checkpoint(
                results_u, "u", float(t + 1), dolfin.XDMFFile.Encoding.HDF5, True
            )

        F = pulse.kinematics.DeformationGradient(results_u)
        E = pulse.kinematics.GreenLagrangeStrain(F)
        # Green strain normal to fiber direction
        V = dolfin.FunctionSpace(self.geometry.mesh, "DG", 0)
        Eff_t = dolfin.project(dolfin.inner(E * self.geometry.f0, self.geometry.f0), V)
        E_ff_segment = []
        for n in range(17):
            indices = np.where(self.problem.geometry.cfun.array() == n + 1)[0]
            E_ff_segment.append(Eff_t.vector()[indices])
        self.E_ff.append(E_ff_segment)

        results_activation = dolfin.project(self.activation, V)
        fname = outdir / "activation.xdmf"
        with dolfin.XDMFFile(fname.as_posix()) as xdmf:
            xdmf.write_checkpoint(
                results_activation,
                "activation",
                float(t + 1),
                dolfin.XDMFFile.Encoding.HDF5,
                True,
            )

    def assign_state_variables(self, activation_value, pressure_value):
        self.lv_pressure.assign(pressure_value)
        self.activation.assign(activation_value)

    def get_ellipsoid_geometry(self, folder: Path, geo_props: dict):
        """
        Generates the ellipsoid geometry based on cardiac_geometries, for info look at caridiac_geometries.

        Parameters:
        folder (Path): The directory to save or read the geometry.
        geo_props (dict): Geometric properties for the ellipsoid model.

        Returns:
        A geometry object compatible with the pulse.MechanicsProblem.
        """
        # if not folder.exists():
        cardiac_geometries.mesh.create_lv_ellipsoid(
            outdir=folder,
            r_short_endo=geo_props["r_short_endo"],
            r_short_epi=geo_props["r_short_epi"],
            r_long_endo=geo_props["r_long_endo"],
            r_long_epi=geo_props["r_long_epi"],
            psize_ref=geo_props["mesh_size"],
            mu_apex_endo=-np.pi,
            mu_base_endo=-np.arccos(
                geo_props["r_short_epi"] / geo_props["r_long_endo"] / 2
            ),
            mu_apex_epi=-np.pi,
            mu_base_epi=-np.arccos(
                geo_props["r_short_epi"] / geo_props["r_long_epi"] / 2
            ),
            create_fibers=True,
            fiber_angle_endo=-60,
            fiber_angle_epi=60,
            fiber_space="P_1",
            aha=True,
        )
        # Trying to force cardiac_geometries to read cfun, containing aha 17 segments
        schema = cardiac_geometries.geometry.Geometry.default_schema()
        cfun_schema = schema["cfun"]._asdict()
        cfun_schema["fname"] = "cfun.xdmf:f"
        schema["cfun"] = cardiac_geometries.geometry.H5Path(**cfun_schema)

        geo = cardiac_geometries.geometry.Geometry.from_folder(folder, schema=schema)
        marker_functions = pulse.MarkerFunctions(cfun=geo.cfun, ffun=geo.ffun)
        microstructure = pulse.Microstructure(f0=geo.f0, s0=geo.s0, n0=geo.n0)
        return pulse.HeartGeometry(
            mesh=geo.mesh,
            markers=geo.markers,
            marker_functions=marker_functions,
            microstructure=microstructure,
        )
        
    @staticmethod
    def refine_geo(geo, geo_refinement):
        mesh, cfun, ffun = geo.mesh, geo.cfun, geo.ffun 
        dolfin.parameters["refinement_algorithm"] = "plaza_with_parent_facets"
        for _ in range(geo_refinement):
            mesh = dolfin.adapt(mesh)
            cfun = dolfin.adapt(cfun, mesh)
            ffun = dolfin.adapt(ffun, mesh)
            
        geo.f0.set_allow_extrapolation(True)
        geo.s0.set_allow_extrapolation(True)
        geo.n0.set_allow_extrapolation(True)

        V_refined = dolfin.FunctionSpace(mesh, geo.f0.function_space().ufl_element())
        
        f0_refined = dolfin.Function(V_refined)
        f0_refined.interpolate(geo.f0)    
        s0_refined = dolfin.Function(V_refined)
        s0_refined.interpolate(geo.s0)  
        n0_refined = dolfin.Function(V_refined)
        n0_refined.interpolate(geo.n0)  
            
        marker_functions = pulse.MarkerFunctions(cfun=cfun, ffun=ffun)
        microstructure = pulse.Microstructure(f0=geo.f0, s0=geo.s0, n0=geo.n0)
        return pulse.HeartGeometry(
            mesh=mesh,
            markers=geo.markers,
            marker_functions=marker_functions,
            microstructure=microstructure,
        )

    def get_material_model(self):
        """
        Constructs the material model for the heart using default parameters.

        Returns:
        A material model object for use in a pulse.MechanicsProblem.
        """
        # matparams = pulse.HolzapfelOgden.default_parameters()
        matparams = dict(
            a=2.28,
            a_f=1.686,
            b=9.726,
            b_f=15.779,
            a_s=0.0,
            b_s=0.0,
            a_fs=0.0,
            b_fs=0.0,
        )

        return pulse.HolzapfelOgden(
            activation=self.activation,
            active_model="active_stress",
            parameters=matparams,
            f0=self.geometry.f0,
            s0=self.geometry.s0,
            n0=self.geometry.n0,
        )

    def apply_bcs(self):
        bcs = pulse.BoundaryConditions(
            dirichlet=(self._fixed_base_x,),
            neumann=self._neumann_bc(),
            robin=self._robin_bc(),
        )
        return bcs

    def _fixed_endoring(self, W):
        V = W if W.sub(0).num_sub_spaces() == 0 else W.sub(0)

        # Fixing the endo ring in all directions to prevent rigid body motion
        endo_ring_points = self._get_endo_ring()
        endo_ring_points_x0 = np.mean(endo_ring_points[:, 0])
        endo_ring_points_radius = np.sqrt(
            np.min((endo_ring_points[:, 1] ** 2 + endo_ring_points[:, 2] ** 2))
        )

        class EndoRing_subDomain(dolfin.SubDomain):
            def __init__(self, x0, x2):
                super().__init__()
                self.x0 = x0
                self.x2 = x2
                print(x0)

            def inside(self, x, on_boundary):
                return dolfin.near(x[0], self.x0, 0.01) and dolfin.near(
                    pow(pow(x[1], 2) + pow(x[2], 2), 0.5), self.x2, 0.1
                )

        endo_ring_fixed = dolfin.DirichletBC(
            V,
            dolfin.Constant((0.0, 0.0, 0.0)),
            EndoRing_subDomain(endo_ring_points_x0, endo_ring_points_radius),
            method="pointwise",
        )
        return endo_ring_fixed

    def _fixed_base(self, W):
        V = W if W.sub(0).num_sub_spaces() == 0 else W.sub(0)

        # Fixing the base in x[0] direction
        bc_fixed_based = dolfin.DirichletBC(
            V,
            dolfin.Constant((0.0, 0.0, 0.0)),
            self.geometry.ffun,
            self.geometry.markers["BASE"][0],
        )

        return bc_fixed_based

    def _fixed_base_x(self, W):
        V = W if W.sub(0).num_sub_spaces() == 0 else W.sub(0)

        # Fixing the base in x[0] direction
        bc_fixed_based = dolfin.DirichletBC(
            V.sub(0),
            dolfin.Constant((0.0)),
            self.geometry.ffun,
            self.geometry.markers["BASE"][0],
        )

        return bc_fixed_based

    def _neumann_bc(self):
        # LV Pressure
        lv_marker = self.geometry.markers["ENDO"][0]
        lv_pressure = pulse.NeumannBC(
            traction=self.lv_pressure, marker=lv_marker, name="lv"
        )
        neumann_bc = [lv_pressure]
        return neumann_bc

    def _robin_bc(self):
        if self.bc_params["pericardium_spring"] > 0.0:
            robin_bc = [
                pulse.RobinBC(
                    value=dolfin.Constant(self.bc_params["pericardium_spring"]),
                    marker=self.geometry.markers["EPI"][0],
                ),
            ]
        else:
            robin_bc = []
        return robin_bc

    def _get_geo_params(self, geo_params):
        # Use provided geo_params or default ones if not provided
        default_geo_params = self.get_default_geo_params()
        self.geo_params = (
            {
                key: geo_params.get(key, default_geo_params[key])
                for key in default_geo_params
            }
            if geo_params
            else default_geo_params
        )

    def _get_bc_params(self, bc_params):
        # Use provided geo_params or default ones if not provided
        default_bc_params = self.get_default_bc_params()
        self.bc_params = (
            {
                key: bc_params.get(key, default_bc_params[key])
                for key in default_bc_params
            }
            if bc_params
            else default_bc_params
        )

    def _get_endo_ring(self):
        endo_ring_points = []
        for fc in dolfin.facets(self.geometry.mesh):
            if self.geometry.ffun[fc] == self.geometry.markers["BASE"][0]:
                for vertex in dolfin.vertices(fc):
                    endo_ring_points.append(vertex.point().array())
        endo_ring_points = np.array(endo_ring_points)
        return endo_ring_points

    @staticmethod
    def get_default_geo_params():
        """
        Default geometrical parameter for the left ventricle
        """
        return {
            "r_short_endo": 3,
            "r_short_epi": 3.75,
            "r_long_endo": 5,
            "r_long_epi": 5.75,
            "mesh_size": 2.5,
        }

    @staticmethod
    def get_default_bc_params():
        """
        Default BC parameter for the left ventricle
        """
        return {
            "pericardium_spring": 0,
            "base_spring": 0,
        }
