# 1-n numbers by using oops approach with thread based 

import threading

class san(threading.Thread):
    def run(self):
        print("default name= {}".format(threading.current_thread().name))
        print("i am from san class")
        
class disp(san):
    def run(self):
        san.run(self)
        print("default name= {}".format(threading.current_thread().name))
        print("active count after start = {}".format(threading.active_count()))
        self.n=int(input("enter the num: "))
        for i in range(1,self.n+1):
            print(i)

print("default name= {}".format(threading.current_thread().name))
s=disp()
print("execution before start= {}".format(s.is_alive()))
print("active count before start = {}".format(threading.active_count()))
s.start()
print("execution after start= {}".format(s.is_alive()))
print("active count after start = {}".format(threading.active_count()))
s.join()
print("execution after finish= {}".format(s.is_alive()))
print("active count after finish = {}".format(threading.active_count()))
