# unpickling
import pickle,sys
try:
    with open("emp.data","rb") as wp:
        try:
            print("ENo"+" "+"Ename"+" "+"Esal")
            while(True):
                obj=pickle.load(wp)
                for i in obj:
                    print(i,end=" ")
                print()
        except EOFError:
            print("Record list completed")
            sys.exit()
except FileNotFoundError:
    print("source file doesnot exists")