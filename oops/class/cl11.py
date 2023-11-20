class student:
    def setstudvalues(self,sno,sname,marks,crs="python"):
        self.stno=sno
        self.stname=sname
        self.stmarks=marks
        self.crs=crs
    
    def dispstudvalues(self):
        print("\t{}\t{}\t{}\t{}".format(self.stno,self.stname,self.stmarks,self.crs))
