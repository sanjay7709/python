#oops without inheritancelocking ex
import threading
class locking:
    # def setvalue(self,n):
    #     self.n=n
    def multab(self,n):
        l.acquire() #step-2
        #self.n=int(input("enter the number: "))
        print("-"*40)
        print("Thread name current: {}".format(threading.current_thread().name))
        print("multiply table for= {}".format(n))
        print("-"*40)
        for i in range(1,11):
            print("\t{}*{}={}".format(n,i,n*i))
        print("-"*40)
        l.release() #step-3

#main progr
#k=threading.Lock()
l=threading.Lock()
m1=locking()
m2=locking()
m3=locking()
m4=locking()
t1=threading.Thread(target=m1.multab,args=(12,))
t2=threading.Thread(target=m2.multab,args=(16,))
t3=threading.Thread(target=m3.multab,args=(19,))
t4=threading.Thread(target=m4.multab,args=(22,))

t1.start()
t2.start()
t3.start()
t4.start()