""" 
Decorators:
===============
To add additional functionality to the existing function

"""

# normal method 

def getval():
    n=float(input("enter the number: "))
    return n

def square():
    n=getval()
    sq=n**2
    return n,sq

obj=square()
print("square of {}={}".format(obj[0],obj[1]))