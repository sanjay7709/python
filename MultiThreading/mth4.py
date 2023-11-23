#pypr

import threading,time

class threadd:
    def fer(self):
        print("name of default thread = {}".format(threading.current_thread().name))
        for i in range(1,11):
            time.sleep(1)
            print(i)
print("name of default thread = {}".format(threading.current_thread().name))
c=threadd()
dname=threading.Thread(target=c.fer,args=()) #creating child thread
dname.start() # dispatching the child thread 

'''
class thread:
    def __init__(self):
        print("i am from init__ block")
        self.n= int(input())
        print("name of default thread = {}".format(threading.current_thread().name))
        self.d=threading.Thread(target=self.disp)
        self.d.start()
        for i in range(1,(self.n)+1):
            #time.sleep(1)
            print(i)
        

           
class inher(thread):
    def disp(self):
        
        print("i am from inher block")
        print("name of default thread = {}".format(threading.current_thread().name))

       
        print("name of default thread = {}".format(threading.current_thread().name))

c=inher()
c.disp()
'''

            