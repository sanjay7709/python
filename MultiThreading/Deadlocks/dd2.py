#lockingex

import threading
def multab(n):
    k.acquire()
    print("-"*40)
    print("Thread name current: {}".format(threading.current_thread().name))
    print("multiply table for= {}".format(n))
    print("-"*40)
    for i in range(1,11):
        print("\t{}*{}={}".format(n,i,n*i))
    print("-"*40)
    k.release()

#main progr
k=threading.Lock()
t1=threading.Thread(target=multab,args=(10,))
t2=threading.Thread(target=multab,args=(14,))
t3=threading.Thread(target=multab,args=(17,))
t4=threading.Thread(target=multab,args=(67,))
# dispatch to funct
t1.start()
t2.start()
t3.start()
t4.start()