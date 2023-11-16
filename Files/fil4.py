import os
os.system('cls')
try:
    #san=open("stud.info","a")
    san=open("stud.info","x")
except FileNotFoundError:
    print("File does not exists")
except FileExistsError:
    print("File already exists, please check the file name again..")
else:
    print("file opened in exclusively write mode successfully")
    print("type of file pointer= {}".format(type(san)))
    print("file name= {}".format(san.name))
    print("file mode= {}".format(san.mode))
    print("is {} is readable ? = {}".format(san.name,san.readable()))
    print("is {} is writable ? = {}".format(san.name,san.writable()))
    print("is {} is closable ? = {}".format(san.name,san.closed))
finally:
    san.close()
    print("This is finally block")
    print("is {} is closed ? = {}".format(san.name,san.closed))