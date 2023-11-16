# program to get student details , no, name, marks , college
import pickle
# n= int(input("enter the number of students : "))
# if(n<=0):
#     print("{} is an invalid input".format(n))
# else:
with open("stud.data","ab") as fp:
    # for i in range(1,n+1):
    while(True):
        print("*"*50)
        print("\t Enter student details: ")
        print("*"*50)
        sno=int(input("Enter the student no: "))
        sname=input("Enter the student name: ")
        smarks=float(input("entre the student marks: "))
        scol=input("Enter the college name: ")
        l=[]
        l.append(sno)
        l.append(sname)
        l.append(smarks)
        l.append(scol)
        pickle.dump(l,fp)
        # print("{} record has been successfully inserted".format(i))
        ch=input("Do you want to enter another record (yes/no): ")
        if(ch.lower()=="no"):
            print("Thanks for using the application! ...")
            break

