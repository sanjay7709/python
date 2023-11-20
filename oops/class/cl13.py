# cla area and perimeterof circle
import math
class circle:
    @classmethod
    def calc(cls):
        cls.pi=round(math.pi,2)
        
    def getrad(self):
        self.r=float(input("enter the radius: "))
        self.calc()
        self.area=self.r*self.r*self.pi
        self.peri=2*self.pi*self.r
        self.disp()
    
    def disp(self):
        print("\t Area and permiter of circle")
        print("*"*50)
        print("Area of circle = {}".format(self.area))
        print("perimeter of circle = {}".format(self.peri))   

a=circle()
a.getrad()
