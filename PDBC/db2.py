import cx_Oracle
try:
    con=cx_Oracle.connect("username/password@DNS/serviceid")
    cur=con.cursor()
    qry="alter table student modify(eno number(5))"
    #qry="alter table student add(esal number(7,2))"
    #qry="create table student(stno number(3) primary key,sname varchar2(10) not null, marks number(5,2) not null)"
    cur.execute(qry)
    print("table modified successfully")
except cx_Oracle.DatabaseError as db:
    print("problem in db:  ",db)
