from math import sqrt
def square():
    x=float(input("enter the number: "))
    #c= x**(1/2)
    c=sqrt(x)
    return x,c

a,b =square()
print("square root of given number {}= {}".format(a,b))



def rect(d,e):
    k=d*e  #length*breadth
    l= 2*(d+e)  #2*(lenghth+breadth)
    return k,l

m,n=float(input("enter the length of rectangle")),float(input("enter the breadth: "))
c,g=rect(m,n)
print("area of rectangle is {}*{}= {}".format(m,n,c))
print("perimeter of rectangle : {}".format(g))

def swap():
    a,b=input("enter the two numbers: "),input("Enter two numbers: ")
    c=a
    a=b
    b=c
    print("the swapped values are = {},{}".format(a,b))

swap()


def squa(x):
    ar= x**2
    pr= 4*x
    return ar, pr

x= float(input("enter the side: "))
e,f = squa(x)
print("Area of square: {}".format(e))
print("perimieter of square: {}".format(f))    


