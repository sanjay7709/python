#which accepts numerical value and find sum of digits in the given number

n=int(input("enter the number: "))
if(n<=0):
    print("{} is an invalid number".format(n))
else:
    s=0 
    while(n>0):
        d=n%10
        s=s+d
        n=n//10
    else:
        print("sum={}".format(s))


#645
#sum=15