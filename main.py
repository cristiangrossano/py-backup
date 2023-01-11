import os
import shutil

# Add path to folders
local_folder = "./testA"
destination_folder = "./testB"

print("Copying files from " + str(local_folder) +
      " to " + str(destination_folder))

local_files = os.listdir(local_folder)

for file_name in local_files:
    local_file = os.path.join(local_folder, file_name)
    destination_file = os.path.join(destination_folder, file_name)
    if not os.path.exists(destination_file):
        shutil.copy2(local_file, destination_folder)
        print("Copied " + str(local_file))

print("Completed!")
