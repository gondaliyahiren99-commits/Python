"""
 is  a combination of single leve; , miultipe and hiarchical combinartion

 Eg,
   A
   |
   |
   B---------------C
   |               |
   |               |
   C
   +++++++++++++++++++
          D



                                 Vehicle
                                    |
                                    | 
                        ---------------------------
                        |                         |
                        |                         |
                      car                  Elctricle car
                        |                         |
                        -------------------------
                                    |
                                  tesla
"""

# class Vehicle: 
#     def info(self) :
#         print("This is info about vehicle class")

# class Car(Vehicle) :
#     def displayCar(self) :
#         print("informationabout car regarding")

# class ElectricCAr(Vehicle) :
#     def displayEcar(self) :
#         print("informaooon about Electric Car :")

# class Tesla(Car,ElectricCAr) :
#     def displayBattery(self) :
#         print("provide car")

    
# obj = Tesla()
# obj.info()
# obj.displayCar()
# obj.displayECar()
# obj.displayBattery()



class Dada :
    __money = 500
    P_MOney= 500 - 400
    def punMony(self, P_MOney) :
        print(self.punMony)

class Father(Dada) :
    def Money_Acess(self) :
        print(D.P_MOney)
        print(self.__money)  #cant acess

D = Father()
D.Money_Acess()

  