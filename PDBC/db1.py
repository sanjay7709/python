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
python wants to communicate any database we need to use pre-defined module, such module are not present
in python library
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
3. create an object of Cursor
4. Design the query and place the query in object of cursor(DDL,DML,DRL)
5. python process the result from db
6. python program closes the connection
"""