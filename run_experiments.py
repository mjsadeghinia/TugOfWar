# import subprocess
# from concurrent.futures import ThreadPoolExecutor

# s_values = [
#     # "single_compartment",
#     "homogenous_compartment",
#     #"heterogenous_compartment"
# ]

# activation_modes = [
#     "delay", "diastole_time", "systole_time", "decay"
# ]

# activation_variations = [0.01, 0.03, 0.05]

# base_outdir = "01_results_24_08_29"

# def run_experiment(s, activation_mode, activation_variation):
#     outdir = f"{base_outdir}/{s}/{activation_mode}_{int(activation_variation * 1000)}"
#     cmd = [
#         "python3", "/home/shared/TugOfWar/tug_of_war.py",
#         "-m", ".5",
#         "-c", "72",
#         "-l", "6",
#         "-s", s,
#         "-p", "activation",
#         "--activation_mode", activation_mode,
#         "--activation_variation", str(activation_variation),
#         "-o", outdir
#     ]
#     subprocess.run(cmd)

# with ThreadPoolExecutor(max_workers=6) as executor:
#     for s in s_values:
#         for activation_mode in activation_modes:
#             for activation_variation in activation_variations:
#                 executor.submit(run_experiment, s, activation_mode, activation_variation)

import subprocess
from concurrent.futures import ThreadPoolExecutor

mi_stiffness = [0, 50, 200]
mi_severity = [1, 0.5, 0]
mi_center = "(-4.10805,-4.48492e-16,-0.768866)"
base_outdir = "/home/shared/01_results_24_10_30_apex"

def run_experiment(mi_stiffness, mi_severity):
    outdir = f"{base_outdir}/Severity_{int(mi_severity * 100)}_Stiffness_{mi_stiffness}"
    cmd = [
        "python3", "/home/shared/TugOfWar/tug_of_war.py",
        "-ep",
        "-mi",
        "--mi_severity", str(mi_severity),
        "--mi_stiffness", str(mi_stiffness),
        "--mi_center", mi_center,
        "-o", outdir,
        "--epdir", "/home/shared/01_results_24_10_30/EP_data"
    ]
    subprocess.run(cmd)

with ThreadPoolExecutor(max_workers=8) as executor:
    for st in mi_stiffness:
        for sv in mi_severity:
            executor.submit(run_experiment, st, sv)

