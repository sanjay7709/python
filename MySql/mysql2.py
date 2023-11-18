import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",username=" ",passwd=" ")
    print("connection is established")
    cur=con.cursor()
    dbname= input("enter the database name: ")
    qry="create database %s"  
    obj=cur.execute(qry %dbname)
    print("the database is created")
except mysql.connector.DatabaseError as db:
    print("problem in db ", db)
    

import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",username=" ",passwd=" ",databse="")
    print("connection is established")
    cur=con.cursor()
    #tabe = input("enter the table name: ")
    qry="create table employee (eno int(3) primary key, ename varchar(10) not null, salary real not null)"
                # real can be (double or float)
    obj=cur.execute(qry)
    print("the table is created")
except mysql.connector.DatabaseError as db:
    print("problem in db ", db)
    
#[program -3]
import mysql.connector
def inserec1():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",username=" ",passwd=" ",databse="")
            print("connection is established")
            cur=con.cursor()
            #tabe = input("enter the table name: ")
                        # real can be (double or float)
            eno=int(input("enter the emono: "))
            empname=input("enter the emp name: ")
            esal=float(input("enter the emp sal: "))
            qry = "insert into employee values(%d,%s,%f)"
            obj=cur.execute(qry %(eno,empname,esal))
            con.commit()
            if(cur.rowcount>0):
                print("the employee record is inserted")
            else:
                print("no records exists")
            print("*"*50)
            ch=input("Do you want to enter another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("thanks for using this application! ")
                break
                
        except mysql.connector.DatabaseError as db:
            print("problem in db ", db)

inserec1()


#[program -4]
import mysql.connector
def delrec1():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",username=" ",passwd=" ",databse="")
            print("connection is established")
            cur=con.cursor()
            #tabe = input("enter the table name: ")
                        # real can be (double or float)
            eno=int(input("enter the emono: "))
            qry = "delete from employee where empno=%d"
            obj=cur.execute(qry %(eno))
            con.commit()
            if(cur.rowcount>0):
                print("the employee record deleted")
            else:
                print("no records exists")
            print("*"*50)
            ch=input("Do you want to delete another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("thanks for using this application! ")
                break
                
        except mysql.connector.DatabaseError as db:
            print("problem in db ", db)

delrec1()


#[program -5]
import mysql.connector
def updrec1():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",username=" ",passwd=" ",databse="")
            print("connection is established")
            cur=con.cursor()
            #tabe = input("enter the table name: ")
                        # real can be (double or float)
            eno=int(input("enter the employee no: "))
            hsal=float(input("enter the salary"))
            qry = "update employee set sal=sal+sal*(%f/100) where eno=%d"
            cur.execute(qry %(hsal,eno))
            con.commit()
            if(cur.rowcount>0):
                print("the employee record updated")
            else:
                print("no records exists")
            print("*"*50)
            ch=input("Do you want to update another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("thanks for using this application! ")
                break
                
        except mysql.connector.DataBaseError as db:
            print("problem in db ", db)

delrec1()