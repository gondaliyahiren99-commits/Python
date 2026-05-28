
from  abc import ABC , abstractmethod

class Vehicle(ABC) :
    @abstractmethod
    def wheel(self, no_of_wheel):
        pass

    @abstractmethod
    def brand(self, brand_name) :
        pass


class CAr(Vehicle) :
    def wheel(self , no_of_wheel) :
        self.no_of_wheel = no_of_wheel
        print(self.no_of_wheel)


    def brand(self , brand_name) :
        self.brand_name =brand_name
        print(self.brand_name)

class Bike(Vehicle) :
    def wheel(self , no_of_wheel) :
        self.no_of_wheel = no_of_wheel
        print(self.no_of_wheel)


    def brand(self , brand_name) :
        self.brand_name =brand_name
        print(brand_name)


# car = CAr()
# car.wheel(4)
# car.brand("BMW")
# b = Bike()
# b.brand("Honda")
# b.wheel(2)

# from ADVANCE.INHERIITANCE.1SINGLE.EX2 import Bank
# from abc import ABC, abstractmethod
# class Bamk(ABC):

#     @abstractmethod 
#     def Deposite(self , ) :
#         pass
#     def Withdraw(self , amount) :
#         pass

# class SBI(Bamk) :
#     def Deposite(self , amount) :
#         self.balance -=amount

#     def Withdraw(self , amount) :
#         self.Withdraw +=amount

# class ICICI(Bank):
#     def Deposite(self , amount) :
#         self.balance -=amount

#     def Withdraw(self , amount) :
#         self.Withdraw +=amount

# s =SBI()
# s.Deposite(1500)
# i = ICICI()
# i.Deposite()
# i.Withdraw()

# from abc import ABC , abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self)  :
#         pass

# class Circle(Shape) :
#     def __init__(self , r ) :
#         self.radius = r

#     def area(self) :
#         print(f"Area Of  Circle = {self.radius*self.radius*3.14}")

# class Square(Shape) :
#     def __init__(self , s) :
#         self.side = s
#     def area(self) :
#         print(f"Area of Square = {self.side*self.side}")

# c= Circle(5) 
# s = Square(7)
# c.area()
# s.area()


from os import name
from abc import ABC , abstractmethod
class student(ABC) :
    @abstractmethod
    def Info(self , name , roll ) :
        pass
class Hiren(student) :
    def Info(self , name , roll) :
        self.name = name
        self.id = roll
        print(self.name , self.id)

class Mahesh(student) :
    def Info(self , name , roll) :
         self.name = name
         self.id = roll
         print(self.name ,self.id)

h = Hiren()
h.Info("Herry" , 99)


from abc import ABC, abstractmethod
class A(ABC) :
    @abstractmethod
    def pay(self , amount):
        pass

class Gpay(A) :
    def pay(self , amount):
        self.amount = amount
        print(f"Pay By Gpay.....! {self.amount}")

class Ppay(A):
    def pay(self,amount):
        self.amount = amount
        print(f"Pay By Ppay....! {self.amount}")

g=Gpay()
p = Ppay()
g.pay(1500)
p.pay(9000)


