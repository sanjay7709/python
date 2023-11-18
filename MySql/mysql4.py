# program transfers amount from src to dest account

import mysql.connector
try:
    con=mysql.connector.connect(host="localhost", username="",passwd="",database="")
    cur=con.cursor()
    tname=input("enter the table name: ")
    qry="select * from %s"
    cur.execute(qry %(tname))
    recs=cur.fetchall()
    print("*"*50)
    for col in [xdata for xdata in cur.description]:
        print(col[0],end=" ")
    print()
    print("*"*50)
    for rec in recs:
        for val in rec:
            print(val,end=" ")
        print()
    print("*"*50)
    sracno=int(input("Enter the source accno: "))
    found=False
    for i in recs:
        if(sracno==i[0]):
            found=True
            srbal=i[2]
            break   
    if(found==False):
        print("The record {} is an invalid accno".format(sracno))
    else:
        stramt=float(input("enter the src amount: "))
        if((stramt+500)>srbal):
            print("You dont have sufficient funds")
        else:
            dstacno=int(input("Enter the destination accno: "))
            found=False
            for i in recs:
                if(dstacno==i[0]):
                    found=True
                    srbal=i[2]
                    break   
            if(found==False):
                print("The record {} is an invalid accno".format(dstacno))
            qry="update fundstransf set bal=bal-%f where acno=%d"
            cur.execute(qry %(stramt,sracno))
            qry1="update fundstransf set bal=bal+%f where acno=%d"
            cur.execute(qry %(stramt,dstacno))
            con.commit()
            print("\n form Account number {} INR: {} is transferred to Acno: {} -- verify".format(sracno,stramt,dstacno))
            print("The records updated successfully")
            cur.execute(qry %(tname))
            recs=cur.fetchall()
            print("*"*50)
            for col in [xdata for xdata in cur.description]:
                print(col[0],end=" ")
            print()
            print("*"*50)
            for rec in recs:
                for val in rec:
                    print(val,end=" ")
                print()
            print("*"*50)
except mysql.connector.DataBaseError as db:
    print("The problem in db", db)
                



