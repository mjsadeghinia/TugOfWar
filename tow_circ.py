#%%
from pathlib import Path
import logging
import cardiac_geometries
import pulse
import dolfin
import ufl_legacy as ufl
from pulse.solver import NonlinearSolver
from pulse.solver import NonlinearProblem
from pulse.utils import getLogger

import copy
import csv
import numpy as np
import matplotlib.pyplot as plt
import activation_model
from scipy.integrate import solve_ivp

logger = getLogger(__name__)

global p_current, p_old

#%% Parameters
# [ms] [cm] [ml] [kPa] 
# Constants

R_ao = 1     #   aortic resistance [kPa][ml][ms]^{-1}
R_circ = 10  #   systemic circulation resistance [kPa][ml][ms]^{-1}
C_circ = 5   #   ystemic circulation capacitance [ml][kPa]^{-1}

t_res=1000
# t_span = (0.0, 1000.0)

# # Initial Aortic Pressure and fixed diasotlic pressure
p_ao=10
p_dia=10

# # Assuming 5 cm for LVEDd (ED diameter), and .75cm for wall thickness.  
r_short_endo = 3
r_short_epi = 3.75
r_long_endo = 5.0
r_long_epi = 5.5
mesh_size=3
# # Sigma_0 for activation parameter
sigma_0=150     #[kPa]
t_sys=160      #[ms]
t_dias=484      #[ms] 

results_name='results.xdmf'
outdir = Path("results")
outdir.mkdir(exist_ok=True, parents=True)
outname = Path(outdir) / results_name
if outname.is_file():
    outname.unlink()
    outname.with_suffix(".h5").unlink()
#%%

def get_ellipsoid_geometry(folder=Path("lv"),r_short_endo = 7,r_short_epi = 10,r_long_endo = 17,r_long_epi = 20, mesh_size=3):
    geo = cardiac_geometries.mesh.create_lv_ellipsoid(
        outdir= folder,
        r_short_endo = r_short_endo,
        r_short_epi = r_short_epi,
        r_long_endo = r_long_endo,
        r_long_epi = r_long_epi,
        psize_ref = mesh_size,
        mu_apex_endo = -np.pi,
        mu_base_endo = -np.arccos(r_short_epi / r_long_endo/2),
        mu_apex_epi = -np.pi,
        mu_base_epi = -np.arccos(r_short_epi / r_long_epi/2),
        create_fibers = True,
        fiber_angle_endo = -60,
        fiber_angle_epi = +60,
        fiber_space = "P_1",
        aha = True,
    )
    marker_functions = pulse.MarkerFunctions(cfun=geo.cfun, ffun=geo.ffun, efun=geo.efun)
    microstructure = pulse.Microstructure(f0=geo.f0, s0=geo.s0, n0=geo.n0)
    geometry=pulse.HeartGeometry(
        mesh=geo.mesh,
        markers=geo.markers,
        marker_functions=marker_functions,
        microstructure=microstructure,
    )
    return geometry

geometry = get_ellipsoid_geometry(folder=Path("lv"),r_short_endo = r_short_endo, r_short_epi = r_short_epi, r_long_endo = r_long_endo, r_long_epi = r_long_epi, mesh_size=mesh_size)
geometry.mesh
print(geometry.cavity_volume())
#%% creating a normal activation model
t_span = (0.0, 1.0)
t_eval = np.linspace(*t_span, t_res)
normal_activation_params = activation_model.default_parameters()
normal_activation_params['sigma_0']=sigma_0*1000
normal_activation_params['t_sys']=t_sys/1000
normal_activation_params['t_dias']=t_dias/1000

normal_activation = (
    activation_model.activation_function(
        t_span=t_span,
        t_eval=t_eval,
        parameters=normal_activation_params,
    )
    / 1000.0
)
systole_ind=np.where(normal_activation == 0)[0][-1]+1
normal_activation_systole=normal_activation[systole_ind:]
t_eval_systole=t_eval[systole_ind:]*1000

