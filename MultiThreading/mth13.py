# accept the line of txt and display each charc afer every scond
'''
import threading,time

class text:
    def accept(self):
        print("thread name={}".format(threading.current_thread().name))
        self.indata=input("enter the line of text: ")
        for i in range(len(self.indata)):
            print(self.indata[i])
            time.sleep(1)
# mainprogram
t=text()
t1=threading.Thread(target=t.accept)
t1.start()


import threading,time
def accept():
    print("thread name={}".format(threading.current_thread().name))
    indata=input("enter the line of text: ")
    ch=input("enter the char to search: ")
    
    for i in indata:
        print(i)
    count=0
    for k in list(indata):
        if(k==ch):
            count+=1
    print("{} occurance={}".format(ch,count))

           
            
        #time.sleep(1)
    
        
# mainprogram
t1=threading.Thread(target=accept)
t1.start()
'''

import threading,time
class char(threading.Thread):
    def run(self):
        print("thread name={}".format(threading.current_thread().name))
        indata=input("enter the line of text: ")
        l=list(indata)
        for i in indata:
            print("\t{} in occurancers ={}".format(i,l.count(i)))
            #time.sleep(1)
    
        
# mainprogram
t1=char()
t1.start()

