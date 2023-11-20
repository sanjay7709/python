'''
class employee:
    def getempval(self):pass
    def dispemp(self):pass

e1=employee()
e1.getempval()  # we dont need to call this method explcitly since in constructors
                we canuse it implicitly

'''
class employee:
    def __init__(self):
        self.eno=int(input("enter the eno: "))
        self.ename=input("enter the name: ")
        self.esal=float(input("enter the sal: "))
        
    def dispval(self):
        print("\tEmployee details")
        print("\tSno\tName\tSal")
        print("\t{}\t{}\t{}".format(self.eno,self.ename,self.esal))
        # print("employee number: {}".format(self.eno))
        # print("employee name: {}".format(self.ename))
        # print("employee sal: {}".format(self.esal))

e1=employee()
e2=employee()
e1.dispval()
e2.dispval()
