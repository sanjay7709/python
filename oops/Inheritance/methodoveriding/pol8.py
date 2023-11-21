# Abstract class

class banking:  # abstract class
    def openac(self,name):pass
    def deposit(self,damt):pass
    def loan(self,name,lamt):pass   # null body methods ^^
    
class ravi(banking):
    def loan(self,name,lamt):
        print("{} took load of amt {} and went out of india".format(name,lamt))

class person(banking):
    def openac(self,name):
        print("{} opens a new account".format(name))
    def deposit(self,damt):
        print("{} amount is deposited in accxxx".format(damt))

r=ravi()
r.loan("vmalay",2.4)

p=person()
p.openac("sanjay")
p.deposit(5000)