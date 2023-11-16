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
import random as r
s="ABCDE$%^&*()#@1234567829"
for i in range(1,6):
    print(r.choice(s),end= " ")
#print(r.choice(s),r.choice(s),r.choice(s))
print()
# code-2 
for i in r.sample(s,6):
    print(i, end= " ")
print()
# code-3
s1=" "
s1=s1.join(r.sample(s,6))
print(s1)


#--Shuffle

lst=[10,20,30,40,50,60]
print(lst)
r.shuffle(lst)
print(lst)

for i in range(1,6):
    r.shuffle(lst)
    print(lst)