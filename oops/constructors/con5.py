#pickling conept using constructors
from con4 import student
import pickle,sys
class stud1:
    def __init__(self):
        while(True):
            try:
                with open("cons.data","ab") as fp:
                    self.sno=int(input("enter the student number: "))
                    self.sname=input("enter the student name: ")
                    self.marks=float(input("enter the student marks: "))
                    s=student(self.sno,self.sname,self.marks)
                    pickle.dump(s,fp)
                    print("*"*50)
                    print("Records inserted successfully")
                    print("*"*50)
                    ch=input("Do you want to enter another record (yes/no): ")
                    if(ch.lower()=="no"):
                        print("Thanks for using this application")
                        sys.exit()
            except FileExistsError:
                print("files already exists")
sp=stud1()
            