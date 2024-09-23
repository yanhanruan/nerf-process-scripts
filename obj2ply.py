import os
import pymeshlab
import argparse

def convert_obj_to_ply(directory):
    # Create a new MeshSet
    ms = pymeshlab.MeshSet()

    # Traverse the directory and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.obj'):
                obj_path = os.path.join(root, file)
                ply_path = os.path.splitext(obj_path)[0] + '.ply'
                
                # Load the OBJ file
                ms.load_new_mesh(obj_path)
                
                # Save the mesh as a PLY file
                ms.save_current_mesh(ply_path)
                print(f'Converted: {obj_path} to {ply_path}')

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert OBJ files to PLY format.')
    parser.add_argument('--folder', type=str, required=True, help='Path to the folder containing OBJ files.')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Convert OBJ files to PLY
    convert_obj_to_ply(args.folder)
