import subprocess
from concurrent.futures import ThreadPoolExecutor


address1 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR35_SC5_MI_200_apex"
commands_processor_1 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address1}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 35 --systematic_compliance 5 -mi --mi_stiffness 200 --mi_center "(-3.84297,-8.80244e-17,1.28115)" --iz_radius 0.6',
    f'python3 TugOfWar/post_processing.py --data_folder "{address1}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address1}" -o 72_6 -p 0.03'
]


address2 = "/home/shared/01_results_24_11_14/decay_-070_rate_-020_AR5_SR35_SC5_MI_50_apex"
commands_processor_2 = [
    f'python3 TugOfWar/tug_of_war.py -ep -o "{address2}" --activation_mode rate --activation_variation -0.2 --aortic_resistance 5 --systematic_resistance 35 --systematic_compliance 5 -mi --mi_stiffness 50 --mi_center "(-3.84297,-8.80244e-17,1.28115)" --iz_radius 0.6',
    f'python3 TugOfWar/post_processing.py --data_folder "{address2}" -o 72_6',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.01',
    f'python3 TugOfWar/peak_detection.py --data_folder "{address2}" -o 72_6 -p 0.03'
]


# Function to run commands sequentially in each processor
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# Run each set of commands in parallel with up to 6 processors
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [
        executor.submit(run_commands, commands_processor_1),
        executor.submit(run_commands, commands_processor_2),
#        executor.submit(run_commands, commands_processor_3),
#        executor.submit(run_commands, commands_processor_4),
#        executor.submit(run_commands, commands_processor_5),
#        executor.submit(run_commands, commands_processor_6),
#        executor.submit(run_commands, commands_processor_7),
#        executor.submit(run_commands, commands_processor_8),
    ]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("All processes completed.")

