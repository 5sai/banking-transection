import sys
class banking:
    ''' State Bank Of India '''
    bankname="SBI"
    def __init__(self,name,account,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("total ammount:",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient funds")
            sys.exit()
        self.balance=self.balance-amt
        print("balance after with draw:",self.balance)
print("wel come to :",banking.bankname)
name=input("enter your name:")
account=int(input("enter your account number"))
l=list(str(account))
if len(l)>11:
    print("invalid account number")
    sys.exit()
c=banking(name,account)
while True:
    print("d=deposit\nw =withdraw\ne=exit")
    k=input("choose your option")
    if k=="d" or k=="D":
        amt=float(input("enter the ammount:"))
        c.deposit(amt)
    elif k=="w" or k=="W":
        amt=float(input("enter the ammount:"))
        c.withdraw(amt)
    elif k=="e" or k=="E":
        print("thank you for visiting")
        sys.exit()
    else:
        print("invalid option.plese retry again")
     
