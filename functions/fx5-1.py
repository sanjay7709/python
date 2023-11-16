 #all arithmetric operations using functions
from os import system
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

r=True
while(r):
        print("*"*50)
        print("\t ...Welcome to Arithmetic application....")
        print("*"*50)
        print("\t1.addition")
        print("\t2.subtraction")
        print("\t3.multiplication")
        print("\t4.division")
        print("\t5.modulos")
        print("\t6.exponential")
        print("\t7.Exit")
        print("*"*50)
        ch = int(input("please enter your choice: "))
        match(ch):
                case 1:
                    addop()
                case 2:
                    subop()
                case 3:
                    mulop()
                case 4:
                    divop()
                case 5:
                    moduop()
                case 6:
                    expo()
                case 7:
                  break
                case _:
                    print("invalid input please enter the write value")
        k= input("Do you want to continue the operations (y|Y|n|N): ")
        if(k=="y" or k=="Y"):
             system('cls')  #module to clear screen
             r=True
        else:
             print("*"*50)
             print("thanks for using the application! .......")
             print("*"*50)
             break
