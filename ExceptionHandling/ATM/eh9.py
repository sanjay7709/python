import getpass,sys
from eh7 import sbi
def atm():
    count=3
    while(True):
        pin=getpass.getpass(prompt="Enter your PIN : ")
        if(pin=="4652"):
            sbi()
        else:
            print("You have entered incorrect pin {} attempts remaining".format(count))
            count=count-1
            if(count==-1):
                print("Your card is blocked..")
                sys.exit()
