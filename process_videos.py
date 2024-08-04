# FIXME wrong relative image_path in generated transform.json file 
import os
import subprocess

def process_videos(num_folders):
    # Generate folder names and video file names dynamically
    folders = [f"data\\7-22\\{i}" for i in range(1, num_folders + 1)]
    video_files = [f"C{i:04d}.MP4" for i in range(1, num_folders + 1)]

    # Path to the colmap2nerf.py script
    script_path = "C:/Users/WIN/Desktop/Instant-NGP-for-RTX-3000-and-4000/scripts/colmap2nerf.py"

    # Loop through each folder and process the video file inside
    for folder, video_file in zip(folders, video_files):
        video_path = os.path.join(folder, video_file)
        output_path = os.path.join(folder, "transforms.json")
        command = [
            "python", script_path,
            "--video_in", video_path,
            "--video_fps", "4",
            "--run_colmap",
            "--aabb_scale", "16",
            "--out", output_path,
            "--overwrite"
        ]
        
        subprocess.run(command)
        print(f"Processed {video_path}")

    print("All videos processed successfully!")

# Define the number of folders
num_folders = 6  # Change this value as needed

# Call the function to process the videos
process_videos(num_folders)
