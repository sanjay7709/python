# pickling concepts using constructors

class student:
    def __init__(self,sno,sname,marks,crs="python"):
        self.stno=sno
        self.stname=sname
        self.stmarks=marks
        self.cname=crs
    
    def dispval(self):
        print("\t{}\t{}\t{}\t{}".format(self.stno,self.stname,self.stmarks,self.cname))
    