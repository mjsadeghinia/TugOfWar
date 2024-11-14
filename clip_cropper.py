import cv2
import os

def crop_avi_by_percentage(input_avi, output_mp4, rec_percentage):
    """
    Crop a video based on a rectangle defined as percentages of total width and height,
    and save it as an MP4 file.

    Args:
        input_avi (str): Path to the input AVI file.
        output_mp4 (str): Path to save the cropped MP4 file.
        rec_percentage (tuple): Rectangle percentages (x%, y%, width%, height%).
    """
    if not os.path.exists(input_avi):
        raise FileNotFoundError(f"Input file {input_avi} not found.")

    # Open the input video
    cap = cv2.VideoCapture(input_avi)
    if not cap.isOpened():
        raise ValueError(f"Unable to open video file {input_avi}.")

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Extract percentages
    x_pct, y_pct, w_pct, h_pct = rec_percentage
    if not (0 <= x_pct <= 1 and 0 <= y_pct <= 1 and 0 <= w_pct <= 1 and 0 <= h_pct <= 1):
        raise ValueError("Rectangle percentages must be between 0 and 1.")

    # Convert percentages to pixel values
    x = int(x_pct * frame_width)
    y = int(y_pct * frame_height)
    w = int(w_pct * frame_width)
    h = int(h_pct * frame_height)

    # Ensure the rectangle is within bounds
    if x < 0 or y < 0 or x + w > frame_width or y + h > frame_height:
        raise ValueError("Cropping rectangle is out of bounds.")

    # Define codec (mp4v for compatibility) and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_mp4, fourcc, fps, (w, h), isColor=True)

    print(f"Processing video: {frame_count} frames")
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Crop the frame
        cropped_frame = frame[y:y+h, x:x+w]

        # Write the cropped frame to the output video
        out.write(cropped_frame)
        frame_idx += 1
        if frame_idx % 100 == 0:
            print(f"Processed {frame_idx}/{frame_count} frames...")

    # Release resources
    cap.release()
    out.release()
    print(f"Cropping completed. Cropped video saved to {output_mp4}")


def process_videos_in_folder(folder_path, rec_percentage):
    """
    Process all video files in a folder by cropping them and saving as MP4 files.

    Args:
        folder_path (str): Path to the folder containing video files.
        rec_percentage (tuple): Rectangle percentages (x%, y%, width%, height%).
    """
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".avi"):  # Process only AVI files
            input_file = os.path.join(folder_path, file_name)
            output_file = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}.mp4")  # Change extension to .mp4

            print(f"Processing video: {file_name}")
            crop_avi_by_percentage(input_file, output_file, rec_percentage)

            # Optionally, remove the original file after conversion
            os.remove(input_file)
            print(f"Video {file_name} processed and saved as {output_file}")


# Example usage
if __name__ == "__main__":
    folder_path = "/home/shared/01_results_24_11_14_videos"  # Replace with your folder path
    rectangle_percentage = (0.35, 0, 0.35, 0.9)  # Crop rectangle as percentages (x%, y%, width%, height%)

    process_videos_in_folder(folder_path, rectangle_percentage)
