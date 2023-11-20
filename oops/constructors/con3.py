# employee details using constructors

class employee:
    
    @classmethod
    def getcompname(cls):
        cls.comp="MICR"
        cls.addr="pune"
    
    def __init__(self):
        while(True):
            try:
                self.empno=int(input("enter the empno: "))
                self.empname=input("enter the employee name: ")
                self.getcompname()
                ch=input("do you wnat to enter another record (yes/no): ")
                if(ch.lower()=="no"):
                    print("Thanks for using this application")
                    break
                else:
                    self.disp()
            except ValueError:
                print("Dont enter str symbols or alpha numeric chars")
    
    def disp(self):
        print("*"*50)
        print("Employee details")
        print("*"*50)
        print("\tSno\tname\tcomp\taddr")
        print("*"*50)
        print("\t{}\t{}\t{}\t{}".format(self.empno,self.empname,self.comp,self.addr))
        print("*"*50)

c1=employee()
