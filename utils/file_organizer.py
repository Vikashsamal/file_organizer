import os, sys
import shutil
from utils.helper import get_file_extension, create_directory

class FileOrganizer:
    def __init__(self, source_directory):
        self.source_directory = source_directory
        # Organise complete files

    def organize_files(self):
        if not os.path.exists(self.source_directory):
            print("Source directory not exists")
            return
    # Used to get the list of all file and directory in the specified directory. 
        for filename in os.listdir(self.source_directory):
            file_path = os.path.join(self.source_directory, filename)
            
    # Checking whether the file path exists or not.
            if os.path.isfile(file_path):
                extension = get_file_extension(filename)
                if extension:
                    destination_directory = os.path.join(self.source_directory, extension[1:])
                    create_directory(destination_directory)
                    
                try:
                    shutil.move(file_path, os.path.join(destination_directory, filename))
                    print(f"moved '{filename}' to ''{destination_directory}'")
                except Exception as e:
                    print(f"Error during moving '{filename}' to '{destination_directory}': {e}")
                    
                else:
                    print(f"Skipped '{filename}' as it doesn't have any extension.")
                
            else:
                print(f"Skipped '{filename}' as it is not a file.")
            
        print("Our files are organized.")