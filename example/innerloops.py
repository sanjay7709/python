#n= int(input("enter the number for pattern: "))
n=5
# for i in range(1,n+1):
#     #print(i)
#     for j in range(1, i+1):
#         print("*", end="")
#     print()
# i,j=1,1
# while(i<=n):
#     print(i)
#     while(j<4):
#         print(j,end="")
#         j+=1
#     else:
#         print()
#         i=i+1
#         j=1
#---------------------------------
# for in while
i,j=1,1
while(i<=n):
    print(i)
    for j in range(1,4):
        print(j, end="")
    else:
        print()
        i=i+1
        j=1
print("*"*50)
print("while in for loop result")
for i in range(1,n+1):
    print(i)
    j=1
    while(j<4):
        print(j, end="")
        j=j+1
    else:
        print()
        
