import os
import zipfile
import shutil

def zip_folders(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for folder_name in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder_name)
        if os.path.isdir(folder_path):
            zip_path = os.path.join(output_dir, f"{folder_name}.zip")
            h5p_path = os.path.join(output_dir, f"{folder_name}.h5p")

            try:
                # Create a zip file
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, _, files in os.walk(folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            # Store relative path inside the zip (removing the top folder level)
                            arcname = os.path.relpath(file_path, folder_path)
                            zipf.write(file_path, arcname)
                            print(f"Added {file_path} as {arcname} to {zip_path}")

                # Rename .zip to .h5p
                shutil.move(zip_path, h5p_path)
                print(f"Renamed {zip_path} to {h5p_path}")

                # Delete the original folder
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")
            except Exception as e:
                print(f"Error processing folder {folder_name}: {e}")

if __name__ == "__main__":
    input_directory = "/Users/tomomi/Downloads"  # Change to your folders' location
    output_directory = "/Users/tomomi/Downloads"  # Change to your desired output location
    zip_folders(input_directory, output_directory)