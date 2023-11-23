#pypr accept line of text and accept a search pattern and search inthe given data and
#display search is succesfull or not
# using finditer
'''
import re
indata=input("enter the line of text: ")
ser=input("enter the search pattern: ")
nc=0
cite=re.finditer(ser,indata)
for mat in cite:
    nc=nc+1
    print("start index = {}, end index={}, value={}".format(mat.start(),mat.end(),mat.group()))
else:
    print("occurances of '{}' = {}".format(ser,nc))
'''

# using search()
import re
indata=input("enter the line of text: ")
ser=input("enter the search pattern: ")
nc=0
cite=re.search(ser,indata)
if(cite!="None"):
    print("{} search is successfull".format(ser))
    print("start index = {}, end index={}, value={}".format(cite.start(),cite.end(),cite.group()))
else:
    print("{} search is not found".format(ser))