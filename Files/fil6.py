# read data from keyboard
# read content and display on the monitor
try:
    fn=input("enter file name: ")
    with open(fn,"r") as fp:
        fd=fp.read()
        print(type(fd))
        print("*"*50)
        print("content of the data: {}".format(fd))
        print("*"*50)
except FileNotFoundError:
    print("file {} does not exists".format(fn))