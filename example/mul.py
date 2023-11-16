n=int(input("enter the size of list: "))
if (n<=0):
    print("please enter the crt size")
else:
    lst=[]
    for i in range(1,n+1):
        c=int(input("enter the {} value of list: ".format(i)))
        lst.append(c)
    else:
        for i in lst:
            if(i<=0):
                print("{} is an invalid number".format(i))
            else:
                print("*"*50)
                print("Multiplication table for {}".format(i))
                print("*"*50)
                for j in range(1,11):
                    print("{}*{}={}".format(i,j,i*j))