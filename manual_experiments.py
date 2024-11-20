import subprocess
from concurrent.futures import ThreadPoolExecutor


address1 = "/home/shared/01_results_24_11_21/Infarct_mid_200"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address1}" -mi --mi_stiffness 200 -micomp --infarct_comp 157 158 159 160 161 162 163 164 165 166',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.03',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  --data_folder "{address1}"'
]

address2 = "/home/shared/01_results_24_11_21/Infarct_mid_50"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address2}" -mi --mi_stiffness 50 -micomp --infarct_comp 157 158 159 160 161 162 163 164 165 166',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.03',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  --data_folder "{address2}"'
]

address3 = "/home/shared/01_results_24_11_21/Infarct_apex_200"
commands_processor_3 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address3}" -mi --mi_stiffness 200 -micomp --infarct_comp 301 302 303 304 305 306 307 308 309 310 311',
    f'python3 TugOfWar/post_processing.py --data_folder "{address3}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address3}" -o 72_6 -p 0.03',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  --data_folder "{address3}"'
]

address4 = "/home/shared/01_results_24_11_21/Infarct_apex_50"
commands_processor_4 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address4}" -mi --mi_stiffness 50 -micomp --infarct_comp 301 302 303 304 305 306 307 308 309 310 311',
    f'python3 TugOfWar/post_processing.py --data_folder "{address4}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address4}" -o 72_6 -p 0.03',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  --data_folder "{address4}"'
]

address5 = "/home/shared/01_results_24_11_21/Normal"
commands_processor_5 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address5}" ',
    f'python3 TugOfWar/post_processing.py --data_folder "{address5}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address5}" -o 72_6 -p 0.03',
    f'python3 TugOfWar/mi_post_processing.py -s 1 2 3 4 5 6  --data_folder "{address5}"'
]

# Function to run commands sequentially in each processor
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Run each set of commands in parallel with up to 6 processors
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [
        executor.submit(run_commands, commands_processor_1),
        executor.submit(run_commands, commands_processor_2),
        executor.submit(run_commands, commands_processor_3),
        executor.submit(run_commands, commands_processor_4),
        executor.submit(run_commands, commands_processor_5),
#        executor.submit(run_commands, commands_processor_6),
#        executor.submit(run_commands, commands_processor_7),
#        executor.submit(run_commands, commands_processor_8),
    ]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("All processes completed.")

