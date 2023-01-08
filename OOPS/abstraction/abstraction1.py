
# Abstraction :

from abc import ABC,abstractmethod

class bank(ABC):                # interface

    @abstractmethod
    def check_balance(self):
        pass
    
    @abstractmethod
    def deposite(self):
        pass
    
    @abstractmethod
    def wid(self):
        pass

class gpay(bank):

    def __init__(self):
        self.balance = 1000
    
    def check_balance(self):
        return "Current balance is " + str(self.balance)
    
    def deposite(self,depo):
        self.balance = self.balance + depo
    
    def wid(self,wid):
        self.balance = self.balance - wid

class phonepay(bank):

    def __init__(self):
        self.balance = 1000
        self.wallet = 0
    
    def check_balance(self , check):
        if check == "account":
            return "Current account balance is " + str(self.balance)
        elif(check == "wallet"):
            return "Current wallet balance is " + str(self.wallet)
    def deposite(self,depo):
        self.balance = self.balance + depo
    
    def wid(self,wid):
        self.balance = self.balance - wid
    def add(self,add):
        self.wallet = self.wallet + add

def main1():

    upi = gpay()
    print(upi.check_balance())
    upi.deposite(500)
    print(upi.check_balance())
    upi.wid(200)
    print(upi.check_balance())

main1()

def main2():
    upi2 = phonepay()
    print(upi2.check_balance("account"))
    upi2.deposite(200)
    print(upi2.check_balance("account"))
    print(upi2.check_balance("wallet"))
    upi2.add(200)
    print(upi2.check_balance("wallet"))

main2()