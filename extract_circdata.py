import os
import argparse
import numpy as np
import csv

def extract_circ_results(fname):
    data = np.loadtxt(fname, delimiter=",", skiprows=1)
    ejection_indices = np.where(data[:, 5] > 0.0)[0]
    
    # MVO and MVC is found based on ejection (outflow)
    AVO_index = ejection_indices[0]
    AVC_index = ejection_indices[-1]
    mid_ejection_ind = ejection_indices[int(len(ejection_indices) / 2)]

    # MVO and MVC is found based on atrium pressure with threshold of 1kpa
    MVC_index = np.min(np.where(data[:, 3] > 1)[0])
    MVO_index = np.max(np.where(data[AVC_index:, 3] < 1)[0]) + AVC_index

    EDV = data[AVO_index - 1, 2]
    ESV = data[AVC_index + 1, 2]
    ejection_fraction = (EDV - ESV) / EDV

    valve_timings = {
        "AVO_index": AVO_index,
        "AVC_index": AVC_index,
        "MVO_index": MVO_index,
        "MVC_index": MVC_index,
        "mid_ejection_ind": mid_ejection_ind
    }
    
    return (
        ejection_fraction,
        valve_timings
    )

def process_directory(input_dir, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Experiment", "EF", "MVC_index", "AVO_index", "AVC_index", "MVO_index", "IVC", "IVR"])
        
        for folder_name in os.listdir(input_dir):
            folder_path = os.path.join(input_dir, folder_name)
            if os.path.isdir(folder_path):
                result_file = os.path.join(folder_path, "results_data.csv")
                if os.path.isfile(result_file):
                    try:
                        ef, timings = extract_circ_results(result_file)
                        ivc = timings['AVO_index'] - timings['MVC_index']
                        ivr = timings['MVO_index'] - timings['AVC_index']
                        writer.writerow([folder_name, ef, timings['MVC_index'], timings['AVO_index'], timings['AVC_index'], timings['MVO_index'], ivc, ivr])
                    except Exception as e:
                        print(f"Error processing {result_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Process results_data.csv files in subdirectories.")
    parser.add_argument("--input_dir", default="/home/shared/01_results_24_11_14", type=str, help="Directory containing subdirectories with results_data.csv")
    parser.add_argument("--output_file", default="/home/shared/01_results_24_11_14_compare/timings.csv", type=str, help="Output CSV file path")
    args = parser.parse_args()

    process_directory(args.input_dir, args.output_file)

if __name__ == "__main__":
    main()
