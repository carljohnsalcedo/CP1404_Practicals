import os, shutil

print("Current directory is", os.getcwd())

os.chdir('FilesToSort')

os.mkdir('xlsx')
os.mkdir('xls')
os.mkdir('txt')
os.mkdir('png')
os.mkdir('jpg')
os.mkdir('gif')
os.mkdir('docx')
os.mkdir('doc')

CATEGORY = ["doc", "docx", "png", "gif", "txt", "xls", "xlsx", "jpg"]

for category in CATEGORY:

    for filename in os.listdir('.'):

        if not os.path.isdir(filename):
            if filename.find(".{}x".format(category)) > -1:
                shutil.move(filename, '{}x/'.format(category) + filename)
            elif filename.find(".{}".format(category)) > -1:
                shutil.move(filename, '{}/'.format(category) + filename)
