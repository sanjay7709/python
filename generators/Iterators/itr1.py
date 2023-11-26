#Iterators
""" 
Iterators
=========
To provid ethe values of list, str, dict ,s et on demand
"""

lst=[10,20,30,40,50,60,70,80,90]
for i in lst:
    print(i)
itrobj=iter(lst) # conevreting list obj to iterator obj
print(type(itrobj))
# print(next(itrobj))
# print(next(itrobj))
# print(next(itrobj))
while(True):
    try:
        print(next(itrobj))
    except StopIteration:
        break