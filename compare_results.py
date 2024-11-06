from pathlib import Path
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.cm as cm
import numpy as np
import utils

def generate_color_map(results_dir, folder_list=None):
    """
    Generate a color map based on the folders in results_dir or a provided list of folders,
    using the 'jet' colormap.
    
    Args:
        results_dir (str): Path to the directory containing the folders.
        folder_list (list, optional): List of folder names to use for generating the color map.
    
    Returns:
        dict: A dictionary mapping folder names to colors.
    """
    # Determine the folders to use
    folders = folder_list if folder_list else [f.name for f in Path(results_dir).iterdir() if f.is_dir()]
    
    # Generate the jet colormap and sample colors based on the number of folders
    cmap = plt.get_cmap("Spectral")
    colors = [cmap(i / (len(folders) - 1)) for i in range(len(folders))]
    
    # Map each folder to a color
    color_map = {folder: colors[i] for i, folder in enumerate(folders)}
    
    return color_map

def get_experiment_data(results_dir, selected_experiments=None):
    """Fetch data from each experiment folder, optionally filtering by selected experiments."""
    experiments_data = {}
    for folder_path in Path(results_dir).iterdir():
        if folder_path.is_dir() and (selected_experiments is None or folder_path.name in selected_experiments):
            csv_path = folder_path / "results_data.csv"
            if csv_path.is_file():
                with open(csv_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader)  # Skip header row
                    volume = []
                    pressure_kpa = []
                    for row in reader:
                        volume.append(float(row[2]))  # 3rd column: Volume in ml
                        pressure_kpa.append(float(row[3]))  # 4th column: Pressure in kPa
                    experiments_data[folder_path.name] = (volume, pressure_kpa)
    return experiments_data

