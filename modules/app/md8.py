def readvalues(op):
     a,b=float(input("enter first value for {}: ".format(op))),float(input("enter second value for {}: ".format(op)))
     return a,b

def addop():
    a,b=readvalues("Addition")
    print("sum ({},{})={}".format(a,b,a+b))
def subop():
    a,b=readvalues("subtraction")
    print("sub ({},{})={}".format(a,b,a-b))
def mulop():
    a,b=readvalues("multiplication")
    print("mul ({},{})={}".format(a,b,a*b))
def divop():
    a,b=readvalues("division")
    print("div({},{})={}".format(a,b,a/b))
    print("floordiv({},{})={}".format(a,b,a//b))
def moduop():
    a,b=readvalues("modulous")
    print("mod ({},{})={}".format(a,b,a%b))
def expo():
    a,b=readvalues("exponential")
    print("expo ({},{})={}".format(a,b,a**b))