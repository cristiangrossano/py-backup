import os
import shutil

# Add path to folders
local_folder = "./TestA"
destination_folder = "./TestB"
count = 0

print(f"Copying files from {local_folder}  to  {destination_folder}")

for subdir, dirs, files in os.walk(local_folder):
    subdir_name = os.path.relpath(subdir, local_folder)
    destination_subdir = os.path.join(destination_folder, subdir_name)
    if not os.path.exists(destination_subdir):
        os.makedirs(destination_subdir)
    for file_name in files:
        local_file = os.path.join(subdir, file_name)
        destination_file = os.path.join(destination_subdir, file_name)
        if not os.path.exists(destination_file):
            shutil.copy2(local_file, destination_subdir)
            count = count + 1

print("Completed!")
print(f"{count} files was successfully copied.")
