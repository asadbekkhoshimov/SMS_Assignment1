import os

# Define your directory structure
base_dir = "~/SMS_Assignment1/Final_Assignment/week_14_lab"
sub_dir = "sub_directory"
file_name = "my_file.txt"

# Create the base directory
os.makedirs(os.path.expanduser(base_dir), exist_ok=True)

# Create the subdirectory
sub_dir_path = os.path.join(base_dir, sub_dir)
os.makedirs(os.path.expanduser(sub_dir_path), exist_ok=True)

# Create the file in the subdirectory
file_path = os.path.join(sub_dir_path, file_name)
with open(os.path.expanduser(file_path), 'w') as file:
    file.write("This is a file within a subdirectory of a directory in the Linux file system.\n")

print(f"File {file_path} has been created.")

