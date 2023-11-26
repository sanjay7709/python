#oops without inheritancelocking ex -- constructors
import threading
class locking:
    @classmethod
    def getval(cls):
        cls.l=threading.Lock()
    def __init__(self,n):
        self.n=n
    def multab(self):
        self.l.acquire() #step-2
        #self.n=int(input("enter the number: "))
        print("-"*40)
        print("Thread name current: {}".format(threading.current_thread().name))
        print("multiply table for= {}".format(self.n))
        print("-"*40)
        for i in range(1,11):
            print("\t{}*{}={}".format(self.n,i,self.n*i))
        print("-"*40)
        self.l.release() #step-3

#main progr
#k=threading.Lock()
#l=threading.Lock()
locking.getval()
m1=locking(12)
m2=locking(43)
m3=locking(54)
m4=locking(65)
t1=threading.Thread(target=m1.multab)
t2=threading.Thread(target=m2.multab)
t3=threading.Thread(target=m3.multab)
t4=threading.Thread(target=m4.multab)

t1.start()
t2.start()
t3.start()
t4.start()