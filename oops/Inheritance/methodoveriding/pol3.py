#constructor

class test:
    def __init__(self,a): # original method constructor
        print("class test = ",a)

class sample:
    def __init__(self,a,b): #original METHIOD constructor
        print("class sample= ",a,b)

class example(test,sample):
    def __init__(self,name): #original METHIOD constructor
        #super().__init__()
        print("class example = name= {}".format(name))
        test.__init__(self,12)
        sample.__init__(self,100,200)
        #sample.__init__()  --- throw error missing positional arguments
        
s=example("sanjay")