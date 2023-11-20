#program student using class and object
# instance level datamembers
class student:
    crs="PYTHON"  # classlevel 

s1=student()
print("content of s1 = ",s1.__dict__)
print("type of s1 = ",type(s1.__dict__))
print("len of s1 = ",len(s1.__dict__))
s1.sno=14
s1.name="rs"
s1.marks=56.88
print("content of s1 = ",s1.__dict__)

s2=student()
print("content of s2 = ",s2.__dict__)
print("type of s2 = ",type(s2.__dict__))
print("len of s2 = ",len(s2.__dict__))
s2.sno=14
s2.name="rs"
s2.marks=56.88
print("content of s2 = ",s2.__dict__)

print("*"*50)
print("Student details")
print("*"*50)
print("Student number: ",s1.sno)
print("Student name: ",s1.name)
print("Student marks: ",s1.marks)
print("Student course: ",student.crs) # class level datamember
print("Student course: ",s1.crs) # access using object ==> class level datamember
print("*"*50)

