import subprocess
from concurrent.futures import ThreadPoolExecutor

address1 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR30"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address1}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 30',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.03'
]


address2 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR35"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address2}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 35',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.03'
]


address3 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR25_SC1"
commands_processor_3 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address3}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 25 --systematic_compliance 1',
    f'python3 TugOfWar/post_processing.py --data_folder "{address3}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.03'
]

address4 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR25_SC5"
commands_processor_4 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address4}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 25 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address4}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.03'
]

address5 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR25_SC15"
commands_processor_5 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address5}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 25 --systematic_compliance 15',
    f'python3 TugOfWar/post_processing.py --data_folder "{address5}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.03'
]


address6 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR25_SC20"
commands_processor_6 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address6}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 25 --systematic_compliance 20',
    f'python3 TugOfWar/post_processing.py --data_folder "{address6}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.03'
]



# Function to run commands sequentially in each processor
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Run each set of commands in parallel with up to 6 processors
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = [
        executor.submit(run_commands, commands_processor_1),
        executor.submit(run_commands, commands_processor_2),
        executor.submit(run_commands, commands_processor_3),
        executor.submit(run_commands, commands_processor_4),
        executor.submit(run_commands, commands_processor_5),
        executor.submit(run_commands, commands_processor_6),
    ]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("All processes completed.")
