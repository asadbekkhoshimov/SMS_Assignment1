#!/bin/bash
# Name: Asadbek
# Course: Operating_System

# Create a log file
logfile="file_ops.log"

# Function to log and print message
log_and_print() {
    echo "$1"
    echo "$1" >> "$logfile"
}

# Create a directory
dir1="my_directory"
log_and_print "Creating directory $dir1"
mkdir "$dir1"

# Create a file
file1="my_file.txt"
log_and_print "Creating file $file1"
touch "$file1"

# Move the file into the directory
log_and_print "Moving $file1 into $dir1"
mv "$file1" "$dir1"

# List the contents of the directory
log_and_print "Contents of $dir1:"
ls "$dir1" | while read -r line; do log_and_print "$line"; done

# Remove the file
log_and_print "Removing $file1 from $dir1"
rm "$dir1/$file1"

# Remove the directory
log_and_print "Removing directory $dir1"
rmdir "$dir1"

