#non csv reader
import csv 
import pandas as pd
try:
    with open("pandas.csv","r") as rp:
        csvread= csv.reader(rp)
        print(csvread) # address of csv object
        for val in csvread:
            for rec in val:
                print(rec, end=" ")
            print()
        # csvread= csv.reader(rp)
        # df=pd.DataFrame(csvread)
        # print(df)
except FileNotFoundError:
    print("file does not esists")
        