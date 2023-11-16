from menu import DepositError,WithdrawError,InsufficientFundError
bal=500.00
def Deposit():
    damt=float(input("enter the amount to be deposited: "))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("UR Account xxxxx credited amount INR: {}".format(damt))
        print("Available current balance INR: {}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter the amount to withdraw: "))
    if((wamt+500)>bal):
        raise InsufficientFundError
    elif(wamt<=0):
        raise WithdrawError
    else:
        bal=bal-wamt
        print("Ur Account xxxxx Debited amount INR: {}".format(wamt))
        print("Available Current Balance is INR: {} ".format(bal))
def balenq():
    print("Available Current Balance is INR: {}".format(bal))