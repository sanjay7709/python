# regex-3
#search
from re import search
gd="python is an oop lang. python is also functional programming,is, python"
sp="python"
'''It finds only the first result and stops the execution once the match is found
   if no input is found it returns "None"  '''
matchinfo=search(sp,gd)  # here matchinfo is of type search 
print(type(matchinfo)) # <class 're.Match'>
#nc=0
print("start index={} endindex={} value= {}".format(matchinfo.start(),matchinfo.end(),matchinfo.group()))
# for omt in matchlist:
#     #nc=nc+1
#     print(omt)
#     #print("start index= {} end index={} value= {}".format(omt.start(),omt.end(),omt.group()))
# else:
#     print("number of word '{}' occurances={}".format(sp,len(matchlist)))
