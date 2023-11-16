# method--1
import md3 as m,calendar as k
m.area()
m.peri()
print(k.month(2023,5))
# for i in dir(m):
#     print(i)

# method-2
from md3 import *  # it provides required variables names and classes but also uninterested variables also , thus
                    # Takes more memory space and execution time
area()
peri()