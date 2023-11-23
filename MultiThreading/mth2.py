import threading
def hello():
    tname1=threading.current_thread().name
    print("default excution done by = ",tname1)
    print("hello world")

def hi():
    tname2=threading.current_thread().name
    print("default excution done by = ",tname2)
    print("hi world")

def show():
    tname3=threading.current_thread().name
    print("default excution done by = ",tname3)
    print("show world")

dfname=threading.current_thread().name
print("default excution done by = ",dfname)
hi()
hello()
show()