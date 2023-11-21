#self.stno, name, marks in3 calculate total marks , give self.grade fail less than 40 in any of sub, distinction'
#totalmarks lies b/w 250-300
#first marks lies--200-249
#second--199-150
#third--149--120
#generate results and store it in result db
#(store(self.stno,self.sname,self.sub1,self.sub2,self.sub3 and self.grade))
import mysql.connector
class student:
    def __init__(self):
        while(True):
            self.stno=int(input("Enter the student number: "))
            self.sname=input("Enter the student name: ")
            while(True):
                self.sub1=float(input("enter the self.sub1 marks: "))
                if(self.sub1>=0) and (self.sub1<=100):
                    break
                print("dont enter -ve values or values more than 100")
            while(True):
                self.sub2=float(input("enter the self.sub2 marks: "))
                if(self.sub2>=0) and (self.sub2<=100):
                    break
                print("dont enter -ve valuesor values more than 100")
            while(True):
                self.sub3=float(input("enter the self.sub3 marks: "))
                if(self.sub3>=0) and (self.sub3<=100):
                    break
                print("dont enter -ve valuesor values more than 100")
            #print("\t{}\t{}\t{}".format(self.sub1,self.sub2,self.sub3))
            # calculate marks
            self.totmarks=self.sub1+self.sub2+self.sub3
            self.per= (self.totmarks/300)*100

            # decide the self.grades
            if(self.sub1<40) or (self.sub2<40) or (self.sub3<40):
                self.grade="Fail"
            elif(self.totmarks<=300) and(self.totmarks>=250):
                self.grade= "Distinction"
            elif(self.totmarks<=249) and(self.totmarks>=200):
                self.grade="First"
            elif(self.totmarks<=199) and(self.totmarks>=150):
                self.grade="second"
            elif(self.totmarks<=149) and(self.totmarks>=120):
                self.grade="third"
                
            # student memo

            print("*"*50)
            print("\tStudent details")
            print("*"*50)
            print("Student no: {}".format(self.stno))
            print("Student name: {}".format(self.sname))
            print("Student sub1 marks: {}".format(self.sub1))
            print("Student sub2 marks: {}".format(self.sub2))
            print("Student sub3 marks: {}".format(self.sub3))
            print("Student total marks: {}".format(self.totmarks))
            print("Student percentage: {}".format(self.per))
            print("Student self.grade: {}".format(self.grade))
            print("*"*50) 

            ch=input("Do you want to enter another student deatils (yes/no): ")
            if(ch.lower()!="yes"):
                print("Thanks for using this application")
                break
            
    def insertrec(self):
        try:
            con=mysql.connector.connect(host="localhost",username="",passwd="",database="result")
            cur=con.cursor()
            #s=student()  # if u areusing it in another program
            qry="insert into student values(%d,'%s',%0.2f,%0.2f,%0.2f,%0.2f,%f,'%s')"
            cur.execute(qry %(self.stno,self.sname,self.sub1,self.sub2,self.sub3,self.totmarks,self.per,self.grade))
            con.commit()
            if(cur.rowcount>0):
                print("The employee records inserted successfully")
            else:
                print("The record does not exists")
        except mysql.connector.databaseerror as db:
            print("problem in db", db)
        

s=student()
s.insertrec()

