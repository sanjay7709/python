# os module

''''
getcwd()
mkdir()
makedirs()
rmdir()
removedirs()
rename()
listdir()

Exceptions
=============

os error
FileNotFoundError
'''
# Rename
import os
try:
    os.rename("functions", "Functions")
    print("Folder renamed successfulyy")
except FileNotFoundError:
    print("File does not exists")

try:
    a=os.listdir(".")  #current working folder 
    print(type(a))
    for i in a:
        print(i)
    else:
        print("No of files = {}".format(len(a)))
except FileNotFoundError:
    print("File does not exists")
