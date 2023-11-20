'''class student:
    def readdata(self):
        print(" inside is of self = {}".format(id(self)))

s1=student()
s2=student()
s1.readdata()
s2.readdata()
print("idof s1= ",id(s1))
print("idof s2= ",id(s2))'''

class student:
    def readdata(self):
        self.sno=int(input("enter the student number: "))
        self.sname=input("enter the student name: ")
        self.marks=float(input("enter the marks: "))
        # print("Student Details")
        # print("*"*50)
        ''' calling instance method from another insatnce method'''
        # self.disp()   
        # print("*"*50)
        
    
    def disp(self):
        print("student number:{} ".format(self.sno))
        print("student name:{} ".format(self.sname))
        print("student marks:{} ".format(self.marks))

s1=student()
s1.readdata()
print("*"*50)
print("Student Details")
print("*"*50)
s1.disp()
print("*"*50)
