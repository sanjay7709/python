from eh1 import SanDivError
def divi(a,b):
    if(b==0):
        raise SanDivError
    else:
        c=(a/b)
        return c