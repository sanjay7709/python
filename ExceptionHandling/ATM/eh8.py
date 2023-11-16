from eh6 import DepositError,WithdrawError,InsufficientFundError
bal=500.00
def Deposit():
    damt=float(input("enter how much amount to deposit: "))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account XXXXXX credited with INR:{}".format(damt))
        print("The available balance is {} ".format(bal))
def Withdraw():
    global bal
    wamt=float(input("enter how much amount to Withdraw: "))
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InsufficientFundError
    else:
        bal =bal-wamt
        print("Debited amount INR:{} from ur Account xxxxxx".format(wamt))
        print("Current balance is INR:{}".format(bal))
def balenq():
    print("Your Current balance is INR :{}".format(bal))


