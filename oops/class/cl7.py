# accepts numerical integer value and generate multiplication table
class multiply:
    @staticmethod
    def multi(obj):
        #print(obj.__dict__)
        if(obj.num<=0):
            print("{} it is an invalid input".format(obj.num))
        else:
            print("\t Multiplication table for = {}".format(obj.num))
            for i in range(1,11):
                print("\t{}*{}={}".format(obj.num,i,obj.num*i))

class numbers:
    #instance method
    def getnum(self):
        self.num=int(input("enter the number: "))
        #self.cal()
    
    # def cal(self):
        # if(self.num<=0):
        #     print("{} it is an invalid input".format(obj.num))
        # else:
    #     print("\tMultiplication table for {}".format(self.num))
    #     for i in range(1,11):
    #         print("\t{}*{}={}".format(self.num,i,self.num*i))

n=numbers()
n.getnum()
multiply.multi(n)