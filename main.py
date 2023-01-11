import os
import shutil

# Add path to folders
local_folder = "./testA"
destination_folder = "./testB"
count = 0

print("Copying files from " + local_folder + " to " + destination_folder)

local_files = os.listdir(local_folder)

for file_name in local_files:
    local_file = os.path.join(local_folder, file_name)
    destination_file = os.path.join(destination_folder, file_name)
    if not os.path.exists(destination_file):
        shutil.copy2(local_file, destination_folder)
        count = count + 1

print("Completed!")
print(str(count) + "was successfully copied.")
