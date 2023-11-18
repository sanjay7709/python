"""
Th MYSQL communication to python
================================
pip install mysql-connector

>> show databases;
>> use database <database-name>;
>> create database  <database-name>;
>> show tables;
>> select * from table <table-name>;

steps:
    1) import mysql.connector
    >> install module "pip install mysql-connector"
    2) python connection to --mysqldb
    >>  varname= mysql.connector.connect( host="DNS/IP address",user="<username>",passwd="<password>")
            varname is an objectof "<class,mysql.connector.connection>"
    
    3)create an object of cursor
    4)design and place the query to execute
    5)process the result available to cursor


"""