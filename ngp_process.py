import os
import subprocess

# List of relative paths containing transform.json files
relative_paths = [
    "data\\8-26\\1\\transforms.json",
    # "folder2/transform.json",
    # Add more paths as needed
]

# Absolute path to the instant-ngp executable
instant_ngp_executable = r"C:\Users\WIN\Desktop\Instant-NGP-for-RTX-3000-and-4000\instant-ngp.exe"

# Get the current working directory
current_dir = os.getcwd()

for relative_path in relative_paths:
    path = os.path.join(current_dir, relative_path)
    if os.path.exists(path):
        # Run instant-ngp with the transform.json file
        subprocess.run([instant_ngp_executable, "--input", path])
    else:
        print(f"File not found: {path}")
