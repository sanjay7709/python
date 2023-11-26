"""
synchronization in multithreading
or
Deadlocks


Create an object of lock class:
    >. synt: throbj.Lock()
To acquire the lock
    > synt: trdobj.acquire()
to relase the Lock
    > synt: trdobj.release()
    """
    
#nonlockingex

import threading

def multab(n):
    print("-"*40)
    print("Thread name current: {}".format(threading.current_thread().name))
    print("multiply table for= {}".format(n))
    print("-"*40)
    for i in range(1,11):
        print("\t{}*{}={}".format(n,i,n*i))
    print("-"*40)

#main progr
t1=threading.Thread(target=multab,args=(10,))
t2=threading.Thread(target=multab,args=(14,))
t3=threading.Thread(target=multab,args=(17,))
t4=threading.Thread(target=multab,args=(67,))
# dispatch to funct
t1.start()
t2.start()
t3.start()
t4.start()
