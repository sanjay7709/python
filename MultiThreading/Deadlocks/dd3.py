#oops locking ex
import threading
class locking(threading.Thread):
    l=threading.Lock()  # class level datamemeber --step-1
    def setvalue(self,n):
        self.n=n
    def run(self):
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
t1=locking()
t1.setvalue(14)
t2=locking()
t2.setvalue(16)
t3=locking()
t3.setvalue(17)
t4=locking()
t4.setvalue(94)
t1.start()
t2.start()
t3.start()
t4.start()
