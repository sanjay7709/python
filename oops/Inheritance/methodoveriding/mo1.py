"""
Method overiding
=================
(method heading is same and body is different)
if we are using he same method name in different classes then the method get overriden
by the last mentioned one
hence we use "super().<methodname>()"
            "classname.methodname()"
            

"""

class dog:
    def noise(self):   # original method
        print(" bow bow")

class cat(dog):
    def noise(self):  # method overridden
        print(" mew mew")
        super().noise()
    # or
        #dog.noise(self)

class cow(cat):
    def noise(self):  # method overridden
        print(" maah maah")
        super().noise()
    # or
        #dog.noise(self)
c=cow()
c.noise()