#%% creating the tow_activation
def create_infarct(V, center_1=(0, 4, 4), center_2=(-6, 0, 0)) -> dolfin.Function:
    expr = dolfin.Expression(
        "(exp(-(pow(x[0] - x1, 2) + pow(x[1] - y1, 2) + pow(x[2] - z1, 2)) / pow(sigma1, 2)) + exp(-(pow(x[0] - x1, 2) + pow(x[1] + y1, 2) + pow(x[2] - z1, 2)) / pow(sigma1, 2)) +exp(-(pow(x[0] - x1, 2) + pow(x[1] - y1, 2) + pow(x[2] + z1, 2)) / pow(sigma1, 2)) + exp(-(pow(x[0] - x1, 2) + pow(x[1] + y1, 2) + pow(x[2] + z1, 2)) / pow(sigma1, 2)) + exp(-(pow(x[0] - x2, 2) + pow(x[1] - y2, 2) + pow(x[2] - z2, 2)) / pow(sigma2, 2)))/100",
        degree=1,
        x1=center_1[0],
        y1=center_1[1],
        z1=center_1[2],
        sigma1=4.0,
        x2=center_2[0],
        y2=center_2[1],
        z2=center_2[2],
        sigma2=7.0,
    )
    f = dolfin.interpolate(expr, V)
    return f

V = dolfin.FunctionSpace(geometry.mesh, "CG", 1)
infarct = create_infarct(V=V)
with dolfin.XDMFFile((outdir / "infarct.xdmf").as_posix()) as xdmf:
    xdmf.write_checkpoint(
        infarct,
        "infarct",
        0.0,
        dolfin.XDMFFile.Encoding.HDF5,
        False,
    )
# Find the delayed activation dofs
delays = infarct.vector().get_local()
target_activation = dolfin.Function(V)
activation = dolfin.Function(V)

delayed_activations=np.zeros((normal_activation.shape[0],delays.shape[0]))
i=0
for i, delay in enumerate(delays):
    delayed_activation_params = normal_activation_params.copy()
    delayed_activation_params["t_sys"] += delay*5
    delayed_activation_params["t_dias"] += delay*5
    delayed_activation = (
        activation_model.activation_function(
            t_span=t_span,
            t_eval=t_eval,
            parameters=delayed_activation_params,
        )
        / 1000.0
    )
    delayed_activations[:,i]=delayed_activation


# %% Defining activation as dolfin.constant

activation = dolfin.Constant(0.0, name='gamma')

#%% Material Properties
matparams = pulse.HolzapfelOgden.default_parameters()
material = pulse.HolzapfelOgden(
    activation=activation,
    active_model="active_stress",
    parameters=matparams,
    f0=geometry.f0,
    s0=geometry.s0,
    n0=geometry.n0,
)
#%% Boundary Conditions
# ------------------- Fix base and/or endoring  -------------------------
# Finidng the endo ring radius
pnts=[]
radii=[]
for fc in dolfin.facets(geometry.mesh):
    if geometry.ffun[fc]==geometry.markers['BASE'][0]:
        for vertex in dolfin.vertices(fc):
            pnts.append(vertex.point().array())
pnts=np.array(pnts)            
EndoRing_radius=np.sqrt(np.min((pnts[:,1]**2+pnts[:,2]**2)))
print(f'Endoring radius is {EndoRing_radius}')
# EndoRing_subDomain = dolfin.CompiledSubDomain('near(x[0], 1, 0.001) && near(pow(x[1],2)+pow(x[2],2), radius, 0.001)', radius=EndoRing_radius)

def AllBCs(W):
    V = W if W.sub(0).num_sub_spaces() == 0 else W.sub(0)
    bc_fixed_based = dolfin.DirichletBC(
        V.sub(0),
        dolfin.Constant(0.0),
        geometry.ffun,
        geometry.markers["BASE"][0],
    )
    class EndoRing_subDomain(dolfin.SubDomain):
        def inside(self, x, on_boundary):
            return dolfin.near(x[0], 1.875, .01) and dolfin.near(pow(pow(x[1],2)+pow(x[2],2),0.5), 2.78, .1)
    endo_ring_fixed=dolfin.DirichletBC(
        V,
        dolfin.Constant((0.0,0.0,0.0)),
        EndoRing_subDomain(),
        method="pointwise",
    )
    return [bc_fixed_based,endo_ring_fixed]
dirichlet_bc = (AllBCs,)


# ------------------- LV pressure on ENDO surface -------------------------
# LV Pressure
lvp = dolfin.Constant(0.0, name='LV Pressure')
lv_marker = geometry.markers["ENDO"][0]
lv_pressure = pulse.NeumannBC(traction=lvp, marker=lv_marker, name="lv")
neumann_bc = [lv_pressure]

# Collect boundary conditions
bcs = pulse.BoundaryConditions(
    dirichlet=dirichlet_bc,
    neumann=neumann_bc,
    # robin=robin_bc,
)
#%%
problem = pulse.MechanicsProblem(geometry, material, bcs)

