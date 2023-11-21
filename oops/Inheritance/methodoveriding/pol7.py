# variable length arguments
class show:
    def __init__(self,*a):
        self.a=a
        print("-"*40)
        for i in self.a:
            print("{}".format(i), end=" ")
        print()
        print("-"*40)
#main program
show()
show(10,20)
show(10,20,30)
show(10,30,40,50)
show("python","django","pyspark", "numpy","pandas")