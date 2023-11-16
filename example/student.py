#Accept student number , name and 3- sub marks  , c, cpp, python
#data validations
#calculate total marks of 3- subjects , percentage and grades
#grade-fail marks <40 atleast in one subject
#grade - passed in disctin --total marks lies 300 and 250
#grade first 249-200
#second 199-150
#third 149-120
res= True
while(res):
    stno = int(input("enter the std no: "))
    sname=input("enter the student name: ")
    while(True):
        cm=int(input("enter your marks in c:"))
        if(cm>=0)and (cm<=100):
            break
        print("please enter valid marks ")
    while(True):
        cpm=int(input("enter your marks in cpp:"))
        if(cpm>=0)and (cpm<=100):
            break
        print("please enter valid marks ")
    while(True):
        pym=int(input("enter your marks in python:"))
        if(pym>=0)and (pym<=100):
            break
        print("please enter valid marks ")

    #calculate total marks of 3- subjects
    totalmarks= cm+cpm+pym
    Per = (totalmarks/300)*100
    # decide the grade
    if (cm<40)or(cpm<40)or(pym<40):
        grade="FAIL"
    elif (totalmarks<=300) and (totalmarks>=250):
        grade="distinction"
    elif (totalmarks<=249) and (totalmarks>=200):
        grade="first"
    elif (totalmarks<=199) and (totalmarks>=150):
        grade="second"
    elif (totalmarks<=149) and (totalmarks>=120):
        grade="third"

    #display marks memo

    print("*"*50)
    print("\t student marks report ")
    print("*"*50)
    print("\t student no: {}".format(stno))
    print("\t student name: {}".format(sname))
    print("\t marks in c : {}".format(cm))
    print("\t marks in cpp : {}".format(cpm))
    print("\t marks in python {}".format(pym))
    print("*"*50)
    print("\t total marks: {}".format(totalmarks))
    print("\t percentage:  {}".format(Per))
    print("\t grade: {}".format(grade))
    print("*"*50)

    res=input("do you need to enter another data: (yes/no)")
    if (res.lower()== "yes"):
        res= True
    else:
        res= False







