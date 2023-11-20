# accept employee values from kbd andi nsert those values in emp tableby using classes and objects

import cx_Oracle
class emprec:
    @classmethod
    def compy(cls):
        cls.comp="IBM"
        cls.addr="bangl"
    
    def reco(self):
        con=cx_Oracle.connect("username/passwd@DNS/serviceid")
        cur=con.cursor()
        self.empno=int(input("enter the employee number: "))
        self.empname= input("enter the employee name: ")
        self.empsal=float(input("enter the employee sal= "))
        self.compy()  # calling class method
        qry= "insert into emp values(%d,'%s',%f,'%s','%s')"
        cur.execute(qry %(self.empno,self.empname,self.empsal,self.comp,self.addr))
        con.commit()
        if(cur.rowcount>0):
            print("The employee records inserted successfully")
        else:
            print("The record does not exists")

c1=emprec()
c1.reco()


# anothermethod


import cx_Oracle
class emprec:
    @classmethod
    def compy(cls):
        cls.comp="IBM"
        cls.addr="bangl"
        
    def getvalue(self):
        self.empno=int(input("enter the employee number: "))
        self.empname= input("enter the employee name: ")
        self.empsal=float(input("enter the employee sal= "))
        
    def reco(self):
        con=cx_Oracle.connect("username/passwd@DNS/serviceid")
        cur=con.cursor()
        self.getvalue()
        self.compy()  # calling class method
        qry= "insert into emp values(%d,'%s',%f,'%s','%s')"
        cur.execute(qry %(self.empno,self.empname,self.empsal,self.comp,self.addr))
        con.commit()
        if(cur.rowcount>0):
            print("The employee records inserted successfully")
        else:
            print("The record does not exists")

c1=emprec()
c1.reco()
