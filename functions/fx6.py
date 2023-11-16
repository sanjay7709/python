# Arguments and parameters
def disp(a,b): #a,b are formal parameters
    print(a)
    print(b)
    c=a+b  # c is local variable
    return c
a=float(input("enter first value: "))
b= float(input("enter second value: "))
x=disp(a,b) #a,b are actual Arguments -- also known as global variables

# The mechanism of Passing actual arguments to formal parameters from funct call to fucn defn is called Arugements
#  passing parameter

print("Positional parameters example")
def dispinfo(sn,sn1,sm):
    print("{}\t{}\t{}".format(sn,sn1,sm))
#mainprog
sno= int(input("enter the student no: "))
sname=input("enter the student name: ")
mark= float(input("enter the marks obtained: "))
dispinfo(sno,sname,mark)
#dispinfo(10,"san",78)
#number and order of argumnets must be same in func call and func defn
# -------------------------------------------------------------------
# 
print("Keyword parameter ")
def dispinfo(sn,sn1,sm,city="hyd"):
    print("{}\t{}\t{}".format(sn,sn1,sm,city))
#mainprog
sno= int(input("enter the student no: "))
sname=input("enter the student name: ")
mark= float(input("enter the marks obtained: "))
#dispinfo(sno,sname,mark)
dispinfo(10,"san",78,'hyd')
dispinfo(11,"nas",45,'hyd')
dispinfo(12,"der",30,'hyd')
# dispinfo(sname='san',12,43,"hyd") # Synt-error -positional parameter follows argument
# if there are many common values then mostly to reduce the execution time it ids prefewrref to use keyword parameter

# ------------------------------------------------------------------

# Default parameter
print("Default parameter ")
def dispinfo(sn,sn1,sm=30,city="hyd"):
    print("{}\t{}\t{}".format(sn,sn1,sm,city))
#mainprog
sno= int(input("enter the student no: "))
sname=input("enter the student name: ")
mark= float(input("enter the marks obtained: "))
#dispinfo(sno,sname,mark)
dispinfo(10,"san",78,'hyd')
dispinfo(11,"nas",45)
dispinfo(12,"der")

#variable length parameters

