# without inheritance non sub class
#from n to 1 numbers
import threading #step-1
class numprog: #step-2
    def generate(self,n):
        self.n=n
        print("thread name= {}".format(threading.current_thread().name))
        if(self.n<=0):
            print("invalid")
        else:
            print("*"*40)
            for i in range((self.n),0,-1):  # step-3
                print(i)
            print("*"*40)

# main program
n=numprog() # step-4
t=threading.Thread(target=n.generate,args=(int(input("enter the number: ")),)) #step-5
t.start() # step-6