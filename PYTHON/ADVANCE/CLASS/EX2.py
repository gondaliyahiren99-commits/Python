"""
self : self is an inbuilt keyword which is represent current class value .

in c++ and java we have (this) keyword in python insted of thies we have self keyword

but at 1st positional arg we must whave to pass self keyword
"""

import _sitebuiltins
class Student :
    year = 2026
    def display(self,n) :  # we have must pass all member function in  self keyword 
        age = 2   # ye sirf class ke andar hi use ho sakta h bahar nahi  aar self lagaye to kahi pr bi acesss
        self.name =  n
        print("welcome")
        print(f"in class {self.name}")
        print(age)   #

obj = Student() 
obj.display("Hiren") # method acess
# object ke bina class ke ek bhi member functio or data member access nahi kar sakte

print(f"outside the class {obj.name}")
print(f"outside the class {obj.year}") #we can acess direc

class Bank :
    def __iniit__(self,pin):
        self.pin = pin

class 

    