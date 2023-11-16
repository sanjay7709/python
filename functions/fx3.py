#accept list of elements and  sort in asc and desc

def readname():
    n=int(input("enter the size of list: "))
    if(n<=0):
        return None
    else:
        l=[]
        for i in range(1,n+1):
            val=input("enter the {} name : ".format(i))
            l.append(val)
        return l

def display(name):
    for i in name:
        print("\t{}".format (i))

def sortname(stname):
    #sort the names in ascending order
    stname.sort()
    print("Ascending order")
    display(stname)
    print("descending order")
    stname.sort(reverse=True)
    display(stname)
    
#main program
name=readname()
if(name==None):
    print("{} is an invalid input".format(name))
else:
    print("-"*50)
    print("original elements of list")
    display(name)
    sortname(name)

