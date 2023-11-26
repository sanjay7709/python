#train ex
import threading
class train:
    L=threading.Lock()
    def __init__(self,n):
        self.seats=n
    def reserve(self,nos):
        self.L.acquire()
        if(nos>self.seats):
            print("{} is unable to get {} seats".format(threading.current_thread().name,nos))
        else:
            self.seats=self.seats-nos
            print("{} is reserved for {} seats".format(threading.current_thread().name,nos))
        print(self.seats)
        self.L.release()

t=train(int(input("enter no of seats: ")))
t1=threading.Thread(target=t.reserve,args=(100,))
t2=threading.Thread(target=t.reserve,args=(15,))
t3=threading.Thread(target=t.reserve,args=(20,))
t4=threading.Thread(target=t.reserve,args=(5,))
# dispatch
t1.start()
t2.start()
t3.start()
t4.start()
        