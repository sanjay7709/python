'''
pandas
========
Data analysis
>> Pandas ---> panel data
>> pip tool
>>pip install pandas
==================================
1) Series --> column in excel sheet --> 1D array
        varname=pandas.Series(obj,index,dtype)
2) dataframe --> 2D array
==============================
>>> varname= pandas.Dataframe(obj,index,columns,dtype)


Examples:
=========
>>> import pandas as pd
>>> b=pd.Series([10,20,30,40,50,60],index=[2,4,6,8,10,12])
>>> b
2     10
4     20
6     30
8     40
10    50
12    60 
dtype: int64
>>> b=pd.Series([10,20,30,40,50,60],index=[2,4,6,8,10,12],dtype=float)
>>> b
2     10.0
4     20.0
6     30.0
8     40.0
10    50.0
12    60.0
dtype: float64
>>> b=pd.Series([10,20,30,40,50,60],index=[2,4,6,8,10,12],dtype=bool)
>>> b
2     True
4     True
6     True
8     True
10    True
12    True
dtype: bool
>>> b=pd.Series([10,20,30,40,50,60],index=[2,4,6,8,10,12],dtype=complex)
>>> b
2     10.0+ 0.0j
4     20.0+ 0.0j
6     30.0+ 0.0j
8     40.0+ 0.0j
10    50.0+ 0.0j
12    60.0+ 0.0j
dtype: complex128
=================================================================================
Dataframe
======================================================
>>> df=pd.DataFrame([[10,"san"],[20,"sen"],[30,"ven"]])
>>> df
    0    1
0  10  san
1  20  sen
2  30  ven
>>> df=pd.DataFrame([[10,"san"],[20,"sen"],[30,"ven"]], index=[1,2,3],columns=["sno","sname"])
>>> df
   sno sname
1   10   san
2   20   sen
3   30   ven

'''

import pandas as pd

l=[10,20,30,40,50,60]
b=pd.read_saseries(l)
print(b)