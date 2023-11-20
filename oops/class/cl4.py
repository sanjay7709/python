# class method

class employee:
    @classmethod
    def getempcomp(cls):
        cls.cname="IBM"
        #employee.getcompplace()
        cls.getcompplace()   # calling class level method from another class  method
        ''' if the aboveis not specified we might get attribute error but we can explicitly call using
            in the below shown-(2)'''
    @classmethod
    def getcompplace(cls):
        cls.addr="bang"
        
        
    def getemp(self):
        self.empno=int(input("enter the employee number: "))
        self.empname=input("enter the employee name: ")
        #self.dispemp()
    
    def dispemp(self):
        print("*"*50)
        print("Employee no= {}".format(self.empno))
        print("Employee name= {}".format(self.empname))
        print("company name= {}".format(self.cname))
        self.getcompplace()  #--(2) calling class level method from instance method
        print("company addr= {}".format(self.addr))        
        print("*"*50)

employee.getempcomp()
e1=employee()
e1.getemp()
e2=employee()
e2.getemp()
print("first emp data")
e1.dispemp()
print("second emp data")
e2.dispemp()