#######***multi threading****############
'''
The Main program is executed by PVM which internallly create a main thread and it creates a sub thread
which executes the logic of operations inside the functions/method concurrently
is called thread based application

Thread---> a flow of control to execute/perform some operations inside functions/methods
module name ===> "threading"
functions in threadding module
==============================
1. current_thread()  --> finding the thread name  which is running
    >>> varname=threading.current_thread().name
2. active_count() ----> counting no of running threads
    >>> varname= threading.active_count()
NOTE: 
class name in threading module: Thread 
====================================
1) Thread(target(), arg(<>,)) --> This constructor is used for creating child thread by specifiying 
        target function which is executed by child thread and also specifying values passing to 
        target func in the form of tuple.
        synatx: threading.Thread(target=functionname,arg(val,val2...valn))
2) getName(str)--> deprectaed
3) setname() --> it is deprecated and we can use "name" instead
                synatx : obj.name="san"
4) run() -->  It is one of the null body method of thread class it is used for defining logic of pypr
                which is executed by child thread , This method must be overriten inside of
                sub class of thread class
            synt: class <classname> (threading.Thread):
                        def run(self):
                        ------------
                        ----------
                    
5) start() --> It is used for dispatching the child thread to corresponding function
                synt: childthread.start()
6) is_alive()--> Func returns true if thread is in execution 
            ---> else returns false if thread not yet started or alredy complted
                synt: trdobj.is_alive()
7) join()---> it is used for making the child thread join after their completion
                synt: childthread.join()

Number of approaches to develop thread based application
=========================================================
1) by using functional programming approach
>>  steps-1 : import module
>> step-2: define a function which conatins logic executed by child thread
>> step-3 : create an object of thread class===> child thread
>> step-4: dispatch the child thread 

additional:
>>> step-5: join the threads to evaluate active thread count if needed

2)by using sub class of thread class (inheritance)
>> step-1 : import module
>> step-2: choose programmer defined class
>> step-3: programmer defined classmust inherit from thread class
>> step-4: it must override the run(self) (null body method) of thread class executed by child thread
>> step-5 : we need to  craete an object of sub class of thread class --child thread  ####
>> step-6: dispatch the thread --using start() --> internally calls run()


3) by using non-sub class of thread class (without inheritance)
>> step-1: import module
>> step-2: choose programmer defined class
>> step-3: choose programmer defined method inside class with logic executed by child thread
>> step-4: create an object of programmer defined class
>> step-5: create the child thread class object of threding module
>> step-6 : dispatch the child using start() method

'''
import threading
dfname=threading.current_thread().name
print("number of active threads={}".format(threading.active_count()))
print("default thread= ",dfname)
print("program execution started")
print("hello mutli thread ")
print("program exec completed")