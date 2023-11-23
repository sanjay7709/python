'''
pypr read text document and reads texts file and retrive names and marks 

'''
import re
try:
    with open("studinfo.data","r") as rp:
        fd=rp.read()
        namedat=re.findall("[A-Z][a-z]+",fd)
        # for name in namedat:
        #     print(name)
        marksdat=re.findall("\d{2}",fd)
        # for marks in marksdat:
        #     print(marks)  
        print("*"*40) 
        print("\tName\tMarks")
        print("*"*40) 
        for name, marks in zip(namedat,marksdat):
            print("\t{}\t{}".format(name,marks))
        print("*"*40)     
except FileNotFoundError:
    print("file does not exists")