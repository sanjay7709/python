# all arithmetric operations using functions

def addop():
    a,b=float(input("enter first value: ")),float(input("enter second value: "))
    c=a+b
    print("sum ({},{})={}".format(a,b,c))
def subop():
    a,b=float(input("enter first value: ")),float(input("enter second value: "))
    c=a-b
    print("sub ({},{})={}".format(a,b,c))
def mulop():
    a,b=float(input("enter first value: ")),float(input("enter second value: "))
    c=a*b
    print("mul ({},{})={}".format(a,b,c))
def divop():
    a,b=float(input("enter first value: ")),float(input("enter second value: "))
    c=a/b
    d=a//b
    print("div({},{})={}".format(a,b,c))
    print("floordiv({},{})={}".format(a,b,d))
def moduop():
    a,b=float(input("enter first value: ")),float(input("enter second value: "))
    c=a%b
    print("mod ({},{})={}".format(a,b,c))
def expo():
    a,b=float(input("enter base value: ")),float(input("enter power value: "))
    c=a**b
    print("expo ({},{})={}".format(a,b,c))
r=True
while(r):
        print("*"*50)
        print("\t1.addition")
        print("\t2.subtraction")
        print("\t3.multiplication")
        print("\t4.division")
        print("\t5.modulos")
        print("\t6.exponential")
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
                case _:
                    print("invalid input please enter the write value")
        k= input("Do you want to continue the operations (y|Y|n|N): ")
        if(k=="y" or k=="Y"):
             r=True
        else:
             break
