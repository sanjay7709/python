# Anonymous functions or Lambda functions
# used to perform instant operations
# lambda ---> keyword

addop = lambda a,b: a+b

res=addop(10,20)
print(res)
print(type(addop))
# program
arect= lambda l,b : l*b
l,b=float(input("enter the length: ")),float(input("enter the breadth: "))
ar=arect(l,b)
print("Area of rect={}".format(ar))

# program-2

bigop=lambda a,b : a if a>b else b
threeop = lambda a,b,c : "values are equal" if (a==b) and (b==c) and (c==a) else a if (a>b)and(a>c) else b if(b>c)and(b>a) else c
print("biggest={}".format(bigop(20,40)))

#progr-3

lst=[10,20,30,40,-70,60,0,93]
big = lambda l: max(l)
smal=lambda k: min(k)

#program
print("enter list of values sepearted by space: ")
lst= [int(x) for x in input().split()]
print(lst)

