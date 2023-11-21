import getpass as gp,sys
from menuops import sbi
def runsbi():
    ct=3
    while(True):
        pin=gp.getpass(prompt="Enter your pin: ")
        if(pin=="4444"):
            sbi()
        else:
            print("You have entered incorrect pin ")
            print("attemps remaining {}".format(ct))
            ct=ct-1
            if(ct==0):
                print("Your card is blocked")
                sys.exit()