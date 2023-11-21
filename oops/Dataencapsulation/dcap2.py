'''
data member level encapsulation
'''

class Account:
    def getval(self):
        self.__acno=13
        self.name="san"
        self.bankname="SBI"
        self.__branch="kMH"
        self.__pin="2465"

'''
here in the above example acno, branch and pin should be encapsulated as it is confidential data
encapuslation preceeded by  "__"   
synatx:  __datamember name
'''

"""
method level data encapsulation
"""
class Account:
    def __getval(self):
        self.acno=13
        self.name="san"
        self.bankname="SBI"
        self.branch="kMH"
        self.pin="2465"


"""
constructor level data encapsulation
"""
class Account:
    def ____init__(self):
        self.acno=13
        self.name="san"
        self.bankname="SBI"
        self.branch="kMH"
        self.pin="2465"