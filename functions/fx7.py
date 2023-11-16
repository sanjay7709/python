#varlenparameters

# ERROR --- same function name then only latest function is considered
# def disp(n):
#     print("{} ".format(n))
# def disp(x,y):
#     print("{},{}".format(x,y))
# disp(10)
# disp(10,20)
# disp(10,20,30)
# disp(10,20,30,40)

#=-=========================================
# When we have family of function calls we need to define multiple times
# which is not good , same function with differing variable argumenets
def disp(n):
    print("{} ".format(n))
disp(10)
def disp(x,y):
    print("{},{}".format(x,y))
disp(10,20)
#========================================
#varlenparameters
def disp(*n): # here it holds the value in the form of tuple (immutable)
    print(type(n))
    print("number of elements={}".format(len(n)))
    # to access the elemenst in tuple
    for val in n:
        print("{}".format(val), end=" ")
    print()

disp(10)
disp(10,20)
disp(10,20,30,40)

# default must be used last 
# varlen parameter (*a) must be used last next to default 
# check for positional parameter
def disp(sname, *a, crs="python"):
    print(sname)
    print(crs)
    s=0
    for v in a:
        print(v, end=" ")
        s=s+v
    print(s)
disp("san",10,203,43)
#disp(10,40,30,sname="san")  # Type Error 
#disp("san",10,40,40,50,"JAVA") # again Type Error
#disp("san",crs="JAVA",10,-60,-50)# synatax error
#----------------------------------------------------
# Keyword variable length parameters
#=========================================
def disp(**a): # here the a holds dict value type
    print(a)
    print("type of a={}".format(type(a)))
    # for k,v in a.items():
    #     print("{}---{}".format(k,v))
    for i in a.items():
        print("{}---->{}".format(i[0],i[1]))
#mainprogram
disp(sno=10,sname="san",marks="100",crs="python")
disp(sno=10,sname="san",marks="100")
disp(sno=10,sname="san")
disp(sno=10)