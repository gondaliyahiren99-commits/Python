from abc import ABC,abstractmethod
class Acoount(ABC):
   #init constructer jo abstaction nahi he
    def __init__(self,name,mono) :
        self.name = name
        self.Phone = mono
        print(self.name,self.Phone)

    @abstractmethod
    def deposite(self,amount) :
        pass

    @abstractmethod
    def Withdraw(self , amount):
        pass

    @abstractmethod
    def showbal(self):
        pass
    
class ICICI(Acoount):
    def __init__(self,balance,name ,mono):
        super().__init__(name,mono)
        self.balance = balance
        print(self.balance)
        

    def deposite(self,amount) :
        self.balance+=amount


    def Withdraw(self, amount):
        self.balance-=amount

    def showbal(self):
        print(self.balance)

class Dena(Acoount):
    def __init__(self,balance,name ,mono):
        super().__init__(name,mono)
        self.balance = balance
        print(self.balance)

    def deposite(self,amount) :
        self.balance+=amount

    def Withdraw(self, amount):
        self.balance-=amount

    def showbal(self):
        print(self.balance)

i = ICICI(15000,"Hiren" ,9725465)
i.deposite(5000)
i.showbal()
i.Withdraw(222000)
i.showbal()