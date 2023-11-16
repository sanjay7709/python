#accept any number and convert to equivalent Roman number
#Roman number
# I II III IV V VI VII VIII IX X XI XII L M 
# 1---I--while
# 4---IV--if
# 5---V--if
# 9---IX --if
# 10--X--while
# 40---XL--if
# 50---L --if
# 90---XC--if
# 100--C--while
#500-D--if
#400-CD--if
#1000-M--while
#900-CM--if
n=int(input("enter any number: "))
if(n<=0):
    print("{} is an invalid input".format(n))
else:
    while (n>=1000):
        print("M", end="")
        n=n-1000
    if(n>=900):
        print("CM", end="")
        n=n-900
    if(n>=500):
        print("D", end="")
        n=n-500
    if(n>=400):
        print("CD", end="")
        n=n-400
    while(n>=100):
        print("C",end="")
        n=n-100
    if(n>=90):
        print("XC", end="")
        n=n-90
    if(n>=50):
        print("L", end="")
        n=n-50
    if(n>=40):
        print("XL", end="")
        n=n-40
    while(n>=10):
        print("X",end="")
        n=n-10
    if(n>=9):
        print("IX", end="")
        n=n-9
    if(n>=5):
        print("V", end="")
        n=n-5
    if(n>=4):
        print("IV", end="")
        n=n-4
    while(n>=1):
        print("I", end="")
        n=n-1