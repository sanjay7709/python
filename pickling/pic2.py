# read no of emp details, emp  no, name, sal etc,., save it as records in file by using pickling
import pickle
n=int(input("Enter the no of employess data : "))
if(n<=0):
    print("{} is an invalid input".format(n))
else:
    print("*"*50)
    print("\tEmployee Details")
    with open("emp.data","ab") as fp:
        for i in range(1,n+1):
            print("*"*50)
            print("Enter the details for employee {}".format(i))
            print("*"*50)
            eno=int(input("Enter the employee no: "))
            ename=input("Enter the Employee name: ")
            esal=float(input("Enter the Employee Salary: "))
            lst=[]
            lst.append(eno)
            lst.append(ename)
            lst.append(esal)
            pickle.dump(lst,fp)
            print("*"*50)
            print("{} employee record saved successfully".format(i))
            