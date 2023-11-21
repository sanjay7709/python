# let us assume there exists an university name and its location , acept and display university name and location
#assume a cllege which contains coll namge and location , accept and display 
#coll det along with university details
#assume dtudent no, name and marks, accept and display student det , colg and university det

class university:
    def getunivdet(self):
        self.uname= input("enter the university name: ")
        self.addr= input("enter the university adddr: ")
    def disp(self):
        print("university name: ",self.uname)
        print("university addr: ",self.addr)
        
class college(university):
    def getcoldet(self):
       self.colname= input("enter the college name: ")
       self.coladdr= input("enter the college adddr: ")
    def disp1(self):
        print("college name: ",self.colname)
        print("college addr: ",self.coladdr)
class student(college,university):
    def getstuddet(self):
        self.stno=int(input("enter the student no: "))
        self.sname=input("enter the student name: ")
        self.marks=float(input("enter the student marks: "))
        self.getunivdet()
        self.getcoldet()
    def disp2(self):
        print("*"*50)
        self.disp()
        self.disp1()
        print("student no: ",self.stno)
        print("student name: ",self.sname)
        print("student marks: ",self.marks)
        print("*"*50)

s=student()
s.getstuddet()
s.disp2()