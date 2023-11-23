import re
class student:
    def __init__(self):
        self.name=input("enter the student name: ")
        self.marks= float(input("enter the marks: "))
        self.email=input("enter the email addr: ")
        self.checres()
        
    def checres(self):
        with open("studinfo.data","a+") as wp:
            wp.write(self.name)
            wp.write(str(self.marks))  
            wp.write(self.email)
            # print("enter the line of text and quit to stop")
            # while(True):
            #     self.indata=input()
            #     if(self.indata.lower()=="quit"):
            #         break
            #     else:
            #         wp.write(self.indata + "\n")
                
            with open("studinfo.data","r+") as rp:
                self.fd=rp.read()
                self.namelist=re.findall("[A-Z][a-z]+", self.fd)
                self.marklist=re.findall("\d{2}",self.fd)
                self.email=re.findall("\S+@\S+",self.fd)
                with open("vildrec.info","a+") as wp:
                    wp.writelines(self.namelist)
                    wp.writelines(self.marklist)
                    wp.writelines(self.email)
                    print("record inserted sccessfully")
                    self.disp()
    def disp(self):
        print("\tname\tmarks\temail")
        for name,mark,mail in zip(self.namelist,self.marklist,self.email):
            print("\t{}\t{}\t{}".format(name,mark,mail))
        

s=student()
