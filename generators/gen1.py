""" 
generators
============
it is a function()
if we want to develop our own functions and use it , instead of the default programmer defined functions 
we go for decorators


""yield""
=========

it will return the value to the object and once again will go back to the main function
to perform the operations

""next""
=======
it is a function to get the first value of the object


"""
print("*"*50)
print("using normal method")
print("*"*50)
for i in range(1,11):
    print(i)
print("*"*50)
print("generator method")
print("*"*50)
def sanrange(n,m):  #n==> lower bound, m==> upperbound
    while(n<=m):
        yield n
        n=n+1

obj=sanrange(100,200)
print("type ={}".format(type(obj)))
while(True):
    try:
        print(next(obj))
    except StopIteration:
        print("*"*50)
        break
