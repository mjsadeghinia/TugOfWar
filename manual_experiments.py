import subprocess
from concurrent.futures import ThreadPoolExecutor

# Define the command sequences for each processor with unique addresses
address1 = "/home/shared/01_results_24_11_06/1_ep"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address1}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.03'
]

address2 = "/home/shared/01_results_24_11_06/1_ep_gil-"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address2}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.03'
]

address3 = "/home/shared/01_results_24_11_06/1_ep_gil+"
commands_processor_3 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address3}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address3}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.03'
]

address4 = "/home/shared/01_results_24_11_06/1_ep_git-"
commands_processor_4 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address4}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address4}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.03'
]

address5 = "/home/shared/01_results_24_11_06/1_ep_git+"
commands_processor_5 = [
    f'python3 TugOfWar/ep_create_geo.py -o "{address5}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/ep_solver.py -o "{address5}"',
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address5}" --fiber_angle_endo 30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address5}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.03'
]

address6 = "/home/shared/01_results_24_11_06/1_fibers-30to30"
commands_processor_6 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address6}" --fiber_angle_endo -30 --fiber_angle_epi 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address6}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.03'
]



address7 = "/home/shared/01_results_24_11_06/1_fibers-60to60"
commands_processor_7 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address7}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address7}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.03'
]


address8 = "/home/shared/01_results_24_11_06/0_fibers-30"
commands_processor_8 = [
    f'python3 TugOfWar/tug_of_war.py -o "{address8}" --fiber_angle_endo 30 --fiber_angle_epi 3-0',
    f'python3 TugOfWar/post_processing.py --data_folder "{address8}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address8}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address8}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address8}" -o 72_6 -p 0.03'
]

address9 = "/home/shared/01_results_24_11_06/2_fibers-60to60_ep"
commands_processor_9 = [
#    f'python3 TugOfWar/ep_create_geo.py -o "{address9}" --fiber_angle_endo -60 --fiber_angle_epi 60',
#    f'mpirun -n 8 python3 TugOfWar/ep_solver.py -ep -o "{address9}" ',
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address9}" --fiber_angle_endo -60 --fiber_angle_epi 60',
    f'python3 TugOfWar/post_processing.py --data_folder "{address9}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address9}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address9}" -o 72_6 -p 0.02',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address9}" -o 72_6 -p 0.03'
]


# Function to run commands sequentially in each processor
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Run each set of commands in parallel with up to 6 processors
with ThreadPoolExecutor(max_workers=1) as executor:
    futures = [
        executor.submit(run_commands, commands_processor_9),
    ]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("All processes completed.")

