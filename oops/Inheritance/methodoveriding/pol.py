'''
polymorphism
============
>> representing one form --> many forms is called polymorphism

polymorphism---> method overriding-->inheritance
purpose: efficient utilization memory --> less memory space is achieved
'''

#pypr which will calulate area of different figures such as circle, square, rectangle, by using classes and objects
# import math
# class area:
#     def __init__(self):
#         #self.r=float(input("enter the radius: "))
#         self.pi=math.pi
# class circle(area):
#     def cir(self):
#         #super().__init__()
#         self.r=float(input("enter the radius for circle: "))
#         self.acir=self.r**2*self.pi
#         self.dispp1()
#     def dispp1(self):
#         print("area of circle = {} ".format(self.acir))
# class square(area):
#     def squr(self):
#         #super().__init__()
#         self.r=float(input("enter the radius for square: "))
#         self.asqr=self.r*self.r
#         self.dispp()

#     def dispp(self):
#         print("area of square = {}".format(self.asqr))  
          
# a2=circle()
# a2.cir()        
# a1=square()
# a1.squr()

# single inheritance

import math
class circle:
    def __init__(self):
        #super().__init__()
        self.pi=math.pi
        self.r=float(input("enter the radius for circle: "))
        self.acir=self.r**2*self.pi
        #self.dispp1()
    # def dispp1(self):
    #     print("area of circle = {} ".format(self.acir))
class square(circle):
    def squr(self):
        #super().__init__()
        #circle.cir(self)
        self.r=float(input("enter the radius for square: "))
        self.asqr=self.r*self.r
        self.dispp()
    def dispp(self):
        print("area of square = {}".format(self.asqr))
        print("area of circle = {} ".format(self.acir))
          
a2=square()
a2.squr()        

