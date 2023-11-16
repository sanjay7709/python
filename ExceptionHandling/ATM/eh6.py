# ATM operations menu
class DepositError(Exception):pass
class WithdrawError(Exception):pass
class InsufficientFundError(Exception):pass
def atmmenu():
    print("*"*50)
    print("\tATM OPERATIONS")
    print("*"*50)
    print("\t1.Deposit")
    print("\t2.Withdraw")
    print("\t3.Bal Enq")
    print("\t4.Exit")
    print("*"*50)