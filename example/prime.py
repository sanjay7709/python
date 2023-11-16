# #prime -- divisible by 1 and itself
# n=int(input("enter the number: "))
# if (n<=1):
#     print("please enter the crt num ")
# else:
#     res=False
#     for i in range(2,n):
#         if (n%i==0):
#             res=True
#             break
#     if(res):
#         print("{} is not prime".format(n))
#     else:
#         print("{} is prime number".format(n))

n=int(input("enter the size of list: "))
if (n<=0):
    print("please enter the crt size")
else:
    lst=[]
    for i in range(1,n+1):
        c=int(input("enter the {} value of list: ".format(i)))
        lst.append(c)
    else:
        print("elements of list are: {}".format(lst))
        res=False
        l1=[]
        for i in lst:
            if i==0 or i==1:
                continue
            for j in range(2,i):
                if (i%j==0):
                    res=True
                    break;
            else:
                l1.append(i)
        if(len(l1)):
            print(" prime number: ", end="->")
            for a in l1:
                print(a, end=" ")
        else:
            print("no number from given list is prime")
                
        # if(res):
        #     print("{} is not prime".format(i))
        # else:
        #     print("{} is prime".format(i))