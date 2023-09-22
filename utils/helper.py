import os, sys
import shutil

# This function check for file's extension.

def get_file_extension(filename):
    _, extension = os.path.splitext(filename)
    return extension

# Create Directory 

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)