import os
import subprocess
import argparse

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
        
        subprocess.run(command)
        print(f"Processed {video_path}")

    print("All videos processed successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process videos and generate transforms.json files.")
    parser.add_argument("--folders", nargs='+', default=[f"data\\8-12\\{i}" for i in range(1, 26)], help="List of folders to process.")
    parser.add_argument("--video_fps", type=int, default=4, help="Frames per second for video processing.")
    parser.add_argument("--aabb_scale", type=int, default=16, help="AABB scale for processing.")
    
    args = parser.parse_args()
    
    process_videos(args.folders, args.video_fps, args.aabb_scale)
