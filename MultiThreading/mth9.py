# 1-n numbers by using oops approach with thread based 

import threading,time
#from threading import Thread
class san(threading.Thread):
    def run(self):
        self.n=int(input("enter the num: "))
        if(self.n<=0):
            print("invalid num")
        else:
            for i in range(1,self.n+1):
                time.sleep(1)
                print(i)

print("default name= {}".format(threading.current_thread().name))
s=san()
print("execution before start= {}".format(s.is_alive()))
print("active count before start = {}".format(threading.active_count()))
s.start()
print("execution after start= {}".format(s.is_alive()))
print("active count after start = {}".format(threading.active_count()))
s.join()
print("execution after finish= {}".format(s.is_alive()))
print("active count after finish = {}".format(threading.active_count()))
