# program that accepst table name and displays all its col names
#serviceid= select * from global_name;
import cx_Oracle
try:
    con=cx_Oracle.connect("username/pas@DNS/serviceid")
    cur=con.cursor()
    tname=input("enter the table name: ")
    qry="select * from %s"
    cur.execute(qry, %tname)
    # code for obtaining colnames
    print("*"*50)
    for colname in [metadata for metadata in cur.description]: # list comphrenshion
        print(colname[0], end=" ")
    print()
    print("*"*50)
    rec=cur.fetchall()
    for val in rec:
        for i in val:
            print(i,end=" ")
        print()
    print("*"*50)
    #obj=cur.description  # here obj is list of tuples 
    # for x in obj:
    #     print(x[0],end=" ")
    # print()
except cx_Oracle.DatabaseError:
    print("The table does not exists...")
finally:
    con.close()
    print("the connection is closed....")