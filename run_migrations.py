import os

directory = 'migrations'

for file in os.listdir(directory):
    file_name = os.path.join(directory, file)
    if os.path.isfile(file_name):
        os.system(f"python3 {file_name}")