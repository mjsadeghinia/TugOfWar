import subprocess
from concurrent.futures import ThreadPoolExecutor


address1 = "/home/shared/01_results_25_03_17/3_fibers-60to60_ep_rn_amin_sigma"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -rn -ep -o "{address1}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.01',
]

address2 = "/home/shared/01_results_25_03_17/3_fibers-60to60_ep_rn_tsys_amin_sigma"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -rn -ep -o "{address2}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.01',
]

address3 = "/home/shared/01_results_25_03_17/3_fibers-60to60_ep_rn_tsys"
commands_processor_3 = [
    f'python3 TugOfWar/tug_of_war.py -rn -ep -o "{address3}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address3}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.01',
]

address4 = "/home/shared/01_results_25_03_17/3_fibers-60to60_ep_rn_tsys_amin_sigma_comp"
commands_processor_4 = [
    f'python3 TugOfWar/tug_of_war.py -crn -rn -ep -o "{address4}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address4}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.01',
]

address5 = "/home/shared/01_results_25_03_17/3_fibers-60to60_ep_rn_tsys_amin_sigma_comp_05"
commands_processor_5 = [
    f'python3 TugOfWar/tug_of_war.py -crn -rn -ep -o "{address5}" --fiber_angle_endo -60 --fiber_angle_epi 60 --crn_std 0.05',
    f'python3 TugOfWar/post_processing.py --data_folder "{address5}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.01',
]

address6 = "/home/shared/01_results_25_03_17/3_fibers-60to60_ep_rn_tsys_amin_sigma_comp_02"
commands_processor_6 = [
    f'python3 TugOfWar/tug_of_war.py -crn -rn -ep -o "{address6}" --fiber_angle_endo -60 --fiber_angle_epi 60 --crn_std 0.02',
    f'python3 TugOfWar/post_processing.py --data_folder "{address6}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.01',
]


address7 = "/home/shared/01_results_25_03_17/2_fibers-60to60_ep"
commands_processor_7 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address7}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address7}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.01',
]


# Function to run commands sequentially
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Define grouped commands to run in series
command_groups = [
    # commands_processor_1,
    # commands_processor_2,
    # commands_processor_3,
    #commands_processor_4,
    commands_processor_5,
    commands_processor_6,
    commands_processor_7
]

# Run grouped commands in parallel with up to 4 workers (each runs 2 sets of commands in series)
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(run_commands, group) for group in command_groups]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("All processes completed.")