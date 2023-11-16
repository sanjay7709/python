Approach-1
# Not taking value but returning value
#  RV ---- NTV
#  def add():
#     x,y=int(input("enter the number1: ")),int(input("enter the number2: "))
#     c=x+y
#     return c

# c= add()
# print("value of two numbers: {}".format(c))

Approach-2
# Taking value returning value
#  RV --- TV
# def add(x,y):
#     c=x*y
#     return c

# x,y=int(input("enter the number1: ")),int(input("enter the number2: "))
# r1=add(x,y)
# print("the value of two numbers: {}".format(r1))

Approach -3
# not returning value not taking value
# NTV ------ NRV
# def add():
#     x,y=int(input("enter the number1: ")),int(input("enter the number2: "))
#     c=x+y   
#     print("value is : {}".format(c))

# add()

Approach-4
# taking value but not returning value

# TV ---- NRV
# def add(x,y):
#     c=x+y
#     print(c)

# x,y=int(input("enter the number1: ")),int(input("enter the number2: "))
# add(x,y)


# Approach-1
# (more than one value to return)
# return statement can return one or more number of values

def add():
    x,y=int(input("enter the number1: ")),int(input("enter the number2: "))
    c=x+y
    return x,y,c

a,b,c= add()
#or
a=add()
print(a,type(a))   # class <tuple>
print("sum of {} and {} is : {}".format(a[0],a[1],a[2]))
print("value of two {} and {} numbers: {}".format(a,b,c))

