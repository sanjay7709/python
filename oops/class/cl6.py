import sys
class calculate():
    @staticmethod
    def cal(obj):
        # print(obj.__dict__)
        # print(obj.a,obj.b,obj.op)
        match (obj.op):
            case "+":
                print("sum({},{})={}".format(obj.a,obj.b,obj.a+obj.b))
            case "-":
                print("sub({},{})={}".format(obj.a,obj.b,obj.a-obj.b))
            case "*":
                print("mul({},{})={}".format(obj.a,obj.b,obj.a*obj.b))
            case "%":
                print("mod({},{})={}".format(obj.a,obj.b,obj.a%obj.b))
            case "/":
                try:
                    print("div({},{})={}".format(obj.a,obj.b,obj.a/obj.b))
                except ZeroDivisionError:
                    print("dont enter zero for deno")
            case "//":
                print("floordiv({},{})={}".format(obj.a,obj.b,obj.a//obj.b))
            case "**":
                print("exp({},{})={}".format(obj.a,obj.b,obj.a**obj.b))
            case _:
                print(" %s is an invalid operator " %obj.op)
class numbers():
    def getdata(self):
        try:
            self.a=float(input("enter the first value: "))
            self.b=float(input("enter the second value: "))
            self.op=input("enter the operator: ")
        except ValueError:
            print("dont enter the str, symbols other than arithmetic operators")
            sys.exit()

c1=numbers()
while (True):
    c1.getdata()
    calculate.cal(c1)
    ch = input("Do you want to enter another record (yes/no): ")
    if(ch.lower()=="no"):
        print("thanks for using this applictaion")
        break 

# another method of exception handling

import sys
class calculate():
    @staticmethod
    def cal(obj):
        # print(obj.__dict__)
        # print(obj.a,obj.b,obj.op)
        match (obj.op):
            case "+":
                print("sum({},{})={}".format(obj.a,obj.b,obj.a+obj.b))
            case "-":
                print("sub({},{})={}".format(obj.a,obj.b,obj.a-obj.b))
            case "*":
                print("mul({},{})={}".format(obj.a,obj.b,obj.a*obj.b))
            case "%":
                print("mod({},{})={}".format(obj.a,obj.b,obj.a%obj.b))
            case "/":
                try:
                    print("div({},{})={}".format(obj.a,obj.b,obj.a/obj.b))
                except ZeroDivisionError:
                    print("dont enter zero for deno")
            case "//":
                print("floordiv({},{})={}".format(obj.a,obj.b,obj.a//obj.b))
            case "**":
                print("exp({},{})={}".format(obj.a,obj.b,obj.a**obj.b))
            case _:
                print(" %s is an invalid operator " %obj.op)
class numbers():
    def getdata(self):
        self.a=float(input("enter the first value: "))
        self.b=float(input("enter the second value: "))
        self.op=input("enter the operator: ")


c1=numbers()
while (True):
    try:
        c1.getdata()
    except ValueError:
        print("dont enter str, symbols andd alpha-numeric data")
    else:
        calculate.cal(c1)
        ch = input("Do you want to enter another record (yes/no): ")
        if(ch.lower()=="no"):
            print("thanks for using this applictaion")
            break 
