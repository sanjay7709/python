'''
pypr which will validate and retrieve the email ids where stud info present in file

'''
import re
with open("mailinfo.data","r")as rp:
    fd=rp.read()
    mailslist=re.finditer("\S+@\S+",fd)
    # for mail in mailslist:
    #     print(mail.start(),mail.end(),mail.group())
    
    print("only mail list")
    # mailslist=re.finditer("\S+@\S+",fd)
    for mail in mailslist:
        print(mail.group())
        