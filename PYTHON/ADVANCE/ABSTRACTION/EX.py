from abc import ABC ,abstractmethod

class Parent(ABC) :  #inherit ABC (abstract Base )Class
    @abstractmethod
    def property(self) :
        pass

class Child1(Parent) :
    def property(self) :
        print("i have car" )
        return super().property()



class Child2(Parent) :
    def property(self) :
        print("i have gatkdr" )

    
class Child3(Parent):
    def property(self):
        print("I have BankBalanace")
        

c1 =Child1()
c2 = Child2()
c3 =Child3()
c1.property()
c2.property()
c3.property()
