"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

os.chdir('Lyrics/Christmas')

for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        print(new_name)
        os.rename(filename, new_name)

os.chdir('..')
for dir_name, subdir_list, file_list in os.walk('.'):
    print("In", dir_name)
    print("\tcontains subdirectories:", subdir_list)
    print("\tand files:", file_list)
