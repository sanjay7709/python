import shares as s
import time,importlib
def disp(l):
    print("*"*50)
    print("sharename\tsharevalue")
    print("*"*50)
    for sn,sv in l.items():
        print("{}\t\t{}".format(sn,sv))

l=s.shareinfo()
disp(l)
print("going to sleep for 20 secs")
time.sleep(20)
importlib.reload(s)
print("coming out of sleep after 20 secs")
disp(l)
