from pathlib import Path
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Define the base directory containing the folders
base_directory = Path('/home/shared/01_results_24_11_14')

# Define a function to create commands for a specific folder
def create_commands(address):
    return [
        f'python3 TugOfWar/post_processing.py --data_folder "{address}" -o 72_6',
        f'python3 TugOfWar/peak_detection.py --data_folder "{address}" -o 72_6 -p 0.01',
        # f'python3 TugOfWar/peak_detection.py --data_folder "{address}" -o 72_6 -p 0.02',
        f'python3 TugOfWar/peak_detection.py --data_folder "{address}" -o 72_6 -p 0.03'
    ]

# Function to run commands sequentially in each processor
def run_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True, check=True)

# List all folders in the base directory
folders = [folder for folder in base_directory.iterdir() if folder.is_dir()]

# Run each set of commands in parallel with up to 2 processors
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(run_commands, create_commands(folder)) for folder in folders]

    # Wait for all futures to complete
    for future in futures:
        future.result()

print("All processes completed.")
