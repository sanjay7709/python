def sume():
    n=int(input("enter the size of list:  "))
    if(n<=0):
        return None
    else:
        l=list()
        for i in range(1,n+1):
            val=float(input("enter the elements {} of list: ".format(i)))
            l.append(val)
        return l

def display(c):
    k=sum(c)
    print("sum of list : {}".format(k))
    l= (k/len(c))
    print("the average of list: {}".format(l))
    print("-"*50)

def maxmin(c):
    m= max(c)
    print("The max value of list: {}".format(m))
    n=min(c)
    print("The min value of list: {}".format(n))

#main program
c=sume()
if(c==None):
    print("{} is an invalid input".format(c))
else:
    print("-"*50)
    display(c)
    maxmin(c)
    print("-"*50)
