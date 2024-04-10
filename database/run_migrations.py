import os, sys


root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

directory = f'{root_directory}/migrations'

for file in os.listdir(directory):
    file_name = os.path.join(directory, file)
    if os.path.isfile(file_name):
        os.system(f"python3 {file_name}")