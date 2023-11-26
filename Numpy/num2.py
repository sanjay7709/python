# arithmetic operations on matrices using numpy

import numpy as np
l1=[10,20,30,40]
l2=[1,2,3,4]
a1=np.array(l1)
b1=np.array(l2)
a=a1.reshape(2,2)
b=b1.reshape(2,2)
print("First matrix:")
for i in a:
    print("\t{}".format(i))
print("second matrix:")
for i in b:
    print("\t{}".format(i))
print("{}+\n{}=\n{}".format(a,b,a+b))
print("{}+\n{}=\n{}".format(a,b,a-b))
print("{}+\n{}=\n{}".format(a,b,a*b))  # element wise multiplicsation # not correct
print("actual multiplication method is : ")
print("{}+\n{}=\n{}".format(a,b,(np.dot(a,b)))) 
print("{}+\n{}=\n{}".format(a,b,a/b))  
print("{}+\n{}=\n{}".format(a,b,a%b))
print("{}+\n{}=\n{}".format(a,b,a**b))    