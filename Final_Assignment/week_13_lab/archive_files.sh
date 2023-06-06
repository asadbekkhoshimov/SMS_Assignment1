#!/bin/bash
# Name: Asadbek
# Course: Operating_System

# Replace 'my_directory' with the directory you want to archive
echo "Creating a tar archive of a directory:"
tar -cvf my_archive.tar week_13_lab

echo "Listing the contents of the tar archive:"
tar -tvf my_archive.tar

echo "Extracting the tar archive into a directory called 'extracted_files':"
mkdir extracted_files
tar -xvf my_archive.tar -C extracted_files

