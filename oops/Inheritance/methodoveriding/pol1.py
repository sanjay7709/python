# polymorphism
# multiple inheritance
import math,sys
class circle:
    def area(self):  # original method
        #super().__init__()
        self.pi=math.pi
        self.r=float(input("enter the radius for circle: "))
        self.acir=self.r**2*self.pi
        #self.dispp1()
    # def dispp1(self):
    #     print("area of circle = {} ".format(self.acir))
class square:
    def area(self):  # overriden method
        #super().area()
        circle.area(self)
        self.r=float(input("enter the radius for square: "))
        self.asqr=self.r*self.r
        print("*"*50)
        print("area of square = {}".format(self.asqr))
        print("area of circle = {} ".format(self.acir))
        print("*"*50)
        ch=input("do you want to find another area (yes/no): ")
        if(ch.lower()!="yes"):
            print("Thanks for using this application")
            sys.exit()
        else:
            self.area()  

class rect(square,circle):
    def area(self): # overriden method
        self.l=float(input("enter the length: "))
        self.b=float(input("enter the breadth: "))
        self.arec=self.l*self.b
        print("Area of rectangle = {}".format(self.arec))
        super().area()
        #circle.area(self)   # if not defined in the above class we can use here also

r=rect()
r.area()
    
    