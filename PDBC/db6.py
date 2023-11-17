# read/select all employee records from employee table
import cx_Oracle,sys
def selectrec():
    while(True):
        try:
            con=cx_Oracle.connect("username/password@DNS/serviceid")
            cur=con.cursor()
            qry="select * from employee"
            # rec=cur.execute(qry) 
            # print(rec,type(rec))
            # rec.fetchone()# tuple
            # for i in rec:
            #     print(i, end= " ")
            # print()
            rec=cur.execute(qry)
            while(True):
                rec.fetchone() 
                if(rec==None):
                    break
                else:
                    for val in rec:
                        print(val,end="")
                    print()           
            con.commit()
            if(cur.rowcount>0):
                print("employee records listed")
            else:
                print("employee records not found")
            print("*"*50)
            ch=input("do you want to update another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("Thanks for using this application! ...")
                sys.exit()
        except cx_Oracle.DatabaseError as db:
            print("Problem in db", db)

selectrec()

# using fetch many(no of records)

import cx_Oracle,sys
def selectrec():
    while(True):
        try:
            con=cx_Oracle.connect("username/password@DNS/serviceid")
            cur=con.cursor()
            qry="select * from employee"
            # rec=cur.execute(qry) 
            # print(rec,type(rec))
            # rec.fetchone()# tuple
            # for i in rec:
            #     print(i, end= " ")
            # print()
            rec=cur.execute(qry)
            n=int(input("enter the number of records"))
            while(True):
                rec.fetchmany(n) 
                if(rec==None):
                    break
                else:
                    for val in rec:
                        for j in val:
                            print(j,end="")
                        print()           
            con.commit()
            if(cur.rowcount>0):
                print("employee records listed")
            else:
                print("employee records not found")
            print("*"*50)
            ch=input("do you want to update another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("Thanks for using this application! ...")
                sys.exit()
        except cx_Oracle.DatabaseError as db:
            print("Problem in db", db)
selectrec()

# using fetch all()
import cx_Oracle,sys
def selectrec():
    while(True):
        try:
            con=cx_Oracle.connect("username/password@DNS/serviceid")
            cur=con.cursor()
            qry="select * from employee"
            # rec=cur.execute(qry) 
            # print(rec,type(rec))
            # rec.fetchone()# tuple
            # for i in rec:
            #     print(i, end= " ")
            # print()
            rec=cur.execute(qry)
            n=int(input("enter the number of records"))
            while(True):
                rec.fetchall()
                if(rec==None):
                    break
                else:
                    for val in rec:
                        for j in val:
                            print(j,end="")
                        print()           
            con.commit()
            if(cur.rowcount>0):
                print("employee records listed")
            else:
                print("employee records not found")
            print("*"*50)
            ch=input("do you want to update another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("Thanks for using this application! ...")
                sys.exit()
        except cx_Oracle.DatabaseError as db:
            print("Problem in db", db)

selectrec()