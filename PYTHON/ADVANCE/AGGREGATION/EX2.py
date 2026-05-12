#aggregation more class and  more 

class Honda :
    def __init__(self,dress,city) :
        self.Colour = dress
        self.city = city
class Maruti :
    def __init__(self, dress, city) :
        self.Colour = dress
        self.city = city

class QDept :
    def __init__(self,salary,rate,honda,maruti) :
        self.salary = salary
        self.rate = rate
        self.compney = honda
        self.compney = maruti
    def show(self):
        print(self.compney.dress)
        print(f"color inn QDept {self.compney.Colour} \n city of QDept {self.compney.city}")
        print(f"MARUTI::color inn QDept {self.compney.Colour} \n city of QDept {self.compney.city}")

    

class WelDept :
    def __init__(self,salary ,cl,honda , maruti) :
        self.salary = salary
        self.cl = cl
        self.compney = honda
        self.compney= maruti
    def show(self):
        print(f"HONDA ::color inn WDept {self.compney.Colour} \n city of WDept {self.compney.city}")
        print(f"MARUTI::color inn WDept {self.compney.Colour} \n city of WDept {self.compney.city}")
    
honda = Honda("White","Ahemdabad")
maruti = Maruti("Black" , "Kolakata" )
q= QDept(25000,350,honda,maruti)
w= WelDept(15000,2500,honda,maruti)
w.show()
print(q.compney.Colour) # gagra same name ke aggregation ho to wo last wala ke acess karaeaga colour =