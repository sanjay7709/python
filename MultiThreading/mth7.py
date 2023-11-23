# approach no--2

import threading

class san(threading.Thread):
    def run(self):
        print("default name= {}".format(threading.current_thread().name))
        print("i am from san class")

print("default name= {}".format(threading.current_thread().name))
s=san()
print("execution before start= {}".format(s.is_alive()))
s.start()
print("execution after start= {}".format(s.is_alive()))