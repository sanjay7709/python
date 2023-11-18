#which accepts empno from keyboard and remove complete record
import cx_Oracle
def empdel():
    while(True):
        try:
            con=cx_Oracle.connect("username/password@dns/serviceid")
            cur=con.cursor()
            eno=int(input("enter the employee no to be deleted: "))
            qry="delete from employee where eno=%d"
            cur.execute(qry %(eno))
            con.commit()
            print("the employee {} record is removed successfully ".format(cur.rowcount))
            if(cur.rowcount<=0):
                print("empno does not exists")
            else:
                print("record removed")
            print("*"*50)
            ch=input("Do you want to enter another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("thanks for using this application! ")
                break
        except cx_Oracle.DatabaseError as db:
            print("problem in db", db)

empdel()   #function call 