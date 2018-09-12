# very simple script That removes duplicated images and saves your Time.
import re
import shutil
import os


pattern = re.compile(r"copy\*?")

def getPath(path):
    file_count = 0
    dest = os.path.join("#path")
    for file1 in os.listdir(path):
        file_count += 1
        check = pattern.match(file1)
        if check == None:
            shutil.move(path +"/"+ file1, dest)
        else:
            print("{} : it's duplicated".format((file1)))
    print("we have complited : total files = {}".format(file_count))


getPath("#enter path")
