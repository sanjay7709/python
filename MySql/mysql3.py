# pypr to transfer funds from one account to another account
import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",username="",passwd="",database="")
    cur=con.cursor()
    cur.execute("create table fundtransf(Aco int primary key,cname varchar(20) not null, bal real not null)")
    print("table is created")
except mysql.connector.DataBaseerror as db:
    print("problem in db", db)

# inserting values
import mysql.connector
def insrec1():
    while(True):
        try:
            con=mysql.connector.connect(host="localhost",username="",passwd="",database="")
            cur=con.cursor()
            acn=int(input("enter the account no: "))
            cname=input("enter the customer name: ")
            bal=float(input("enter the current balance: "))
            qry="insert into fundtransf values(%d,%s,%f)"
            cur.execute(qry %(acn,cname,bal))
            con.commit()
            if(cur.rowcount>0):
                print("the records inserted successfully")
            else:
                print("record does not exists")
            print("*"*50)
            ch=input("Do you want to enter another record (yes/no): ")
            print("*"*50)
            if(ch.lower()=="no"):
                print("thanks for using this application! ")
                break           
        except mysql.connector.DataBaseerror as db:
            print("problem in db", db)


