# pypr update sal and design of employee based on empno
#serviceid= select * from global_name;
import cx_Oracle,sys
def updaterec():
    while(True):
        try:
            con=cx_Oracle.connect("username/password@DNS/serviceid")
            cur=con.cursor()
            empno=int(input("enter the employee no: "))
            empsal=float(input("enter the emp sal"))
            empcname= input("enter employee company name: ")
            qry="update employee set sal=%f,cname=%s where empno=%d"
            cur.execute(qry, %(empsal,empcname,empno)) 
            con.commit()
            if(cur.rowcount>0):
                print("employee records updated")
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

updaterec()