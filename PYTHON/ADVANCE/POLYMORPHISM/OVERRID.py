"""
 two class have same name  properties its called method overriding
"""

# class A :
#     def display(self) :
#         print("A ")
    
# class B(A) :
#     def display(self) :
#         A.display(self)   #a ki properties aceess
#         print("B")

# b = B()
# b.display()

# class Bank :
#     def __init__(self, Bal) :
#         self.Balance = Bal
    
#     def BalShow(self):
#         print(self.Balance)

# class Saving(Bank):
#     def __init__(self,Bal):
#         super().__init__(Bal)

#     def Withdraw(self,amount):
#         self.Balance-=amount

#     def Deposite(self, amount):
#         self.Balance+=amount

# class Current(Bank):
#     def __init__(self, Bal):
#         super().__init__(Bal)

#     def Withdraw(self,amount):
#         self.Balance-=amount

#     def Deposite(self, amount):
#         self.Balance+=amount

# s = Saving(2500)
# s.Withdraw(2000)
# s.BalShow()




# class A :
#     def __init__(self,name):
#         self.name = name

#     def show(self) :
#         print(self.name)

# class B(A) :
#     def __init__(self,name) :
#         self.name = name 
    
#     def show(self) :
#         print(self.name) 

# b = B()
# b.show()

class Bank :
    def __init__(self,name,no):
        self.name = name
        self.no = no

class SBI(Bank):
    def inrest(self):
        print("Sbi")

class HDFC(Bank):
    def intrest(self):
        SBI.inrest(self)
        print("HDFC")
        # print(self.name)
        # print(self.no)

h = HDFC("Hiren",12)
h.intrest()

