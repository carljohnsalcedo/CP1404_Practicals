"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os
__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())
changed_name = ""
os.chdir('Lyrics/Christmas')
for filename in os.listdir('.'):
    if not os.path.isdir(filename):
        count = -1
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        new_example = new_name[0]
        for letter in new_name[1:]:
            if letter.isupper() and count != 0:
                new_example += '_'
            if letter.islower() and new_example[-1] == "_":
                letter = letter.upper()
            new_example += letter
            count += 1
        new_example = new_example.replace("__", "_").replace("(_", "(")
        print(new_example)
        os.rename(filename, new_name)

os.chdir('..')
for dir_name, subdir_list, file_list in os.walk('.'):
    print("In", dir_name)
    print("\tcontains subdirectories:", subdir_list)
    print("\tand files:", file_list)
