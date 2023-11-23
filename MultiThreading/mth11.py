# using inheritance  (from n to 1)
import threading
class numprog(threading.Thread):
    def run(self):
        self.n=int(input("enter the number: "))
        print("thread name= {}".format(threading.current_thread().name))
        if(self.n<=0):
            print("invalid")
        else:
            print("*"*40)
            for i in range((self.n),0,-1): # range(n,0,-1)
                print(i)
            print("*"*40)

# main program
n=numprog()
n.start()

