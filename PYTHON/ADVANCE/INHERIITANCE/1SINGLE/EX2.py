class Bank :
    def __init__(self,balance ,account) :
        self.balance= balance
        self.account=account

    def show(self) :
        print(self.balance)
        print("Parent")

class User(Bank):
    def Withdraw(self,amount) :
        self.balance-=amount

    def show(self):
        # Bank.show(self)   agar same name ke function ho to wo apne me dhundehga agr nahi mila to uske najdika 
        # hume koi specific class ki value chahiye to hum usko hi call karva denge
        print(self.balance)
        print("User")

U = User(50000,"12345")
U.Withdraw(20000)
U.show()
