class DepositError(Exception):pass
class WithdrawError(Exception):pass
class InsufficientFundError(Exception):pass
def atmenu():
    print("*"*50)
    print("\tATM Operations")
    print("*"*50)
    print("\t1.Deposit")
    print("\t2.Withdraw")
    print("\t3.balenq")
    print("\t4.Exit")
    print("*"*50)