def get_EF_ToWi(folder_path):
    """Fetch ejection fraction and tug-of-war index data from the specified files."""
    additional_data = []
    sub_folder = folder_path / "72_6"
    if not sub_folder.is_dir():
        return additional_data
    
    for p in ["0.01", "0.02", "0.03"]:
        for suffix in ["", "_circ"]:
            filename = f"00_tow_index_{p}{suffix}.csv"
            file_path = sub_folder / filename
            if file_path.is_file():
                with open(file_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    header = next(reader)
                    data = next(reader)
                    ejection_fraction = float(data[0])  # First column of the header row
                    tow_index = float(data[1])  # Second column of the data row
                    additional_data.append((ejection_fraction, tow_index, p, suffix))
    return additional_data

def plot_pressure_volume(experiments_data, color_map, save_path="pressure_volume_plot.png"):
    """Plot pressure-volume data with dual y-axis for pressure in kPa and mmHg, and save the plot."""
    fig, ax1 = plt.subplots(figsize=(10, 10))
    
    # Configure the first y-axis (kPa)
    ax1.set_xlabel("Volume (ml)")
    ax1.set_ylabel("Pressure (kPa)", color="black")
    ax1.grid(True)
    
    # Configure the second y-axis (mmHg)
    ax2 = ax1.twinx()
    ax2.set_ylabel("Pressure (mmHg)", color="black")
    
    # Plot each experiment's data
    for exp_name, (volume, pressure_kpa) in experiments_data.items():
        color = color_map.get(exp_name, "black")
        pressure_mmhg = [p * 7.50062 for p in pressure_kpa]  # Convert kPa to mmHg
        
        ax1.plot(volume, pressure_kpa, label=exp_name, color=color)
        ax2.plot(volume, pressure_mmhg, linestyle="--", color=color, alpha = 0)
    
    # Place legend outside the plot, below the title
    fig.legend(loc="upper center", bbox_to_anchor=(0.5, .95), ncol=5, title="Experiments")
    
    # Save the plot
    plt.savefig(save_path, bbox_inches="tight")
    plt.show()

def plot_ejection_fraction_tow_index(results_dir, experiments_data, color_map, selected_folders=None, outname = "ejection_fraction_tow_index_plot.png"):
    """Plot ejection fraction vs. tug-of-war index for each experiment."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlabel("Ejection Fraction (%)")
    ax.set_ylabel("Tug-of-War Index")
    ax.grid(True)

    shape_map = {"0.01": "s", "0.02": "^", "0.03": "o"}  # Square, Triangle, Circle

    # Plot each experiment's additional data
    for exp_name in experiments_data.keys():
        if selected_folders and exp_name not in selected_folders:
            continue
        
        color = color_map.get(exp_name, "black")
        folder_path = Path(results_dir) / exp_name
        additional_data = get_EF_ToWi(folder_path)
        print(f"{exp_name}:")
        print(f"{additional_data}")
        print("--------------------")
        # breakpoint()
        for ejection_fraction, tow_index, p, suffix in additional_data:
            marker = shape_map.get(p, "o")
            fill_style = "none" if suffix == "_circ" else "full"
            ax.scatter(
                ejection_fraction, tow_index, label=f"{exp_name} p={p} {suffix}",
                color=color, marker=marker, edgecolors=color, facecolors=color if fill_style == "full" else "none"
            )

    # Customize legend to avoid too many repeated entries
    handles = [mlines.Line2D([], [], color='black', marker=shape, linestyle="None", markersize=10,
                             label=f"{p} {'' if filled else 'circ'}",
                             markerfacecolor='black' if filled else "none", markeredgecolor='black')
               for p, shape in shape_map.items()
               for filled in [True, False]]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=6, title="Prominence Value & Fiber vs. Circ. strain")

    # Save the plot
    plt.savefig(outname, bbox_inches="tight")
    plt.show()

def main():
    results_dir = "/home/shared/01_results_24_11_06"
    color_map = generate_color_map(results_dir)
    # breakpoint()
    selected_experiments = ['0_fibers90', '0_fibers-60 ','0_fibers-30', '0_fibers0']
    # color_map_level_0 = generate_color_map(results_dir, folder_list=selected_experiments)
    save_path = 'PV_level_0.png'
    experiments_data = get_experiment_data(results_dir, selected_experiments)
    plot_pressure_volume(experiments_data, color_map, save_path)
    plot_ejection_fraction_tow_index(results_dir, experiments_data, color_map, selected_folders=selected_experiments, outname="EF_tow_level_0")

    selected_experiments = ['1_ep', '0_fibers-30']
    # color_map_level_1_1 = generate_color_map(results_dir, folder_list=selected_experiments)
    save_path = 'PV_level_1_1.png'
    experiments_data = get_experiment_data(results_dir, selected_experiments)
    plot_pressure_volume(experiments_data, color_map, save_path)
    plot_ejection_fraction_tow_index(results_dir, experiments_data, color_map, selected_folders=selected_experiments, outname="EF_tow_level_1_1")

    selected_experiments = ['0_fibers-30', '0_fibers-60 ', '1_fibers-30to30' , '1_fibers-60to60']
    # color_map_level_1_1 = generate_color_map(results_dir, folder_list=selected_experiments)
    save_path = 'PV_level_1_2.png'
    experiments_data = get_experiment_data(results_dir, selected_experiments)
    plot_pressure_volume(experiments_data, color_map, save_path)
    plot_ejection_fraction_tow_index(results_dir, experiments_data, color_map, selected_folders=selected_experiments, outname="EF_tow_level_1_2")

    
    selected_experiments = ['0_fibers-30', '1_ep',  '1_fibers-60to60' , '2_fibers-30to30_ep']
    # color_map_level_1_1 = generate_color_map(results_dir, folder_list=selected_experiments)
    save_path = 'PV_level_2.png'
    experiments_data = get_experiment_data(results_dir, selected_experiments)
    plot_pressure_volume(experiments_data, color_map, save_path)
    plot_ejection_fraction_tow_index(results_dir, experiments_data, color_map, selected_folders=selected_experiments, outname="EF_tow_level_2")

    
    

    
    
    # plot_ejection_fraction_tow_index(results_dir, experiments_data, color_map, selected_folders=selected_experiments)

if __name__ == "__main__":
    main()
    
# ['0_fibers90', '0_fibers+60', '2_fibers-30to30_ep', '1_ep_git-', '1_fibers-30to30', '1_ep_git+', '1_ep', '0_fibers0', '1_ep_gil+', '1_fibers-60to60', '1_ep_gil-', '0_fibers-60 ', '0_fibers+30']