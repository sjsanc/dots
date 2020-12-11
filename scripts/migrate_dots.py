from distutils.dir_util import copy_tree
import os
import shutil
import sh 

home = "/home/" + os.environ.get("USER")
folderlist = "/misc/migration_list.txt"

locations = [i.strip().split() for i in open(home + folderlist).readlines()]

for val in locations: 
    src = home + val[1]
    if os.path.isdir(src):
        copy_tree(src, home + "/dots/" + val[0])
        print("Moved directory: {0}".format(val[0]))
    elif os.path.isfile(src):
        shutil.copy(src, home + "/dots")
        print("Moved file: {0}".format(val[0]))
    else:
         # print(path + val[1] + "=>" + path + "/dots/" + val[0])  
         print("Could not move file: {0}".format(val[0]))


