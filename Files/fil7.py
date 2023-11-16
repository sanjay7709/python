'''try:
    fn=input("enter file name: ")
    with open(fn,"r") as fp:
        n=int(input("enter the index position: "))
        fd=fp.read(n)
        print(type(fd))
        print("position of fp = {}".format(fp.tell())) # to find the index position of file pointer
        print("*"*50)
        print("content of the data: {}".format(fd))
        print("*"*50)
        fp.seek(0) # repoisition to beggining
        fd=fp.read()
        print(fd)
        print("position of fp = {}".format(fp.tell()))
except FileNotFoundError:
    print("file {} does not exists".format(fn))'''



fn=input("enter file name: ")
with open(fn,"r") as fp:
    line=fp.readline()
    print(line)
    print(type(line))

fn=input("enter file name: ")
with open(fn,"r") as fp:
    line=fp.readlines()
    print(line)
    print(type(line))
    for i in line:
        print(i, end= "")