'''
whenever we create an object it as to initialized instead of explicitly calling it 
by calling implicitly by pvm that special method is called constructor

methods-- are meant for peroforming someoperations
purpose of constructors
=======================
 To initialize the object or it is always used for placing our  own values in the object.
 
 Definition
 ===========
 A constructor is one of the special method which is implictly called by pvm during object creation 
 whose role is  to placeour own values in object without empty
 
 syntax
 ========
 >>  def __init__(self,list of formal param):
       ----- block of statements------------
 >> A constructor has instane nature and it can also be class level method nature
 >>constructor must start wit __init__(self)
 
 constructors ---------------------------------method
 1. it can initialize the object |  methods can toperform someoperations on object
 2. __init__(self)               |  methods starts with method name ()
 3.implictily calling            | explicitly calling

Types
=====
1.Default constructor / parameter less constructor/ do nothing parameter
    >> does not take any value except self
    >> syntax --  def __init__(self):   # not taking any params
                    -------BOS-------
    >> purpose: to initialize multiple objects with same class with same values
            class test:
                def __init(self):
                 self.a=10
                 self.b=20
            t1=test()
            print(t1.__dict__)
            t2.test()
            t3.test()  
            # all objects are initialised with same values. 
2.parameterized constructor
        class test:
            def __init__(self,a,b):
                self.a=a
                self.b=b
        t1-test(12,24)
        print(t1.__dict__)
        t2.test(100,200)
        t3.test(54,64)

Mulitple values of same class 
## it takes the default values in the below example if not passing .......
class test:
    def __init__(self,a=100,b=200):
        self.a=a
        self.b=b
t1=test()
t2=test(12,43)
t3=test(b=87,a=90)
t4=test(b=099)
'''