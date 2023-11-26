#space.py
#lists vs numpy

import numpy as np,sys

l=[10,20,30,40,50,60,7,77,8,34,56,9,78,99,0,2,87,54,42,25]
a=np.array([10,20,30,40,50,60,7,77,8,34,56,9,78,99,0,2,87,54,42,25])
print("list type ={}".format(type(l)))
print("array type ={}".format(type(a)))
print("memory space taken by list ={}".format(sys.getsizeof(l)))
print("memory space taken by array ={}".format(sys.getsizeof(a)))


# vector operations

l=[10,20,30,40]
#l+2  # here we get error
a=np.array([[10,20],[30,40]])
print(a+2)
