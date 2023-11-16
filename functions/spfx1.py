# special functiuons

print("*"*50)
print("\t Special functions")
print("*"*50)
print("\t1.filter() functions")
print("\t2.map() functions")
print("\t3.reduce() functions")

#filter()
# synatax 
# varname =filter(functionanme, iterable_object)
print("By using Normal funcctions")
print("Enter the list of elements sepearted by space: ")
lst=[int(x) for x in input().split() ]
print(lst)
def decid(n):
    if(n>0):
        return True
    else:
        return False
pos=filter(decid,lst)
# convert filetr type to list type
pslist=list(pos)
print(pslist)
print("By using Anonysmous funcctions")
print("Enter the list of elements sepearted by space: ")
lst=[int(x) for x in input().split() ]  # list comprehension
print(lst)
#decid= lambda n:  True if n>0 else False
decid = lambda n: n>0
pos=filter(decid,lst)
# convert filetr type to list type
pslist=list(pos)
print(pslist)

#=================================================================
# another method
print("Another method --using single line of code ")
print("Enter the list of elements sepearted by space: ")
print(list(filter(lambda n: n>0,[int(x) for x in input().split()])))
print("Enter the list of elements sepearted by space: ")
print("positive elements of = {}".format(tuple(filter(lambda n: n>0,[int(x) for x in input().split()]))))
print("negative elements of = {}".format(tuple(filter(lambda n: n<0,[int(x) for x in input().split()]))))

print("By using Anonysmous funcctions")
print("Enter the list of elements sepearted by space: ")
lst=[int(x) for x in input().split() ] 
print("even elements of = {}".format(tuple(filter(lambda n: n%2==0,lst))))
print("odd elements of = {}".format(tuple(filter(lambda n: n%2!=0,lst))))

