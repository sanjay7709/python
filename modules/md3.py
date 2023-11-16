# development of programmer defined modules
"""Step-: Define programmer-defined functions
    step-2: define variable name(global)
    step-3: defineclasses(oops)
            save it in an ide as extension.py
            __pycache__
            <filename>.cpython-<version>.pyc"""
from math import *
def area():
    r=float(input("enter the radius: "))
    ar=pi*r**2
    print("Area of circle: {}".format(ar))

def peri():
    r=float(input("enter the radius: "))
    ar=pi*r*2
    print("perimeter of circle: {}".format(ar))

