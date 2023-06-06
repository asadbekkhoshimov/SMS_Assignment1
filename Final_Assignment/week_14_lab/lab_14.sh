#!/bin/bash
# Name: Asadbek
# Course: Operating_System

echo "Mounting the filesystem:"
sudo mount /dev/sdb1 /mnt/mydisk

# display the mounted filesystems
df -h

echo "Unmounting the filesystem:"
sudo umount /mnt/mydisk

# display the filesystems after unmounting
df -h

