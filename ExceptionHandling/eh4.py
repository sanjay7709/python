from eh1 import InvalidInputError,ZeroError
from eh5 import mulop
try:
    n=int(input("enter the number: "))
    mulop(n)
except InvalidInputError:
    print("Dont enter -ve values ")
except ZeroError:
    print("Dont enter Zero as a value")
except ValueError:
    print("Dont enter str, symbols and alnum values ")
except Exception as e:
    print(e)
else:
    print("--Please try again--")