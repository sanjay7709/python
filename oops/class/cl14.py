# program for area and peri of circle using static method 
import math
class circle:
    @classmethod
    def pival(cls):
        cls.pi=round(math.pi,2)
        
    def getval(self):
        self.r=int(input("enter the value of radius: "))
        self.pival()
        
class calcu:
    @staticmethod
    def calc(obj):
        print(obj.__dict__)
        area=obj.pi*obj.r**2
        peri=2*obj.pi*obj.r
        print("Area = {}".format(area))
        print("peri ={}".format(peri))
c=circle()
c.getval()
calcu.calc(c)
