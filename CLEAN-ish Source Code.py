import os
import glob

files_list = glob.glob("*")

extension_set = set()
for file in files_list:
    extension = file.split(sep=".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue
#print(extension_set)
def createDirs():
    for dir in extension_set:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue
def arrange():
    for file in files_list:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1]+"_files/"+file)
        except (OSError, IndexError):
            continue
createDirs()
arrange()