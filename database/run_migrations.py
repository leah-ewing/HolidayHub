import os, sys

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_directory)

directory = f'{root_directory}/migrations'

for i in range(1, len(os.listdir(directory)) + 1):
    for file in os.listdir(directory):
        if int(file[0:2].strip('-')) == i:
            file_name = os.path.join(directory, file)
            os.system(f"python3 {file_name}")