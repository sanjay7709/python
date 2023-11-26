#pypr read muti tread app , there exists two threads, one thread generates list of even num and another
#generates odd um within num
"""
#oddeventhread.py
import functools
lst=[int(x) for x in input().split()]
el=list(filter(lambda x:x%2==0,lst))
print(el)
ol=list(filter(lambda x:x%2!=0,lst))
sel=functools.reduce(lambda x,y:x+y,el)
sol=functools.reduce(lambda x,y:x+y,ol)
print(sel)
print(sol)
"""

import threading
def even(n):
    print("Thread name= {}".format(threading.current_thread().name))
    for val in range(2,n+1,2):
        print("\t even= {}".format(val))

def odd(n):
    print("Thread name= {}".format(threading.current_thread().name))
    for val in range(1,n+1,2):
        print("\t odd= {}".format(val))

# main program
n=int(input("enter the value: "))
e1=threading.Thread(target=even,args=(n,))
o1=threading.Thread(target=odd,args=(n,))
#dispatch
o1.start()
e1.start()
print("Thread count= {}".format(threading.active_count()))
o1.join()
e1.join()
print("Thread count after completion= {}".format(threading.active_count()))