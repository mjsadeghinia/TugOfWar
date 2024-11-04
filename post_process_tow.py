from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import argparse


#%%
s_values = [
    # "single_compartment",
    # "homogenous_compartment",
    "heterogenous_compartment"
]

activation_modes = [
    # "delay", 
    "diastole_time",
    # "systole_time", "decay"
]

mi_stiffness = [0, 50, 200]
mi_severity = [1, 0.5, 0]

activation_variations = [0.01, 0.03, 0.05]

# num_circ_segments = [9, 27, 45, 72, 90]
num_circ_segments = [72]
num_long_segments = [6]
prominence = 0.03

base_outdir = "/home/shared/01_results_24_10_30_apex"

#%%
def plot_EF_tow(ax, data, s, activation_mode, activation_variation):
        # Define marker style for each activation_mode
    colors = {
        "delay": "red",
        "diastole_time": "orange",
        "systole_time": "blue",
        "decay": "green"
    }
    # Define colors for activation_variations
    marker_styles = {
        0.01: "v",
        0.03: "<",
        0.05: "^"
    }
    marker = marker_styles.get(activation_variation, "o")  # Default marker if not found
    color = colors.get(activation_mode, "blue")   # Default color if not found
    # Determine fill style based on the compartment type
    if "homogenous" in s:
        facecolors = 'none'  # Hollow markers for homogeneous
    else:
        facecolors = color   # Filled markers for heterogeneous
    name = f"{activation_mode}_{activation_variation}"
    ax.scatter(
        data[0], data[1], 
        label=name, 
        color=color, 
        marker=marker, 
        facecolors=facecolors, 
        edgecolors=color
    )
    return ax

def plot_EF_tow_mi_stiffness(ax, data, st):
    # Define marker style for each activation_mode
    colors = {
        200: "red",
        50: "orange",
        0: "green"
    }

    color = colors.get(st, "blue")   # Default color if not found
    name = f"{st}% Stiffer IZ"
    ax.scatter(
        data[0], data[1], 
        label=name, 
        color=color, 
        edgecolors=color
    )
    return ax

def plot_comp_tow(ax, data, s, activation_mode, activation_variation,c, l):
        # Define marker style for each activation_mode
    colors = {
        "delay": "red",
        "diastole_time": "orange",
    }

    color = colors.get(activation_mode, "blue")   # Default color if not found
    # Define colors for activation_variations
    marker_styles = {
        0.01: "v",
        0.03: "<",
        0.05: "^"
    }
    marker = marker_styles.get(activation_variation, "o")  # Default marker if not found
    # Determine fill style based on the compartment type
    if "homogenous" in s:
        facecolors = 'none'  # Hollow markers for homogeneous
    else:
        facecolors = color   # Filled markers for heterogeneous
    name = f"{activation_mode}_{activation_variation}_{c} compartments"
    ax.scatter(
        c, data[1], 
        label=name, 
        color=color, 
        marker=marker,
        facecolors=facecolors, 
        edgecolors=color
    )
    return ax

# %%
def parse_arguments(args=None):
    parser = argparse.ArgumentParser()
    # Segmentation parameters
    # Output folder
    parser.add_argument(
        "-o",
        "--outdir",
        default="00_ToW_Results",
        type=Path,
        help="The output directory in the folder_data",
    )
    # Data folder
    parser.add_argument(
        "-f",
        "--data_folder",
        default="/home/shared/01_results_24_10_30_apex",
        type=Path,
        help="The directory of the data to be post processed",
    )
    parser.add_argument(
        "-p",
        "--prominence",
        default=0.03,
        type=float,
        help="The prominence for the peak detection algorithm",
    )
    return parser.parse_args(args)

