#print pos and neg elemenst in list
import numpy as np
print("Enter the elemenst of the list: ")
lst=[int(val) for val in input().split()]
print("*"*50)
print("elements of list:")
print("*"*50)
for i in lst:
    print(i, end=" ")
print("*"*50)
# array of list
a=np.array(lst)
print("positive elemenst of list: {}".format(a[a>0])) 
print("negative elemenst of list: {}".format(a[a<0])) 
print("Even elemenst of list: {}".format(a[a%2==0])) 
print("odd elemenst of list: {}".format(a[a%2!=0])) 
print("*"*50)