vols=[]
pres=[]
flows=[]
ao_pres=[]
# Saving the initial pressure and volume
v_current=geometry.cavity_volume()
p_current=lvp.values()[0]
vols.append(v_current)
pres.append(p_current)
flows.append(0)
ao_pres.append(p_ao)
# %% Initialization to the atrium pressure of 0.2 kPa
pulse.iterate.iterate(problem, lvp, 0.02, initial_number_of_steps=15)
v_current=geometry.cavity_volume(u=problem.state.sub(0))
p_current=lvp.values()[0]
vols.append(v_current)
pres.append(p_current)
flows.append(0)
ao_pres.append(p_ao)
reults_u, p = problem.state.split(deepcopy=True)
reults_u.t=0
with dolfin.XDMFFile(outname.as_posix()) as xdmf:
    xdmf.write_checkpoint(reults_u, "u", float(0), dolfin.XDMFFile.Encoding.HDF5, True)
# %%
tau=t_eval_systole[1]-t_eval_systole[0]
#%%
def WK3(t,y):
    # Defining WK3 function based on scipy.integrate.solve_ivp
    # The main equations are, with p_{ao} and its derivatives are unkowns:
    # 1. Q = \frac{p_{lv} - p_{ao}}{R_{ao}}
    # 2. Q_R = \frac{p_{ao}}{R_{circ}}
    # 3. Q_C = C_{circ} \cdot \frac{dp_{ao}}{dt}
    # 4. Q = Q_R + Q_C
    # 5. \frac{dp_{ao}}{dt} = y[1]
    # 6. \frac{d^2p_{ao}}{dt^2} = \frac{Q - Q_R - Q_C}{C_{circ}}
    p_ao = y[0]
    dp_ao_dt = y[1]

    # Calculating flows
    p_lv_interpolated=p_old + (p_current - p_old) * t
    Q = (p_lv_interpolated - p_ao) / R_ao
    Q_R = (p_ao-p_dia) / R_circ
    Q_C = C_circ * dp_ao_dt

    # Conservation of flow
    dQ_C_dt = (Q - Q_R - Q_C) / C_circ
    d2p_ao_dt2=dQ_C_dt

    return [dp_ao_dt, d2p_ao_dt2]

def dV_WK3(p_current,tau,R_ao,circ_p_ao,circ_dp_ao):
    p_current_backup=p_current
    circ_solution = solve_ivp(WK3, [0, tau], [circ_p_ao, circ_dp_ao],t_eval=[0, tau])
    if p_current>p_ao:
        circ_p_ao_1=circ_solution.y[0][1]
        Q1=(p_current-circ_p_ao_1)/R_ao
    else:
        Q1=0 
    p_current=p_current*1.01
    circ_solution = solve_ivp(WK3, [0, tau], [circ_p_ao, circ_dp_ao],t_eval=[0, tau])
    if p_current>p_ao:
        circ_p_ao_2=circ_solution.y[0][1]
        Q2=(p_current-circ_p_ao_2)/R_ao
    else:
        Q2=0
    p_current=p_current_backup
    return (Q2-Q1)/(p_current*.01)*tau

def dV_FE(problem):
    """
    Calculating the dV/dP based on FE model. 
    
    :pulse.MechanicsProblem problem:    The mechanics problem containg the infromation on FE model.
    
    """
    #
    #  Backup the problem
    state_backup_dv = problem.state.copy(deepcopy=True)
    lvp_value_backup_dv=get_lvp_from_problem(problem).values()[0]
    #
    #
    lvp=get_lvp_from_problem(problem)
    p_old=lvp.values()[0]
    v_old=get_lvv_from_problem(problem)
    dp0=0.001*p_old
    dp=dp0
    k=0
    flag_solved=False
    while (not flag_solved) and k<20:
        try:
            p_new=p_old+dp
            lvp.assign(p_new)
            problem.solve()
            flag_solved=True
        except pulse.mechanicsproblem.SolverDidNotConverge:
            problem.state.assign(state_backup_dv)
            lvp.assign(lvp_value_backup_dv)
            # problem.solve()
            dp+=dp0
            print(f"Derivation not Converged, increasin the dp to : {dp}")
            k+=1
        
    # pulse.iterate.iterate(dummy_problem, dummy_lvp, p_new, initial_number_of_steps=5)
    v_new=get_lvv_from_problem(problem)
    dVdp=(v_new-v_old)/(p_new-p_old)
    problem.state.assign(state_backup_dv)
    lvp.assign(lvp_value_backup_dv)
    # FIXME: I think we need to solve the problem here too
    # problem.solve()
    return dVdp
    

