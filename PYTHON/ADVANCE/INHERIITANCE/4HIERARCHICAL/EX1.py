"""
 one parent can have multiple child class

                A

                |
                |
================================
|                              |
|                              |
B                              C
"""


""" 

                    BankAccount 

                        |
                        |
        ================================
        |                              |
        |                              |
SavingAcoount                      SalaryAccount

"""

class BankAcoount :
    def __init__(self,acno,balance) :
        self.acno= acno
        self.balanace=balance

    def display(self) :
        print(self.acno)
        print(self.balanace)


class SavingAcoount(BankAcoount) :
    def __init__(self,acno,balance) :
        super().__init__(acno,balance)   

    def Wihdraw(self,amount) :
        self.balanace-=amount 
        print("Succesfully")

    def SavingBalance(self):
        print("Withdraw success")
        print(self.balanace)


class SalaryAccount(BankAcoount) :
    def __init__(self,acno,balance) :
        super().__init__(acno,balance)
    
    def deposite(self,amount) :
        self.balanace+=amount

    def showSalryBalanc(self):
        print(self.balanace)

# ob=BankAcoount("120",25000)
# ob.display()
obj =SavingAcoount("1234",30000)
obj.Wihdraw(5000)
obj.SavingBalance()
obj.display()




obj2=SalaryAccount("1234",20000)
obj2.deposite(15000)
obj2.showSalryBalanc()
obj2.display()
