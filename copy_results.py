from pathlib import Path
import shutil
import argparse

def copy_files_of_interest(root_dir: str, out_dir: str, filename: str, user_prefix: str = ""):
    # Convert to Path objects
    root_path = Path(root_dir).expanduser()
    output_path = Path(out_dir).expanduser()

    # Ensure the output directory exists
    output_path.mkdir(parents=True, exist_ok=True)

    if not user_prefix == "":
        user_prefix = f"{user_prefix}_"
                    
    # Iterate over each experiment folder in the root directory
    for folder_path in root_path.iterdir():
        if folder_path.is_dir():
            # Construct the path to the file of interest, allowing for subdirectories
            file_path = folder_path / Path(filename).relative_to(Path(filename).anchor)
            
            # Check if the file exists
            if file_path.exists():
                # Define the new file path in the output directory with the experiment name
                new_file_path = output_path / f'{user_prefix}{folder_path.name}{file_path.suffix}'
                
                # Copy the file to the output directory
                shutil.copy(file_path, new_file_path)
                print(f'Copied {file_path} to {new_file_path}')
            else:
                print(f'File not found: {file_path}')

    print('File copying complete.')

# %%
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy files of interest from experiment folders to an output directory.")
    parser.add_argument(
        "--root_dir",
        default="/home/shared/01_results_24_11_29",
        type=str,
        help='Path to the root directory containing experiment folders',
    )
    parser.add_argument(
        "--out_dir",
        default="/home/shared/01_results_24_11_29_compare",
        type=str,
        help='Path to the output directory'
        )
    parser.add_argument(
        "--filename",
        default="72_6/Green-Lagrange Strains Fibers.png",
        type=str,
        help='Path to the file to copy from each experiment folder (relative to the experiment folder)',
    )
    parser.add_argument(
        "--user_prefix",
        default="",
        type=str,
        help='Prefix for output name',
    )
    args = parser.parse_args()

    copy_files_of_interest(args.root_dir, args.out_dir, args.filename, user_prefix=args.user_prefix)