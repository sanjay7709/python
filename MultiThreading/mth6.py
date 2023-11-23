#pypr mul table using threads (use functional approach)

import threading
def mul(*n):
    print("name of thread= {}".format(threading.current_thread().name))
    for val in n:
        print("multiplication table for = {}".format(val))
        for i in range(1,11):
            print("{}*{}={}".format(val,i,val*i))

#main pypr
print("active count before start={}".format(threading.active_count()))
print("name of thread= {}".format(threading.current_thread().name))
mu=threading.Thread(target=mul,args=((int(input("enter the number: ")),)))
print("execution status of mu before start={}".format(mu.is_alive()))
mu.start()
print("execution status of mu after start={}".format(mu.is_alive()))
mu.name="multiply-new"
print("active count after start={}".format(threading.active_count()))
mu.join()
print("execution status of mu after completion={}".format(mu.is_alive()))