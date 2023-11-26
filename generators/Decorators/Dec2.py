# decorators method 
def square(san):
    def operations():
        n=san()
        sq=n**2
        return sq
    return operations

def getval():
    n=float(input("enter the number: "))
    return n

#main program
obj=square(getval)
print("square = {}".format(obj()))