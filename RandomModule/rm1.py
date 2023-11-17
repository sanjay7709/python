# random module
'''
Random is pre-define module
It contains
1) randint(start,stop) --> random value b/t start and stop value
2) randrange
=============
3)random()--> 0.0 to 1.0
4)uniform()  --> start,stop--> int/float --floating values , stop-1
==============
5) choice()--> takes one arg only
6) shuffle()
7) sample()
'''

# captcha code 
# code-1
print("*"*50)
print("using choice method")
print("*"*50)
import random as r
s="ABCDE$%^&*()#@1234567829"
for i in range(1,6):
    print(r.choice(s),end= " ")
#print(r.choice(s),r.choice(s),r.choice(s))
print()
print("*"*50)
# code-2 
print("using sample method")
print("*"*50)
for i in r.sample(s,6):
    print(i, end= " ")
print()
# code-3
print("*"*50)
print("using join method--sample")
print("*"*50)
s1=" "
s1=s1.join(r.sample(s,6))
print(s1)


#--Shuffle
print("*"*50)
print("using shuffle method for both list and captcha")
print("*"*50)
k=r.sample(s,6)
r.shuffle(k)
print(k)
for i in k:
    print(i, end=" ")
print()

for i in range(1,6):
    for j in k:
        print(j, end=" ")
    print()

lst=[10,20,30,40,50,60]
print(lst)
r.shuffle(lst)
print(lst)

for i in range(1,6):
    r.shuffle(lst)
    print(lst)