def main(args=None) -> int:
    if args is None:
        args = parse_arguments()
    prominence = args.prominence
    data_folder = args.data_folder
    outdir = data_folder / args.outdir
    outdir.mkdir(exist_ok=True, parents=True)
            
    # fig, ax = plt.subplots(figsize=(10, 6))
    # for s in s_values:
    #     for activation_mode in activation_modes:
    #         for activation_variation in activation_variations:
    #             results_folder = f"{data_folder}/{s}/{activation_mode}_{int(activation_variation * 1000)}/72_6"
    #             fname = f"{results_folder}/00_tow_index_{prominence}.csv"
    #             if Path(fname).exists():
    #                 data = np.loadtxt(fname, delimiter=",", skiprows=1)
    #                 ax = plot_EF_tow(ax, data, s, activation_mode, activation_variation)
    # plt.grid(True)  
    # fname =  outdir / f'EFvToW_{prominence}.png'
    # ax.set_xlabel("Ejection Fraction (%)")
    # ax.set_ylabel("Tug of War index (%)")
    # ax.set_ylim([-5, 100])
    # ax.set_xlim([50, 60])
    # plt.legend(loc="lower left")
    # plt.savefig(fname=fname)
    # plt.close()
    # fig, ax = plt.subplots(figsize=(10, 6))
    # for s in s_values:
    #     for activation_mode in activation_modes:
    #         for activation_variation in activation_variations:
    #             for c in num_circ_segments:
    #                 for l in num_long_segments:
    #                     results_folder = f"{data_folder}/{s}/{activation_mode}_{int(activation_variation * 1000)}/{c}_{l}"
    #                     fname = f"{results_folder}/00_tow_index_{prominence}.csv"
    #                     if Path(fname).exists():
    #                         data = np.loadtxt(fname, delimiter=",", skiprows=1)
    #                         ax = plot_comp_tow(ax, data, s, activation_mode, activation_variation,c,l)
    # plt.grid(True)  
    # fname =  outdir / f'CompvToW_{prominence}.png'
    # ax.set_xlabel("Compartment no.")
    # ax.set_ylabel("Tug of War index (%)")
    # ax.set_ylim([-5, 100])
    # ax.set_xlim([0, 100])
    # # plt.legend(loc="lower left", bbox_to_anchor=(1.5, 1))
    # plt.savefig(fname=fname)
    # plt.close()
    
    # sv = 0
    
    for sv in mi_severity:
        EF = []
        ToW = []
        fig, ax = plt.subplots(figsize=(10, 6))
        for st in mi_stiffness:
            for c in num_circ_segments:
                for l in num_long_segments:
                    results_folder = f"{base_outdir}/Severity_{int(sv * 100)}_Stiffness_{st}/{c}_{l}"
                    fname = f"{results_folder}/00_tow_index_{prominence}.csv"
                    if Path(fname).exists():
                        data = np.loadtxt(fname, delimiter=",", skiprows=1)
                        EF.append(data[0])
                        ToW.append(data[1])
                        ax = plot_EF_tow_mi_stiffness(ax, data, st)
        plt.grid(True) 
        ax.plot(EF, ToW, 'k')
        fname =  outdir / f'Stiffness_EFvToW_Severity_{int(sv * 100)}.png'
        ax.set_xlabel("Ejection Fraction (%)")
        ax.set_ylabel("Tug of War index (%)")
        ax.set_ylim([-5, 100])
        ax.set_xlim([0, 100])
        # plt.legend(loc="lower left", bbox_to_anchor=(1.5, 1))
        plt.savefig(fname=fname)
        plt.close()
        
    for st in mi_stiffness:
            EF = []
            ToW = []
            fig, ax = plt.subplots(figsize=(10, 6))
            for sv in mi_severity:
                for c in num_circ_segments:
                    for l in num_long_segments:
                        results_folder = f"{base_outdir}/Severity_{int(sv * 100)}_Stiffness_{st}/{c}_{l}"
                        fname = f"{results_folder}/00_tow_index_{prominence}.csv"
                        if Path(fname).exists():
                            data = np.loadtxt(fname, delimiter=",", skiprows=1)
                            EF.append(data[0])
                            ToW.append(data[1])
                            ax = plot_EF_tow_mi_stiffness(ax, data, st)
            plt.grid(True) 
            ax.plot(EF, ToW, 'k')
            fname =  outdir / f'Severity_EFvToW_Stiffness_{int(st)}.png'
            ax.set_xlabel("Ejection Fraction (%)")
            ax.set_ylabel("Tug of War index (%)")
            ax.set_ylim([-5, 100])
            ax.set_xlim([0, 100])
            # plt.legend(loc="lower left", bbox_to_anchor=(1.5, 1))
            plt.savefig(fname=fname)
            plt.close()
                
# %%
if __name__ == "__main__":
    main()
