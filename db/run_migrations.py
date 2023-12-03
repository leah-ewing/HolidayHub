import os, sys

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

directory = f'{ROOT_FOLDER}/migrations'

for file in os.listdir(directory):
    file_name = os.path.join(directory, file)
    if os.path.isfile(file_name):
        os.system(f"python3 {file_name}")