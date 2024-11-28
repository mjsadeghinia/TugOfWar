import subprocess
from concurrent.futures import ThreadPoolExecutor


address1 = "/home/shared/01_results_24_11_28/0_fibers_n30"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address1}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.001',
    # f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address1}" -p 0.001'
]

address2 = "/home/shared/01_results_24_11_28/1_fibers_n30to30"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address2}" --fiber_angle_endo -30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.001',
    # f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address2}" -p 0.001'
]

address3 = "/home/shared/01_results_24_11_28/1_fibers_n60to60"
commands_processor_3 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address3}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address3}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.001',
    # f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address3}" -p 0.001'
]

address4 = "/home/shared/01_results_24_11_28/1_ep_fibers_n30"
commands_processor_4 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address4}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address4}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address4}" -p 0.001'
]


address5 = "/home/shared/01_results_24_11_28/2_fibers-60to60_ep"
commands_processor_5 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address5}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address5}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address5}" -p 0.001'
]

address6 = "/home/shared/01_results_24_11_28/0_fibers_n60"
commands_processor_6 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address6}" --fiber_angle_endo 60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address6}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.001',
    # f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address6}" -p 0.001'
]


address7 = "/home/shared/01_results_24_11_28/1_ep_fibers_n60"
commands_processor_7 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address7}" --fiber_angle_endo 60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address7}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address7}" -p 0.001'
]

address8 = "/home/shared/01_results_24_11_28/0_fibers_0"
commands_processor_8 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address8}" --fiber_angle_endo 0 --fiber_angle_epi 0',
    f'python3 TugOfWar/post_processing.py --data_folder "{address8}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address8}" -o 72_6 -p 0.001',
    # f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address8}" -p 0.001'
]

address9 = "/home/shared/01_results_24_11_28/0_fibers_90"
commands_processor_9 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address9}" --fiber_angle_endo 90 --fiber_angle_epi 90',
    f'python3 TugOfWar/post_processing.py --data_folder "{address9}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address9}" -o 72_6 -p 0.001',
    # f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address9}" -p 0.001'
]

# Function to run commands sequentially
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Define grouped commands to run in series
command_groups = [
    commands_processor_1 + commands_processor_2,
    commands_processor_3 + commands_processor_4,
    commands_processor_5 + commands_processor_6,
    commands_processor_7 + commands_processor_8,
    commands_processor_9
]

# Run grouped commands in parallel with up to 4 workers (each runs 2 sets of commands in series)
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(run_commands, group) for group in command_groups]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("All processes completed.")
