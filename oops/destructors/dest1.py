'''
        destructor
        =============
    syntax: def __del__(self)
internally executed by garbage collector , it has inbuild del function in it

Destructor will clean up/deallocate unsused memory space at the end of program


'''
import time
class employee:
    def __init__(self):
        print("iam from constructor")
        self.no=10
        self.name="velo"
        print("\t{}\t{}".format(self.no,self.name))
    
    def __del__(self):
        print(" gc ccallss ")

e01=employee()
e01=None  # force fully calling gc
e02=e01  # Deep copy
del e01  # here gc will not __del__(self) , because two objects e01, e02 are pointing to same addr
         # so if we remove one then other one is pointing
del e02  # now it will call gc __del__(Self) , becuase no objects pointto eo2 
        #
# e02=employee()
# del e02
# e03=employee()
# time.sleep(10)

'''
NOTE: do not disable garbage collector
gc is pre-defined module
 import gc
 gc.isenabled()
 gc.disable()  # not having its meaning in higher versions
 gc.enable()
'''