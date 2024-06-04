import dolfin as dolfin
import numpy as np

from cardiac_geometries.dolfin_utils import Geometry


def focal(r_long_endo: float, r_short_endo: float):
    return np.sqrt(r_long_endo**2 - r_short_endo**2)


def full_arctangent(x, y):
    t = np.arctan2(x, y)
    if t < 0:
        return t + 2 * np.pi
    else:
        return t


def cartesian_to_prolate_ellipsoidal(x, y, z, a):
    b1 = np.sqrt((x + a) ** 2 + y**2 + z**2)
    b2 = np.sqrt((x - a) ** 2 + y**2 + z**2)

    sigma = 1 / (2.0 * a) * (b1 + b2)
    tau = 1 / (2.0 * a) * (b1 - b2)
    phi = full_arctangent(z, y)
    nu = np.arccosh(sigma)
    mu = np.arccos(tau)
    return nu, mu, phi



class segments(dolfin.UserExpression):
    def __init__(self, foc: float, mu_base: float, num_circ_segments: int = 4, num_long_segments: int = 4) -> None:
        super().__init__()
        self.mu_base = abs(mu_base)
        self.foc = foc
        self.num_long_segments = num_long_segments
        self.num_circ_segments = num_circ_segments

    @property
    def dmu(self) -> float:
        return (np.pi - self.mu_base) / self.num_long_segments

    def eval_cell(self, value, x, ufc_cell):
        nu, mu, phi = cartesian_to_prolate_ellipsoidal(*x, a=self.foc)

        # Calculate the size of each segment in radians
        segment_size = 2 * np.pi / self.num_circ_segments
        
        for n in range(self.num_long_segments):
            if self.mu_base + self.dmu * n < mu <= self.mu_base + self.dmu * (n+1):
                for i in range(self.num_circ_segments):
                    if i * segment_size < phi <= (i + 1) * segment_size:
                        value[0] = n*self.num_circ_segments + i + 1
                        # break

    def value_shape(self):
        return ()


def segmentation(
    geometry: Geometry,
    r_long_endo: float,
    r_short_endo: float,
    mu_base: float,
    num_circ_segments: int = 4,
    num_long_segments: int = 4,
) -> Geometry:
    foc = focal(r_long_endo=r_long_endo, r_short_endo=r_short_endo)

    V = dolfin.FunctionSpace(geometry.mesh, "DG", 0)
    # f = dolfin.Function(V)
    expr = segments(foc=foc, mu_base=mu_base, num_circ_segments = num_circ_segments , num_long_segments = num_long_segments)
    f = dolfin.interpolate(expr, V)
    geometry.cfun.array()[:] = f.vector().get_local()
    return geometry

