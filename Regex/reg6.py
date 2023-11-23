# Programmer defined character class
'''
#only abcABC
import re
ls=re.finditer("[abcABC]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print("{} ocurance = {}".format(omt.group(),nc))

#except abcABC
import re
ls=re.finditer("[^abcABC]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print("{} ocurance = {}".format(omt.group(),nc))
    
# lowercase
import re
ls=re.finditer("[a-z]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
#ls=re.finditer("[^a-z]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print("{} ocurance = {}".format(omt.group(),nc))
    
# uppercase
import re
ls=re.finditer("[A-Z]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
#ls=re.finditer("[^A-Z]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print("{} ocurance = {}".format(omt.group(),nc))

#digits
# ========
import re
ls=re.finditer("[0-9]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
#ls=re.finditer("[^0-9]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print("{} ocurance = {}".format(omt.group(),nc))

#alpha numeric
import re
ls=re.finditer("[A-Za-z0-9]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
#ls=re.finditer("[^A-Za-z]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print("{} ocurance = {}".format(omt.group(),nc))
'''

#special symbols
# ===============
import re
ls=re.finditer("[^A-Za-z0-9]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} ocurance = {}".format(omt.group(),nc))


# specific special symbols
# ===============
import re
ls=re.finditer("[\^9]","Abtrejald07849!@#%$%^&*((cbABCdskepif))")
nc=0
for omt in ls:
    print("start index= {}, end index={}, values={}".format(omt.start(),omt.end(),omt.group()))
    nc=nc+1
else:
    print()
    print("{} ocurance = {}".format(omt.group(),nc))

