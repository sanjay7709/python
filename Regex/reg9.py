'''
pypr which search for names of student and their marks  in given data
'''
gc= '''Rohit got 56 marks,Rocky got 57 marks,Rani got 58 marks,Ram got 59 marks,Vishwa got 60 marks,
        Swat got 65 marks,John got 66 marks,Moni got 76 marks,'''
import re
namelist=re.findall("[A-Z][a-z]+",gc)
# for name in namelist:
#     print("\t{}".format(name))
# # marklist=re.findall("[0-9][0-9]+",gc)
marklist=re.findall("\d+",gc)
# for mark in marklist:
#     print("\t{}".format(mark))
print("*"*50)
print("\tName\tmarks")
print("*"*50)
for name, mark in zip(namelist,marklist):
    print("\t{}\t{}".format(name,mark))
print()







'''

import re
class student:
    def __init__(self):
        self.name=input("enter the student name: ")
        self.marks= float(input("enter the marks: "))
        self.email=input("enter the email addr: ")
        self.checres()
        
    def checres(self):
        with open("addr.info","a+") as wp:
            wp.write(self.name)
            wp.write(self.marks)   
            wp.write(self.email) 
            with open("addr.info","r+") as rp:
                self.fd=rp.read()
                self.namelist=re.findall("[A-Z][a-z]+", self.fd)
                self.marklist=re.findall("\d{2}",self.fd)
                self.email=re.findall("\S+@\S+",self.fd)
                with open("newrec.info","a+") as wp:
                    wp.writelines(self.fin)
                    print("record inserted sccessfully")

s=student()
'''