# start , stop and step generator
print("*"*50)
print("generator method")
print("*"*50)
def sanrange(n,m,p):  #n==> lower bound, m==> upperbound
    while(n<=m):
        yield n
        n=n+p

obj=sanrange(100,200,4)
print("type ={}".format(type(obj)))
while(True):
    try:
        print(next(obj))
    except StopIteration:
        print("*"*50)
        break
