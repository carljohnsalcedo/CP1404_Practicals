"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

os.chdir('FilesToSort')

os.mkdir('Spreadsheets')
os.mkdir('Images')
os.mkdir('Docs')

CATEGORY = ["doc", "docx", "png", "gif", "txt", "xls", "xlsx", "jpg"]

for category in CATEGORY:
    chosen_category = input("What category would you like to sort {} files into? ".format(category))

    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            if filename.find(".{}".format(category)) > -1:
                shutil.move(filename, '{}/'.format(chosen_category) + filename)
