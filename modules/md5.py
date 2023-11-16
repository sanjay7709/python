# sortnames.py

def readname():
    print("Enter list of names seperated by space: ")
    lst=[str(names) for names in input().split() ]
    return lst

def dispname(name):
    print("*"*50)
    for i in name:
        print(i, end=" ")
    else:
        print()
        print("*"*50)
    

def sortname():
    name=readname()
    print("original names: ")
    dispname(name)
    print("Sorted names: ")
    name.sort()
    dispname(name)
    print("reverse order names: ")
    name.sort(reverse=True)
    dispname(name)

sortname()