import os
import subprocess
import argparse
import json
import logging

def process_videos(folders, video_fps=4, aabb_scale=16):
    # Path to the colmap2nerf.py script
    script_path = "C:/Users/WIN/Desktop/Instant-NGP-for-RTX-3000-and-4000/scripts/colmap2nerf.py"

    # Loop through each folder and process the video file inside
    for folder in folders:
        # Find the MP4 video file in the folder
        video_file = next((f for f in os.listdir(folder) if f.lower().endswith('.mp4')), None)
        if video_file is None:
            print(f"No MP4 video file found in {folder}")
            continue
        
        video_path = os.path.join(folder, video_file)
        output_path = os.path.join(folder, "transforms.json")
        command = [
            "python", script_path,
            "--video_in", video_path,
            "--video_fps", str(video_fps),
            "--run_colmap",
            "--aabb_scale", str(aabb_scale),
            "--out", output_path,
            "--overwrite"
        ]
        
        try:
            subprocess.run(command, check=True)
            print(f"Processed {video_path}")
            modify_transform_json(output_path)
        except subprocess.CalledProcessError as e:
            print(f"Failed to process {video_path}: {e}")
    print("All videos processed successfully!")

def modify_transform_json(file_path):
    """Modify the file_path values in the transform.json file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        for frame in data.get('frames', []):
            if 'file_path' in frame:
                frame['file_path'] = frame['file_path'].split('images', 1)[-1]
                frame['file_path'] = 'images' + frame['file_path']
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        logging.info(f"Modified {file_path}")
    except Exception as e:
        logging.error(f"Failed to modify {file_path}: {e}")

def get_subfolders(parent_folder):
    """Retrieve subdirectories of a specified directory."""
    try:
        return [os.path.join(parent_folder, name) for name in os.listdir(parent_folder)
                if os.path.isdir(os.path.join(parent_folder, name))]
    except FileNotFoundError:
        print(f"Error: The directory {parent_folder} does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access {parent_folder}.")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process videos and generate transforms.json files.")
    # parser.add_argument("--folders", nargs='+', default=[f"data\\8-26\\{i}" for i in range(1, 31)], help="List of folders to process.")
    parser.add_argument("--folder", type=str, required = True, help="folder to process.")
    parser.add_argument("--video_fps", type=int, default=4, help="Frames per second for video processing.")
    parser.add_argument("--aabb_scale", type=int, default=16, help="AABB scale for processing.")
    
    args = parser.parse_args()
    
    subfolders = get_subfolders(args.folder)
    
    
    process_videos(subfolders, args.video_fps, args.aabb_scale)
