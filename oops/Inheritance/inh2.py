"""
single inheritance
"""

class company:
    def getcomp(self):
        self.compname="osi"
        self.addr="itpl"
        self.pin=560066
    def disp1(self):
        print("\t{}\t{}\t{}".format(self.compname,self.addr,self.pin))
        
class employee(company):
    def empdet(self):
        self.empno=42
        self.empname="sanjay"
        self.empaddr="KR"
        self.empsal=10
        self.getcomp()
    
    def disp(self):
        print("\tEMPno\tempname\tempaddr\tsal")
        print("\t{}\t{}\t{}\t{}".format(self.empno,self.empname,self.empaddr,self.empsal))
        print("\tname\taddr\tpincode")

c=employee()
c.empdet()
c.disp()
c.disp1()
