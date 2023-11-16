from menu import atmenu,DepositError,WithdrawError,InsufficientFundError
import sys,os
from menud import Deposit,withdraw,balenq
os.system('cls')
def sbi():
    while(True):
            try:
                atmenu()
                ch=int(input("enter your choice: "))
                match (ch):
                    case 1: 
                        try:
                            Deposit()
                        except DepositError:
                            print("Do not deposit Zero or -ve values")
                    case 2:
                        try:
                            withdraw()
                        except InsufficientFundError:
                            print(" you dont have sufficient balance in Account xxxxxx")
                        except WithdrawError:
                            print("Dont withdraw Zero or -ve values")
                    case 3:
                        balenq()
                    case 4:
                        print("Thanks for using this application: ")
                        sys.exit()
                    case _:
                        print("You have entered invalid selection")
            except ValueError:
                print("Dont enter str,symbols and alnum characters")