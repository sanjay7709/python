"""
Python database communication (PYDBC)
communication b/w python and database
SQL/PLSQL IVAN --book
Files limitations
1) Security is less
2) to extract or process the data from files is very complex
3)unable to store large volume of data
4) files are os dependant
5)files does not contain column names , and very complex to query the data

To overcome limitations we use (RDBMS)
1) security is more in Db
2) querying is easy 
3) os independant
4) can store large volume of data


Module
-------
python wants to communicate any database we need to use pre-defined module, 
such module are not present in python library
so we need to use pre-defined module using "pip"
>> for oracle database
    mod:  cx_Oracle
>> MySql databas
    mod: mysql-connector
check for pip path
>> set path="<path>"
synt:   pip install <module-name>
        pip install cx_Oracle
        pip install mysql-connector
Steps:
=======
1. import cx_Oracle
2. connection from python --> DB
    >> connection from oracle database, we must use ===> connect()
        syntax: varname= cx_Oracle.connect("connection url")
                varname is an object of <class,"cx_Oracle.connection">
        connection url General format is :
             >>      "Username/password@DNS/serviceid" 
             >> username==> username of oracle database
             >> password ==> pass of Oracle database
             >> DNS==> name of machine where oracle software is installed <ip-address> 
                       default: 127.0.0.1 or "localhost"
             >> serviceid ==> On which name DB is avaiable/present in our machine
                            query: ( select * from global_name; ) 
        >> if connection url is wrong 
            we get exception "cx_Oracle.DataBaseError"
3. create an object of Cursor
    >> purpose is to carry the query from python to database in the object of cursor 
    >> We must use ---> cursor() --> present in connection object
            varname =conobj.cursor()
            varname is an object of <class,"cx_Oracle.cursor">
4. Design the query and place the query in object of cursor(DDL,DML,DRL)
        varname= cur.execute("query")
    >> 1) DDL --> data definition language
            a)create
                ceating the table  in db
                $ create table <table-name>
ex: create table student(stno number(3) primary key,sname varchar2(10) not null, marks number(5,2) not null)
        $ to view ---> desc student;
        >> to view content--> select * from student;
            b) alter
>> To alter the existing table alos we cna adddnew columns to the table
ex: alter table student modify(stno number(5) primary key, sname varchar(25) not null, marks number(6,2) not null
                         college varchar2(25) not null)
 alter table table-name add(college varchar2(25) not null)
        # to view --> desc student;
        # to view content--> select * from student;
            c)drop
ex: drop table table-name

    >> 2) DML --> data manipulation language
            a) insert
                >> insert into table values(val1 for col1, val2 for col2 ---valn--coln)
                ex: insert into employee values(111,"san",10.5,"hcl");
                after insertion commit the changes or else the changes will not be reflected
                rollback ---> can be done only before the commit 
            b) delete
            >> delete from table <table-name>
            >> delete from table employee where sal>=10  # condition
            >> delete from employee where eno=555
            
            c) update
            (update all records)
          sql  >> update tablename set existingcolname=exp1,existingcol2=exp2 .....n
          (update particular records)
         sql  >> update tablename set existingcolname=exp1,existingcol2=exp2 ....where condiion list      
            ex: update employee set sal=sal+sal*(25/100)
                update employee set sal=sal+sal*(10/100) where eno=24  # only to specifc employee
  
    >> 3) DRL -->data retrieval language
            a) select
            >> select count(*) from employee       # displays the count result
            >> select eno from employee  # all emp no data
            >> select eno,ename, esal from employee # all emp no, name, and sal data
            >> select * from employee # to get all records
            >> select * from employee where sal>10L and sal<=5L
        To read or extract the records data from table
        syntax:  select col1,col2...coln from <table-name>
    ##NOTE:
        Once select query is executed all the data is present in the cur object
        and we can retrive/ extract them by using 3-methods they are:
        1.fetchone() ---> # here object stores in form of tuple()
        2.fetchmany(no of records) --> # here objectis list of tuple [(),(),()]
        3.fetchall()
5. python process the result from db
6. python program closes the connection
"""