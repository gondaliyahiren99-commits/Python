class Address :
    def __init__(self , city , state , pincode) :
        self.city = city
        self.state = state
        self.pincode = pincode

class Employe :
    def __init__(self , department , salary , address) :
        self.deparrment = department
        self.salary = salary
        self.address = address

    def display(self):
        print(f"department {self.deparrment} salary {self.salary} addres ={self.address.city}")
address = Address("mumbai","Maharashtra", 526652)
obj= Employe("IT", 45000,address)
obj.display()
#=======================================================================================================================
