import os
import shutil

# Function to organize files
def organize_files():
    abs_path = os.getcwd()
    for file in os.listdir(abs_path):
        extension = file.split('.')[-1]
        if extension != 'py' and not os.path.exists(extension):
            os.makedirs(extension)
        shutil.move(file, extension)

organize_files()
