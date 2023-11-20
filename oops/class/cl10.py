#pickling and unpickling by using classes and objects
'''import pickle
class student:
    def studdeta(self):
        self.name=input("enter the name: ")
        self.no=int(input("enter the number: "))
        self.marks=float(input("enter the marks: "))

with open("dest.data","ab") as fp:
    s=student()
    s.studdeta()
    pickle.dump(s,fp)'''

import pickle,sys
from cl11 import student
class studentpick:
    def studval(self):
        try:
            while(True):
                with open("dest.data","ab") as fp:
                    self.sno=int(input("enter the number: "))
                    self.name=input("enter the name: ")
                    self.marks=float(input("enter the marks: "))
                    # create a class of student object
                    s=student()
                    s.setstudvalues(self.sno,self.name,self.marks)
                    # loading the data
                    pickle.dump(s,fp)
                    print("*"*50)
                    print("\n\trecord inserted successfully")
                    print("*"*50)
                    ch=input("Do you want to enter another record (yes/no): ")
                    if(ch.lower()=="no"):
                        print("Thanks for using this application")
                        sys.exit()
        except ValueError:
            print("Dont enter str, symbnols or alpha numeric chars")

sp=studentpick()
sp.studval()