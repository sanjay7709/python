#hybrid inheritance

class c1:
    def x(self):
        print("cl-x")

class c2(c1):
    def y(self):
        print("c2-y")
       # super().x()

class c3(c1):
    def z(self):
        print("c3-z")
        #super().x()

class c4(c2,c3):
    def k(self):
        print("c4-k")
        # c2.y(self)
        # c3.z(self)
        super().y()
        super().z()   # here it as unique function names thats y its ableto display , but with
                        # samefunction names if this is used we might get an error ....
        super().x()
        
o4=c4()
o4.k()
# o4.z()
# o4.y()
# o4.x()