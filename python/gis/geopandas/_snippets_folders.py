##
## Folders
##

## cd C:\Python27\ArcGISx6410.5
## python -m pip install {package}
import os, sys

dataFolder = 'C:\Users\Duncan\Desktop\Data\GIS\DC'
os.chdir(dataFolder)

# list names of files and folders in specified directory
files = os.listdir(dataFolder)
for file in files:
    print file

# list full path of files in specified directory (this only goes one level deep)
for item in os.listdir(dataFolder):
    if os.path.isfile(os.path.join(dataFolder, item)):
        print item

## loop through folder and subfolders and print full paths of files in a directory
for root, dirs, files in os.walk(dataFolder):
    for name in files:
        print(os.path.join(root, name))

# loop through folder and find all files with specific extension
for root, dirs, files in os.walk(dataFolder):
    for name in files:
        if name[name.rfind("."):len(name)] == ".csv":
            print(os.path.join(root, name))

# loop thorugh folder and find subfolders with a specific pattern
# in this case, ones that start with the capital letter r
import re
for root, dirs, files in os.walk(dataFolder):
    for name in dirs:
        if (re.search(r'R\w+', name)):
            print(os.path.join(root, name))

# loop through subfolders and create separate list from files
for root, dirs, files in os.walk(dataFolder):
    for name in dirs:
        print("Files/folders in subdirectory: ", name)
        for root2, dirs2, files2 in os.walk(os.path.join(root, name)):
            for file2 in files2:
                print(os.path.join(root2, file2))



        

