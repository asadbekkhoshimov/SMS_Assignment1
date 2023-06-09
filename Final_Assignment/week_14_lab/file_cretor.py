import os

# Define your directory structure
base_dir = "/path/to/your/base/directory"  # replace this with the actual path
sub_dir = "sub_directory"

# Create the base directory
os.makedirs(base_dir, exist_ok=True)

# Create the subdirectory
sub_dir_path = os.path.join(base_dir, sub_dir)
os.makedirs(sub_dir_path, exist_ok=True)

# Create 10 files in the subdirectory
for i in range(1, 11):
    file_name = f"my_file_{i}.txt"
    file_path = os.path.join(sub_dir_path, file_name)
    with open(file_path, 'w') as file:
        file.write(f"This is file number {i} within a subdirectory of a directory in the Linux file system.\n")

    print(f"File {file_path} has been created.")

