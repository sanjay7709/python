#approach -1
import threading,time
def generate(n):
    
    print("name of thread= {}".format(threading.current_thread().name))
    for val in range(1,n+1):
        print(val)
# mainpypr
print("active count before start={}".format(threading.active_count()))
m1=threading.Thread(target=generate,args=((int(input("enter the number: "))),))
m1.name="rossum"
print("execution status of mu before start={}".format(m1.is_alive()))
m1.start()
print("execution status of mu after start={}".format(m1.is_alive()))
print("active count after start={}".format(threading.active_count()))
m1.join()
print("execution status of mu after completion={}".format(m1.is_alive()))
print("active count after completion={}".format(threading.active_count()))