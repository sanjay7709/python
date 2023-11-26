def func1():
    return "hello"

def gen():
    s="hello"
    i=0
    while(i<len(s)):
        yield s[i]
        i=i+1
        
#main program
print("type of obj= {}".format(type(func1)))
obj=func1()
print(obj)
print("============================")
print("type of obj= {}".format(type(gen)))
obj=gen()
print(next(obj))
