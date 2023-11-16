n=input("enter the text line: ")
for i in n :
    #print(i, end ="")
    if (i not in ('aeiouAEIOU')):
        print("consonants in above text={}".format(i,end=" "))


# 2) map()
# ============================================
# old values are mapped to new values

# varname =mapp(functionmname, itetable_obj)
def hike(sal):
    sal=sal+sal*(2/100)
    return sal

print("enter the salary of list: ")
oldsallst=[float(x) for x in input().split() ]
# obj=map(hike,lst)
# print("new sal list={}".format(list(obj)))
#sal(1+0.02)
newsallst=list(map(lambda sal: sal*1.02,oldsallst))
print("*"*50)
print("\toldsallist\tnewsallist\t")
print("*"*50)
z=zip(oldsallst,newsallst)
for old,new in z:
    print("\t{}\t{}".format(old,round(new,2)))

# for i in oldsallst:
#     print(i)
# print("new list sal==using anony= {}".format(newsallst))
# for j in newsallst:
#     print(j)

# list of elemenst and obtains their squares
# ==============================================
print("Enter you list of elements: ")
lst1=[int(x) for x in input().split()]
lst2=list(map(lambda sq:sq**2,lst1))
lst3=list(map(lambda sq:sq**3,lst1))
print("*"*50)
print("\t numbers\tsquares\tcubes")
print("*"*50)
for n,o,c in zip(lst1,lst2,lst3):
    print("\t  {}\t\t{}\t{}".format(n,o,c))
print("*"*50)


# pos and neg squares

print("enter the elements seperated by space: ")
lst=[int(val) for val in input().split()]
poslist=map(lambda sq:sq**2,list(filter(lambda n:n>0,lst)))
neglist=map(lambda sq:sq**2,list(filter(lambda n:n<0,lst)))
print("*"*50)
print("\t+ve squares\t-ve squares")
print("*"*50)
for m,n in zip(poslist,neglist):
    print("\t{}\t{}".format(m,n))