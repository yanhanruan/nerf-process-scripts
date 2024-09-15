import os
import time
import trimesh
import pywavefront
import numpy as np
import pandas as pd 

# Function to calculate the quality of normals (we'll check how normalized they are)
def calculate_normals_quality(mesh):
    normals = mesh.vertex_normals
    magnitudes = np.linalg.norm(normals, axis=1)
    # The closer the magnitudes are to 1, the better the normals' quality
    deviation_from_unit = np.abs(magnitudes - 1)
    average_deviation = np.mean(deviation_from_unit)
    return average_deviation

# Function to measure render time (simulate more complex operations)
def measure_render_time(mesh):
    start_time = time.perf_counter()
    
    # Simulate rendering complexity by calculating some properties multiple times
    for _ in range(100):  # Increase the number of iterations to simulate complexity
        _ = mesh.centroid
        _ = mesh.bounds
        _ = mesh.vertices.mean(axis=0)
    
    render_time = time.perf_counter() - start_time
    return render_time

# Function to process a single OBJ file and return the indicators
def process_obj_file(filepath):
    # Load the mesh using trimesh
    mesh = trimesh.load(filepath)

    # Vertex count
    vertex_count = len(mesh.vertices)

    # Polygon (Face) count
    polygon_count = len(mesh.faces)

    # Normals quality
    normals_quality = calculate_normals_quality(mesh)

    # Render time (simulated)
    render_time = measure_render_time(mesh)

    # File size in MB
    file_size = os.path.getsize(filepath) / (1024 * 1024)

    return {
        'Filename': os.path.basename(filepath),
        'Vertex Count': vertex_count,
        'Polygon Count': polygon_count,
        'Normals Quality': normals_quality,
        'Render Time (seconds)': render_time,
        'File Size (MB)': file_size
    }

# Function to process all OBJ files in the given folder
def process_obj_files_in_folder(folder_path):
    results = []

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".obj"):
            filepath = os.path.join(folder_path, filename)
            result = process_obj_file(filepath)
            results.append(result)

    # Save the results to a CSV file
    df = pd.DataFrame(results)
    output_csv = os.path.join(folder_path, 'obj_quality_results.csv')
    df.to_csv(output_csv, index=False)

    print(f"Results saved to {output_csv}")

# Folder containing the OBJ files
folder_path = 'data/8-26/2'

# Process the folder
process_obj_files_in_folder(folder_path)
