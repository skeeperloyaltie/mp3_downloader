import os
from pathlib import Path

def select_directory():
    current_directory = os.getcwd()
    selected_directory = str(Path(input("Please select a directory: ")).resolve())
    os.chdir(current_directory)
    return selected_directory

selected_directory = select_directory()
print(selected_directory)

