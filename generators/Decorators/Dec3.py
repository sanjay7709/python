# decorators method 
def cube(san):
    def operations():
        n=san()
        cub=n**3
        return cub
    return operations
def square(san):
    def operations():
        n=san()
        sq=n**2
        return sq
    return operations

#@cube       
#@square
def getval():
    n=float(input("enter the number: "))
    return n
#@cube
def disp():
    n=getval()
    return n
#main program
# obj=getval()
obj=square(getval)
obj1=cube(getval)
print("square = {}".format(obj()))
print("cube = {}".format(obj1()))