# reduce()
# bigger quantity reducing to smaller quantity
# var=reduce(functionname,iterable_obj)
from functools import reduce
print("enter the list of elemnets: ")
lst=[int(x) for x in input().split()]
big=reduce(lambda x,y:x if (x>y) else y,lst)
sma=reduce(lambda x,y:x if (x<y) else y,lst)
res=reduce(lambda x,y:x+y,lst)
n=int(input("enter the natural numbers: "))
nat=reduce(lambda n,m:n*m,range(1,n+1))
print("sum={}".format(res))
print("biggest number={}".format(big))
print("smallest number={}".format(sma))
print("product of n natural numbers: {}".format(nat))


from functools import reduce
print("enter the text: ")
lst=[str(x) for x in input().split()]
res=reduce(lambda x,y:x+" "+y,lst)
print("concatenated({})={}".format(lst,res))

