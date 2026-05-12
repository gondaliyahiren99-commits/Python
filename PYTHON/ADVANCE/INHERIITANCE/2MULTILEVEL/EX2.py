class Vehicle :
    def __init__(self,speed,brand):
        self.speed = speed
        self.brand = brand

class Ev(Vehicle) :
    def __init__(self,speed,brand):
         super().__init__(speed,brand)
       
    def infoEV(self)  :
        print(self.speed, self.brand)

class Petroll(Vehicle):
    def infoPetroll(self) :
        print(self.speed)
        print(self.brand)

E = Ev(120,"BMW") 
