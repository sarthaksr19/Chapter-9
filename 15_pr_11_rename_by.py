import os
oldname = "sample_for_rename.txt"   # but hold on here we only tranfer the data of sample_for_rename.txt file to another file named as newname variable. and the main problem is how to remove old file. so we import a module named OS.
newname = "renamed_by_python.txt"

with open(oldname) as f:
    old = f.read()
with open(newname,'w')as f:
    f.write(old)
os.remove(oldname) #os module have remove function which is used for deleting a file. 