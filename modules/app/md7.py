from md6 import menu
from md8 import *
import sys
while(True):
    menu()
    ch=int(input("enter your choice: "))
    match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            moduop()
        case 6:
            expo()
        case 7:
            print("Thanks for using application")
            sys.exit()
        case _:
            print("your selection of input is invalid , please enter valid input")
