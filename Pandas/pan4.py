""" 
Aceesing data in dataframe

CSV
===

to read csv data
>>> varname= pandas.read_csv(<file-path>)

dataframeobj.head(no of rows)
>> default 5-rows willbe printed
dataframeobj.tail(no of rows)
>> default 5-rows willbe printed

dataframeobj.describe()
> to view the summary
    >> nmost useful , gives the (count, max,mean,min,50%,25%...etc)

dataframeobj.shape()
>> to find the rows and columns details
dataframeobj[start:stop:step]
dataframeobj["colname"]
dataframeobj[["colname1","colname2","colname3"...."colname-n"]]
dataframeobj[["colname1","colname2","colname3"...."colname-n"]][start:stop:step]
dataframeobj.iterrows()
    >> in the form if tuple deisplay
    >> for rec in df.iterrows():
            print(rec)

Understandingloc()-----herestartandstopindexIncludedand

ColNamescanbeused(butnotcolumnnumbers]
----------------------------------------------------------------------------------------------------------------
1)DataFrameobj.loc[row_number]
2)DataFrameobj.loc[row_number,[ColName,.........]]
3)DataFrameobj.loc[start:stop:step]
4)DataFrameobj.loc[start:stop:step,["ColName"]]
5)DataFrameobj.loc[start:stop:step,["ColName1",ColName-2......."]]
6)DataFrameobj.loc[start:stop:step,"ColName1":ColName-n"]
----------------------------------------------------------------------------------------------------------------
Understandingiloc()-----herestartindexincludedandstopindexexcludedand
ColNumbersmustbeused(butnotcolumnnames]
--------------------------------------------------------------------------------------
1)DataFrameobj.iloc[row_number]
2)DataFrameobj.iloc[row_number,ColNumber.........]
3)DataFrameobj.iloc[row_number,[ColNumber1,ColNumber2............]]
3)DataFrameobj.iloc[rowstart:rowstop,ColStart:Colstop]
4)DataFrameobj.iloc[rowstart:rowstop,ColNumber]
5)DataFrameobj.iloc[[rownumber1,rownumber-2.....]]
6)DataFrameobj.iloc[rowstart:rowstop,[ColNumber1,ColNumber2............]]
6)DataFrameobj.iloc[:,[ColNumber1,ColNumber2............]]
================================================================
AddingColumnNametoDataFrame:
1)dataframeobj['newcolname']=defaultvalue
2)dataframeobj['newcolname']=expression
================================================================
RemovingColumnNamefromDataFrame:
1)dataframe.drop(columns="colname")
2)dataframe.drop(columns="colname",inplace=True)
================================================================
sortingthedataframedata:
1)dataframeobj.sort_values("colname")
2)dataframeobj.sort_values("colname",ascending=False)
3)dataframeobj.sort_values(["colname1","colname2",...colname-n])
================================================================
knowingduplicatesindataframedata:
1)dataframeobj.duplicated()---------------givesbooleanresult
================================================================
Removingduplicatesfromdataframedata:
1)dataframeobj.drop_duplicates()
2)dataframeobj.drop_duplicates(inplace=True)
================================================================
DataFilteringandConditionalChange:
1)dataframeobj.loc[simplecondition]
Ex: df.loc[df["maths"]>75]
2)dataframeobj.loc[compundcondition]
Ex:df.loc[(df["maths"]>60)&(df["maths]<85)]
Ex:df.loc[(df["percent"]>=60) & (df["percent"]<=80),["grade"]]="First" # cond
updattion.
SpecialCase:
3)dataframeobj.loc[simplecondition.str.contains(str)]
4)dataframeobj.loc[simplecondition.str.startswith(str)]
5)dataframeobj.loc[simplecondition.str.endswith(str)]
================================================================



"""