def get_lvp_from_problem(problem):
    # getting the LV pressure which is assinged as Neumann BC from a Pulse.MechanicsProblem
    return problem.bcs.neumann[0].traction
def get_lvv_from_problem(problem):
    # getting the LV volume from a Pulse.MechanicsProblem and its solution
    return problem.geometry.cavity_volume(u=problem.state.sub(0))

#%%
for t in range(len(delayed_activations[:,0])):
    target_activation.vector()[:] = delayed_activations[t]
    pulse.iterate.iterate(problem, activation, target_activation)
    #### Circulation
    circ_iter=0
    # initial guess for new pressure
    if t==0:
        p_current=p_current*1.01
        circ_p_ao = p_ao
        circ_dp_ao=0
    else:
        p_current=pres[-1]+(pres[-1]-pres[-2])
        
    p_old=pres[-1]
    v_old=vols[-1]
    R=[]
    tol=1e-4*v_old
    while len(R)==0 or (np.abs(R[-1])>tol and circ_iter<20):
        pulse.iterate.iterate(problem, lvp, p_current)
        v_current=get_lvv_from_problem(problem)
        circ_solution = solve_ivp(WK3, [0, tau], [circ_p_ao, circ_dp_ao],t_eval=[0, tau])
        # check the current p_ao vs previous p_ao to open the ao valve
        if circ_solution.y[0][1]>p_ao:
            circ_p_ao_current=circ_solution.y[0][1]
            circ_dp_ao_current=circ_solution.y[1][1]
            Q=(p_current-circ_p_ao_current)/R_ao
        else:
            circ_p_ao_current=circ_p_ao
            circ_dp_ao_current=circ_dp_ao
            Q=0 
        v_fe=v_current
        v_circ=v_old-Q*tau
        R.append(v_fe-v_circ)
        if np.abs(R[-1])>tol:
            dVFE_dP=dV_FE(problem)
            dVCirc_dP = dV_WK3(p_current,tau,R_ao,circ_p_ao_current,circ_dp_ao_current)                
            J=dVFE_dP+dVCirc_dP
            p_current=p_current-R[-1]/J
            circ_iter+=1
    p_current=get_lvp_from_problem(problem).values()[0]
    v_current=get_lvv_from_problem(problem)
    if circ_solution.y[0][1]>p_ao:
        circ_p_ao=circ_solution.y[0][1]
        circ_dp_ao=circ_solution.y[1][1]
        p_ao=circ_p_ao
    vols.append(v_current)
    pres.append(p_current)
    flows.append(Q*tau)
    ao_pres.append(p_ao)
    reults_u, p = problem.state.split(deepcopy=True)
    reults_u.t=t+1
    with dolfin.XDMFFile(outname.as_posix()) as xdmf:
        xdmf.write_checkpoint(reults_u, "u", float(t+1), dolfin.XDMFFile.Encoding.HDF5, True)
    if p_current<0.01:
        break
#%% Saving the results
fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # Create a figure and two subplots
axs[0,0].plot(t_eval_systole, normal_activation_systole)
axs[0,0].set_ylabel('Activation (kPa)')
axs[0,0].set_xlabel('Time (ms)')
axs[0,1].plot(np.array(vols), pres)
axs[0,1].set_ylabel('Pressure (kPa)')
axs[0,1].set_xlabel('Volume (ml)') 
axs[1,0].plot(t_eval_systole[:t+3], flows)
axs[1,0].set_ylabel('Outflow (ml/s)')
axs[1,0].set_xlabel('Time (ms)')
axs[1,1].plot(t_eval_systole[:t+3],pres,label='LV Pressure')
axs[1,1].plot(t_eval_systole[:t+3],ao_pres,label='Aortic Pressure')
axs[1,1].legend()
axs[1,1].set_ylabel('Pressure (kPa)')
axs[1,1].set_xlabel('Time (ms)')
plt.tight_layout()
name = 'plot_' + str(t) + '.png'
plt.savefig(Path(outdir) / name)
plt.close()
with open(Path(outdir) / 'results_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time [ms]', 'Activation [kPa]', 'Volume [ml]', 'LV Pressure [kPa]', 'Aortic Pressure [kPa]', 'Outflow[ml/ms]'])
    for time, activation, vol, pres_val, ao_pres_val, flow in zip(t_eval_systole, normal_activation_systole, vols, pres, ao_pres, flows):
        writer.writerow([time, activation, vol, pres_val,ao_pres_val, flow])
#%%