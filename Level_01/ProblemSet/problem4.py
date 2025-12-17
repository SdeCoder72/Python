# Write a python program to print the contents of a directory using the os module. Search online for the function which does that

import os

# Specify the directory 
directory_path = 'Your/directory/path'

# List all files and directories in te specified path 
contents = os.listdir(directory_path)

# Print each file and directory name 
for item in contents:
    print(item)