# main program
from eh2 import divi
from eh1 import SanDivError
try:
    x=int(input("enter first value: "))
    y=int(input("enter second value: "))
    res= divi(x,y)
except SanDivError:
    print("\n Dont enter Zero for deno..")
except ValueError:
    print("Dont enter alpha num , str, or symbols")
else:
    print("result={}".format(res))
finally:
    print("i am from finally block")