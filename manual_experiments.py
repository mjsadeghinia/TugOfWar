import subprocess
from concurrent.futures import ThreadPoolExecutor


address1 = "/home/shared/01_results_24_11_27/amin_n11_amax_7_peak_250_AR_5_SR_25_SC_5"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address1}" --activation_mode decay --activation_variation -11',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address1}" -p 0.001'
]

address2 = "/home/shared/01_results_24_11_27/amin_n13_amax_7_peak_250_AR_5_SR_25_SC_5"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address2}" --activation_mode decay --activation_variation -13',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address2}" -p 0.001'
]

address3 = "/home/shared/01_results_24_11_27/amin_n15_amax_7_peak_250_AR_5_SR_25_SC_5"
commands_processor_3 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address3}" --activation_mode decay --activation_variation -15',
    f'python3 TugOfWar/post_processing.py --data_folder "{address3}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address3}" -p 0.001'
]

address4 = "/home/shared/01_results_24_11_27/amin_n17_amax_10_peak_250_AR_5_SR_25_SC_5"
commands_processor_4 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address4}" --activation_mode decay --activation_variation -17',
    f'python3 TugOfWar/post_processing.py --data_folder "{address4}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address4}" -p 0.001'
]


address5 = "/home/shared/01_results_24_11_27/amin_n15_amax_7_peak_250_AR_5_SR_20_SC_5"
commands_processor_5 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address5}" --activation_mode decay --activation_variation -15 --systematic_resistance 20',
    f'python3 TugOfWar/post_processing.py --data_folder "{address5}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address5}" -p 0.001'
]

address6 = "/home/shared/01_results_24_11_27/amin_n15_amax_7_peak_250_AR_5_SR_30_SC_5"
commands_processor_6 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address6}" --activation_mode decay --activation_variation -15 --systematic_resistance 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address6}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address6}" -p 0.001'
]


address7 = "/home/shared/01_results_24_11_27/amin_n15_amax_7_peak_250_AR_5_SR_25_SC_10"
commands_processor_7 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address7}" --activation_mode decay --activation_variation -15 --systematic_compliance 10',
    f'python3 TugOfWar/post_processing.py --data_folder "{address7}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address7}" -p 0.001'
]

address8 = "/home/shared/01_results_24_11_27/amin_n30_amax_7_peak_250_AR_5_SR_25_SC_8"
commands_processor_8 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address8}" --activation_mode decay --activation_variation -15 --systematic_compliance 8',
    f'python3 TugOfWar/post_processing.py --data_folder "{address8}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address8}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address8}" -p 0.001'
]

# Function to run commands sequentially in each processor
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Run each set of commands in parallel with up to 6 processors
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(run_commands, commands_processor_1),
        executor.submit(run_commands, commands_processor_2),
        executor.submit(run_commands, commands_processor_3),
        # executor.submit(run_commands, commands_processor_4),
        # executor.submit(run_commands, commands_processor_5),
        # executor.submit(run_commands, commands_processor_6),
        # executor.submit(run_commands, commands_processor_7),
        executor.submit(run_commands, commands_processor_8),
    ]

    # Wait for all futures to complete
    for future in futures:
        future.result()
        
print("All processes completed.")