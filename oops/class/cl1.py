"""
Class
========
Collection of datamenbers, methods, constructors etc.,,
It is used to develop programmer defined datatypes
in simple class is like a folder and objects are created inside it
Method --> functions defined inside a class is called a method

While creating a "class" -memory space is not allocated
and while creating an object -- > memory space is allocated

class Student: pass
s1=Student()   # object creation
To get the content of the object 
    >> print("contentof s1= ",s1.__dict__)
        "obj.__dict__" 
    o/p>
        content of s1= {}   #empty
        type(s1.__dict__)   #dict
        len(s1.__dict__) #len = 0

NOTE: 
        self == > it is an implicit object defined inside function def within class
                first formal parameter used inth instance method
        containing the id and memory address space as the object created w.r.to the class

types of datamembers
====================
1) Instance level 
>> used for storing specifi values
>> specific memory space is created for each and every object
>> 3-ways
    1) through object name
    2)instance method name
    3) constructors
>> can be accessed using object name or self
    objname.instancedatamember
    self.instancedatamember

2) Class level
>> used for storing  commmon values
>> inside of clas definition and inside of class method
>>they are available to all object
>> access them using classname or objectname or cls
>> only once the memory space is created and the it is used for common for all objects

Types of methods
================
1) Instance method 
>>  self as the first parameter , used to perform specific operations
    self.instancemethod()
    obj.instancemethod()
    
    def instancemethod(self):
        
2) Class method
>> used to perform classlevel operations
    it always takes "cls" as the first positional parameter for obtaining current clas name
    syntax = cls.classlevelmethodname()
            obj.classlevelmethodname()
            classname.classlevelmethodname()
            self.classlevelmethodname()

    here it should preceed with a decorator called "@classmethod"
        @classmethod
        def classmethod(cls):

3) static method
>>  Utility operation

it takes obj as the first positional parameter neither self nor cls
syntax : obj.staticmethodname()


"""