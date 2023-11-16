# ATM ops()
from eh6 import atmmenu,DepositError,InsufficientFundError,WithdrawError
import sys
#from os import system
from eh8 import Deposit,Withdraw,balenq
#system('cls')
def sbi():
    while(True):
        atmmenu()
        try:
            ch= int(input("enter your choice: "))
            match(ch):
                case 1: 
                    try:
                        Deposit()
                    except ValueError:
                        print("Dont enter str, symbols, alnum")
                    except DepositError:
                        print("Dont deposit -ve or Zero as input values")
                case 2:
                    try:
                        Withdraw()
                    except ValueError:
                        print("Dont enter str, symbols, alnum")
                    except WithdrawError:
                        print("Dont withdraw -ve or Zero as input values")
                    except InsufficientFundError:
                        print("You dont have sufficeint funds....")
                case 3:
                        balenq()
                case 4: 
                    print("Thanks for using application")
                    sys.exit()
                case _: 
                    print("Try again, entered choice is wrong: {}".format(ch))
        except ValueError:
            print("Dont enter str, symbols, alnum")