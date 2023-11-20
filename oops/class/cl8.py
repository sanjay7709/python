# take two inputs and calculate all arithmetic ops

# pypr select all records of a emp table  using classes and objects
import mysql.connector
class emp:
    def selecrec(self):
        con=mysql.connector.connect(host="localhost",username="",passwd="",database="")
        cur=con.cursor()
        qry="select * from emp"
        cur.execute(qry)
        for col in [x for x in cur.description]:
            print(col[0],end="")
        print()
        recs=cur.fetchall() 
        for rec in recs:
            for val in rec:
                print(val, end="")
            print()
c=emp()
c.selecrec()