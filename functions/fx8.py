# global and local variables
# global variables is that to store common values for different function calls
# They are defuned before function calls

# local variables
# defined within the function body


#globals keyword

a=10
def inc():
    global a
    a=a+1
    print(a)

# globals() -- function

a=10
b=12
c=14
d=23
def dip():
    global c,d
    c=c+1
    d=d+1
    a=100
    b=120
dip()

globals()['a']
globals.get('a')
x=globals()  # dict