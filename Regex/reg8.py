# Quantifiers in python

print("*"*50)
print("exactly for one k only")
print("*"*50)
#=========
import re
ls=re.finditer("k","akaakkkkakkkaaaaakakaakaka")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))

print("*"*50)
print("k and along with k ")
print("*"*50)
#=========
import re
ls=re.finditer("k.","akaakkkkakkkaaaaakakaakaka")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))

print("*"*50)
print("one or more k+")
print("*"*50)
#=========
import re
ls=re.finditer("k+","akaakkkkakkkaaaaakakaakaka")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))

print("*"*50)
print("zero, one or more k*")
print("*"*50)
#=========
import re
ls=re.finditer("k*","akaakkkkakkkaaaaakakaakaka")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))

print("*"*50)
print("zero/one k?")
print("*"*50)
#=========
import re
ls=re.finditer("k?","akaakkkkakkkaaaaakakaakaka")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))