"""
Python database communication (PYDB)
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
    mod:  cx_oracle
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

    >> 1) DDL --> data definition language
            a)create
            b) alter
            c)drop
    >> 2) DML --> data manipulation language
            a) insert
            b)delete
            c) update
    >> 3) DRL -->data retrieval language
            a) select
5. python process the result from db
6. python program closes the connection
"""