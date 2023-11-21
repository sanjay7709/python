#hybrid inheritance with polymorphism

class c1:
    def x(self):
        print("cl-x")

class c2(c1):
    def x(self):
        print("c2-y")
       # super().x()

class c3(c1):
    def x(self):
        print("c3-z")
        #super().x()

class c4(c2,c3):
    def x(self):
        print("c4-k")
        # c2.y(self)
        # c3.z(self)
          # here it as unique function names thats y its ableto display , but with
          # samefunction names if this is used we might get an error ....
        #super().x()   # here it gives only the  result of y()
        c3.x(self)
        c2.x(self)
        c1.x(self)
o4=c4()
o4.x()
# o4.z()
# o4.y()
# o4.x()