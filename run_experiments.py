import subprocess
from concurrent.futures import ThreadPoolExecutor

s_values = [
    # "single_compartment",
    "homogenous_compartment",
    #"heterogenous_compartment"
]

activation_modes = [
    "delay", "diastole_time", "systole_time", "decay"
]

activation_variations = [0.01, 0.03, 0.05]

base_outdir = "01_results_24_08_29"

def run_experiment(s, activation_mode, activation_variation):
    outdir = f"{base_outdir}/{s}/{activation_mode}_{int(activation_variation * 1000)}"
    cmd = [
        "python3", "/home/shared/TugOfWar/tug_of_war.py",
        "-m", ".5",
        "-c", "72",
        "-l", "6",
        "-s", s,
        "-p", "activation",
        "--activation_mode", activation_mode,
        "--activation_variation", str(activation_variation),
        "-o", outdir
    ]
    subprocess.run(cmd)

with ThreadPoolExecutor(max_workers=6) as executor:
    for s in s_values:
        for activation_mode in activation_modes:
            for activation_variation in activation_variations:
                executor.submit(run_experiment, s, activation_mode, activation_variation)

