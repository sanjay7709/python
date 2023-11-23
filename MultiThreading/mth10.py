# Approach-3
## Non sub class of thread class (without inheritance)
import threading
class sample:
    def show(self):
        print("default name= {}".format(threading.current_thread().name))
        self.n=int(input("enter the num: "))
        if(self.n<=0):
            print("invalid num")
        else:
            for i in range(1,self.n+1):
                print(i)
c=sample()
c1= threading.Thread(target=c.show) # child thread
c1.name="SAMPLE"
c1.start() # dispatch it to class