import subprocess
from concurrent.futures import ThreadPoolExecutor


address1 = "/home/shared/01_results_24_11_27/amax_7_peak_250_AR_5_SR_10_SC_5"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address1}" --aortic_resistance 5 --systematic_resistance 10 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address1}"'

]


address2 = "/home/shared/01_results_24_11_27/amax_7_peak_250_AR_5_SR_15_SC_5"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address2}" --aortic_resistance 5 --systematic_resistance 15 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address2}"'
]

address3 = "/home/shared/01_results_24_11_27/amax_7_peak_250_AR_5_SR_20_SC_5"
commands_processor_3 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address3}" --aortic_resistance 5 --systematic_resistance 20 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address3}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address3}"'
]

address4 = "/home/shared/01_results_24_11_27/amax_7_peak_250_AR_5_SR_25_SC_5"
commands_processor_4 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address4}" --aortic_resistance 5 --systematic_resistance 25 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address4}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address4}"'
]

address5 = "/home/shared/01_results_24_11_27/amax_7_peak_250_AR_5_SR_30_SC_5"
commands_processor_5 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address5}" --aortic_resistance 5 --systematic_resistance 30 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address5}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address5}"'
]


address6 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_10_SC_5"
commands_processor_6 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address6}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 10 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address6}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address6}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address6}"'

]


address7 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_15_SC_5"
commands_processor_7 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address7}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 15 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address7}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address7}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address7}"'
]

address8 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_20_SC_5"
commands_processor_8 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address8}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 20 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address8}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address8}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address8}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address8}"'
]

address9 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_25_SC_5"
commands_processor_9 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address9}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 25 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address9}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address9}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address9}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address9}"'
]

address10 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_30_SC_5"
commands_processor_10 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address10}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 30 --systematic_compliance 5',
    f'python3 TugOfWar/post_processing.py --data_folder "{address10}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address10}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address10}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address10}"'
]

address11 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_20_SC_1"
commands_processor_11 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address11}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 20 --systematic_compliance 1',
    f'python3 TugOfWar/post_processing.py --data_folder "{address11}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address11}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address11}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address11}"'
]

address12 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_25_SC_3"
commands_processor_12 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address12}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 25 --systematic_compliance 3',
    f'python3 TugOfWar/post_processing.py --data_folder "{address12}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address12}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address12}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address12}"'
]

address13 = "/home/shared/01_results_24_11_27/amax_5_peak_250_AR_5_SR_30_SC_7"
commands_processor_13= [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address13}" --activation_mode rate --activation_variation 5 --aortic_resistance 5 --systematic_resistance 30 --systematic_compliance 7',
    f'python3 TugOfWar/post_processing.py --data_folder "{address13}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address13}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address13}" -o 72_6 -p 0.001',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  -f "{address13}"'
]
# Function to run commands sequentially in each processor
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Run each set of commands in parallel with up to 6 processors
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [
        executor.submit(run_commands, commands_processor_1),
        executor.submit(run_commands, commands_processor_2),
        executor.submit(run_commands, commands_processor_3),
        executor.submit(run_commands, commands_processor_4),
        executor.submit(run_commands, commands_processor_5),
        executor.submit(run_commands, commands_processor_6),
        executor.submit(run_commands, commands_processor_7),
        executor.submit(run_commands, commands_processor_8),
        executor.submit(run_commands, commands_processor_9),
        executor.submit(run_commands, commands_processor_10),
        executor.submit(run_commands, commands_processor_11),
        executor.submit(run_commands, commands_processor_12),
    ]

    # Wait for all futures to complete
    for future in futures:
        future.result()
        
print("All processes completed.")