# static data
import cx_Oracle
try:
    con=cx_Oracle.connect("username/password@dns/serviceid")
    cur=con.cursor()
    qry="insert into table values(111,'san',90,'aspen')"
    cur.execute(qry)
    con.commit() # always commit when DML query is mentioned
    print("The record inserted successfully")
except cx_Oracle.DatabaseError as db:
    print("problem in db ",db)

# dynamic insertion DML 
import cx_Oracle
try:
    con=cx_Oracle.connect("username/password@dns/serviceid")
    cur=con.cursor()
    sno=int(input("enter the number: "))
    sname=input("Enter the name: ")
    smarks=float(input("enter the marks: "))
    col=input("enter the college: ")
    qry = "insert into student values (%d,'%s',%f,'%s')"  # take care of quotes single
    cur.execute(qry %(sno,sname,smarks,col))
    con.commit()
    print("The record {} inserted successfully".format(cur.rowcount))
except cx_Oracle.DatabaseError as db:
    print("problem in db ",db)

# method-3
import cx_Oracle,sys
while(True):
    try:
        con=cx_Oracle.connect("username/password@dns/serviceid")
        cur=con.cursor()
        sno=int(input("enter the number: "))
        sname=input("Enter the name: ")
        smarks=float(input("enter the marks: "))
        col=input("enter the college: ")
        qry = "insert into student values (%d,'%s',%f,'%s')"  # take care of quotes single
        cur.execute(qry %(sno,sname,smarks,col))
        con.commit()
        print("The record {} inserted successfully".format(cur.rowcount))
        print("*"*50)
        ch=input("Do you want to enter another record (yes/no): ")
        print("*"*50)
        if(ch.lower()=="no"):
            print("thanks for using this application! ")
            break
    except cx_Oracle.DatabaseError as db:
        print("problem in db ",db)


# method-4 : functions
import cx_Oracle,sys
def studinsert():
    while(True):
        try:
            con=cx_Oracle.connect("username/password@dns/serviceid")
            cur=con.cursor()
            sno=int(input("enter the number: "))
            sname=input("Enter the name: ")
            smarks=float(input("enter the marks: "))
            col=input("enter the college: ")
            qry = "insert into student values (%d,'%s',%f,'%s')"  # take care of quotes single
            cur.execute(qry %(sno,sname,smarks,col))
            con.commit()
            print("The record {} inserted successfully".format(cur.rowcount))
            print("*"*50)
            ch=input("Do you want to enter another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("thanks for using this application! ")
                break
        except cx_Oracle.DatabaseError as db:
            print("problem in db ",db)

studinsert()  # function call