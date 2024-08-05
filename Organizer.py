import os
import shutil

# Function to organize files
def organize_files():
    path = os.getcwd()
    for file in os.listdir(path):
        full_file_path = os.path.join(path, file)
        # Ignore directories and files without an extension
        if os.path.isfile(full_file_path) and '.' in file:
            extension = file.split('.')[-1]
            # Ignore Python files and the current directory
            if extension != 'py':
                dest_dir = os.path.join(path, extension)
                # Create directory if it does not exist
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                # Check if the file is already in the correct directory
                if os.path.dirname(full_file_path) != dest_dir:
                    try:
                        shutil.move(full_file_path, dest_dir)
                    except Exception as e:
                        print(f"Error moving file {file}: {e}")
                        continue

organize_files()
