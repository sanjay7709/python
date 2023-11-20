# unpickling
import pickle
try:
    with open("cons.data","rb") as rp:
        print("*"*50)
        print("\tsno\tname\tmarks\tcourse")
        print("*"*50)
        while(True):
            try:
                obj=pickle.load(rp)
                obj.dispval()
            except EOFError:
                print("*"*50)
                break
  
except FileNotFoundError:
    print("File doesnot exists")