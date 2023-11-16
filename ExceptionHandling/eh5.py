from eh1 import InvalidInputError,ZeroError
def mulop(n):
    if(n<0):
        raise InvalidInputError
    elif(n==0):
        raise ZeroError
    else:
        print("*"*50)
        print("\tMulitiplication table of {}".format(n))
        print("*"*50)
        for i in range(1,11):
            print("\t{}*{}={}".format(n,i,n*i))
        print("*"*50)
