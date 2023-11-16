# ;list of employee sal 1-20000 and above give 20% hike more than 10000 and 25% hike for more than less than 10000
# finf the total salary
# using 
from functools import reduce
print("enter the list of elemnets: ")
lst=[int(x) for x in input().split()]
tm=map(lambda sal:sal*1.2,filter(lambda n:n>10000,lst))
lm=map(lambda sal:sal*1.25,filter(lambda n:n<10000,lst))
for i in tm:
    print(i)
for j in lm:
    print(j)
print("*"*50)
print("original salary list: {}".format(lst))
print("*"*50)
print("\tsal>10000\tsal<10000")
# Zip function takes equal number of elements
for m,n in zip(tm,lm):
    print("\t{}\t\t{}".format(m,n))
print("*"*50)
sl=reduce(lambda x,y:x+y,(map(lambda sal: sal+sal*0.25,filter(lambda n:n<10000,lst))))
ll=reduce(lambda x,y:x+y,(map(lambda sal: sal+sal*0.2,filter(lambda n:n>10000,lst))))
print("sum of sal>10000 = {}".format(ll))
print("sum of sal<10000 = {}".format(sl))
print("*"*50)