import pickle
with open("stud.data","rb") as rp:
    print("*"*50)
    print("\tEmployee records")
    print("*"*50)
    while(True):
        try:
            ob=pickle.load(rp)
            for i in ob:
                print(i,end=" ")
            print()
        except EOFError:
            print("records completed")
            break
