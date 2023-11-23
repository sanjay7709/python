import threading,time
def squares(n):
    tname1=threading.current_thread().name
    print("defualt thread ={}".format(tname1))
    for val in n:
        print(" squares({})={}".format(val,val**2))

def cubes(n):
    tname2=threading.current_thread().name
    print("defualt thread ={}".format(tname2))
    for val in n:
        print(" cubes({})={}".format(val,val**3))

bt=time.time()
dfname=threading.current_thread().name
print("defualt thread ={}".format(dfname))
print("Enter the numbers of list sepearated by space")
l=[int(x) for x in input().split()]
f=list(filter(lambda x:x>0,l))
sqt=threading.Thread(target=squares,args=(f,)) # creating child threads
cqt=threading.Thread(target=cubes,args=(f,)) # creating child threads
# squares(f)
# cubes(f)
sqt.name="squ"
cqt.name="cubb"
sqt.start()
cqt.start()
sqt.join()
cqt.join()
print("number of active threads={}".format(threading.active_count()))
et=time.time()
print("The total time taken ={}".format(et-bt))
