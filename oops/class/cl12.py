import pickle,sys
#$from cl11 import student
class studunpick:
    def readstud(self):
        try:
            with open("dest.data", "rb") as fp:
                print("*"*50)
                print("\tsno\tname\tmarks\tcrs")
                print("*"*50)
                try:
                    while(True):
                        obj=pickle.load(fp)
                        obj.dispstudvalues()           
                except EOFError:
                    print("*"*50)
                    sys.exit()
        except FileNotFoundError:
            print("file does not exists")
            sys.exit()

c=studunpick()
c.readstud()