#python script
while(True):
    age = int(input("enter your age: "))
    if (age>=18) and (age<=100):
        print("=========================")
        print("age is {} and eligible to vote".format(age))
        print("--------------------------")
    else:
        print("you are not eligible to vote")
