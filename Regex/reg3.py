# regex-3
#findall
from re import findall
gd="python is an oop lang. python is also functional programming,is, python"
sp="py"
matchlist=findall(sp,gd)  # here res is of type match list
print(type(matchlist))  #<class list>
#nc=0
for omt in matchlist:
    #nc=nc+1
    print(omt)
    #print("start index= {} end index={} value= {}".format(omt.start(),omt.end(),omt.group()))
else:
    print("number of word '{}' occurances={}".format(sp,len(matchlist)))
