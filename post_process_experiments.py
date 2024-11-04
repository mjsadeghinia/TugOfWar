import subprocess
from concurrent.futures import ThreadPoolExecutor

s_values = [
    # "single_compartment",
    # "homogenous_compartment",
    "heterogenous_compartment"
]

activation_modes = [
    "delay", "diastole_time",
    # "systole_time", "decay"
]


mi_stiffness = [0, 50, 200]
mi_severity = [1, 0.5, 0]


activation_variations = [0.01, 0.03, 0.05]

# num_circ_segments = [9, 27, 45, 72, 90]
num_circ_segments = [72]
num_long_segments = [6]
prominence = 0.03

base_outdir = "/home/shared/01_results_24_10_30_apex"

def post_process_experiment(mi_stiffness, mi_severity, num_circ_segments, num_long_segments):
    data_folder = f"{base_outdir}/Severity_{int(mi_severity * 100)}_Stiffness_{mi_stiffness}"
    outdir = f"{num_circ_segments}_{num_long_segments}"
    cmd = [
        "python3", "/home/shared/TugOfWar/post_processing.py",
        "--data_folder", data_folder,
        "--outdir", outdir,
        "--num_circ_segments",f"{num_circ_segments}",
        "--num_long_segments",f"{num_long_segments}",
    ]
    subprocess.run(cmd)
    
def peak_detection_experiment(mi_stiffness, mi_severity, num_circ_segments, num_long_segments, prominence):
    data_folder = f"{base_outdir}/Severity_{int(mi_severity * 100)}_Stiffness_{mi_stiffness}"
    outdir = f"{num_circ_segments}_{num_long_segments}"
    cmd = [
        "python3", "/home/shared/TugOfWar/peak_detection.py",
        "--data_folder", data_folder,
        "--outdir", outdir,
        "-p",f"{prominence}",
    ]
    subprocess.run(cmd)

# with ThreadPoolExecutor(max_workers=8) as executor:
#     for s in s_values:
#         for activation_mode in activation_modes:
#             for activation_variation in activation_variations:
                # for c in num_circ_segments:
                #     for l in num_long_segments:
#                         executor.submit(post_process_experiment, s, activation_mode, activation_variation, c, l)


# with ThreadPoolExecutor(max_workers=8) as executor:
#     for s in s_values:
#         for activation_mode in activation_modes:
#             for activation_variation in activation_variations:
#                 for c in num_circ_segments:
#                     for l in num_long_segments:
#                         executor.submit(peak_detection_experiment, s, activation_mode, activation_variation, c, l, prominence)

with ThreadPoolExecutor(max_workers=9) as executor:
    for st in mi_stiffness:
        for sv in mi_severity:
            for c in num_circ_segments:
                    for l in num_long_segments:
                        executor.submit(post_process_experiment, st, sv, c, l)

with ThreadPoolExecutor(max_workers=9) as executor:
    for st in mi_stiffness:
        for sv in mi_severity:
            for c in num_circ_segments:
                    for l in num_long_segments:
                        executor.submit(peak_detection_experiment, st, sv, c, l, prominence)
