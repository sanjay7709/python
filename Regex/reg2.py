# regex
#finditer
from re import finditer
gd="python is an oop lang. python is also functional programming,is, python"
sp="py"
res=finditer(sp,gd)  # here res is of type <callable_iterable>
print(type(res))
nc=0
for omt in res:
    nc=nc+1
    print("start index= {} end index={} value= {}".format(omt.start(),omt.end(),omt.group()))
else:
    print("number of word '{}' occurances={}".format(sp,nc))






#example --files to inpout data till quit 
'''
try:
    with open("addr.info","a+") as fp:
        print("enter the lines of code and quit to stop")
        while(True):
            indata=input()
            if(indata.lower()=="quit"):
                break
            else:
                fp.write(indata +"\n")
except FileExistsError:
    print("file alraedy exists")
'''