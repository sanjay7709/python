#pre-defined char classes
# ================================
print("*"*50)
print("space")
print("*"*50)
#space
#=========
import re
ls=re.finditer("\s","Abtrej ald0784 9!@#%$%^&*((cbA BCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))
    
print("*"*50)  
print("Except space chars")
print("*"*50)
# Except space chars
#=========
import re
ls=re.finditer("\S","Abt rejald078 49!@ #%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))
    
print("*"*50)
print("digit chars  (only digits)")
print("*"*50)
# digit chars  (only digits)
#=========
import re
ls=re.finditer("\d","Abt rejald078 49!@ #%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))

print("*"*50)
print("except digitchars --(alpha + special symbols)")
print("*"*50)
# except digitchars --(alpha + special symbols)
#=========
import re
ls=re.finditer("\D","Abt rejald078 49!@ #%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))
    
print("*"*50)    
print("all word chars and digits (alpha numeric==(alpha+digits))  chars")
print("*"*50)
# all word chars and digits (alpha numeric==(alpha+digits))  chars
#=========
import re
ls=re.finditer("\w","Abt rejald078 49!@ #%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))
    
print("*"*50)
print("except words and digits --(only special symbols)  chars")
print("*"*50)
# except words and digits --(only special symbols)  chars
#=========
import re
ls=re.finditer("\W","Abt rejald078 49!@ #%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))


print("*"*50)
print("only two digits chars")
print("*"*50)
#=========
import re
ls=re.finditer("\d+","Abt rejald07849!@ #%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} occurance = {}".format(omt.group(),nc))

