import os
os.system('cls')
try:
    #san=open("stud.info","w")
    #san=open("stud.info","w+")
    with open("stud.info","w+") as san:
        print("file opened in read mode successfully")
        print("type of file pointer= {}".format(type(san)))
        print("file name= {}".format(san.name))
        print("file mode= {}".format(san.mode))
        print("is {} is readable ? = {}".format(san.name,san.readable()))
        print("is {} is writable ? = {}".format(san.name,san.writable()))
        print("is {} is closed ? = {}".format(san.name,san.closed)) 
except FileNotFoundError:
    print("File does not exists")
# else:
#     print("file opened in write mode successfully")
#     print("type of file pointer= {}".format(type(san)))
#     print("file name= {}".format(san.name))
#     print("file mode= {}".format(san.mode))
#     print("is {} is readable ? = {}".format(san.name,san.readable()))
#     print("is {} is writable ? = {}".format(san.name,san.writable()))
#     print("is {} is closable ? = {}".format(san.name,san.closed))
finally:
    san.close()
    print("This is finally block")
    print("is {} is closed ? = {}".format(san.name,san.closed))