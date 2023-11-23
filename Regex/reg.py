# mobile number validation
import re
try:
    while(True):
        mob=int(input("enter the mobile number: "))
        fin=re.search("[6-9][0-9]{9}",str(mob))
        #fin1=re.search("\d{10}",str(mob))
        if (fin!=None) and(len(str((mob)))==10):
            print("{} number in range".format(fin.group()))
        else:
            print("entered number {} is not valid".format(mob))
            break
except ValueError:
    print("Dont enter float values, str, and symbols as input")