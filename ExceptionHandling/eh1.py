# exception handling
# ================================
'''complie time errors
    Logical error
    Runtime error'''
'''try
except
else
finally
raise'''

''' 
syntax for handling exceptions
'''
import os
os.system('cls')
# try:
#     s1=input("enter the first value: ")
#     s2=input("entr the second value: ")
#     a=int(s1)
#     b=int(s2)
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("zero is not divisble , do not enter it in denominator")
# except ValueError:
#     print("do not enter str, special characters , alnum")
# except Exception as e :
#     print("something went wrong",e)
# else:
#     print("value of a={}".format(a))
#     print("value of b={}".format(b))
#     print("value of c={}".format(c))
# finally:
#     print("\n i am from finally block")


# class <classname> (Baseclass): pass 

class SanDivError(Exception):pass

class InvalidInputError(Exception):pass
class ZeroError(Exception):pass


