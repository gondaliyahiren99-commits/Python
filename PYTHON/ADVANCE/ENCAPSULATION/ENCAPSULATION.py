"""
encapsulation : is a look like capsule which is provide data hoding

encapsulation which is provide getter and setter

syntax :

    class<classname>:
        def gettemethod() :
            pass
        def settermethod() :
            pass

encapsulation data or method ko direct acess nahi karene deta wo hide karke rakhta jhe jabhi usme set  karan aho 
increse karana ya fir decrese karna ho to uske liye particuler method use karte he

ex bank me hum balance directly chanege nahai kr sakte 
agar karna ho to hume deposite ya withdraw jki method use karni padegi

"""
class Student :
    def __init__(self,r,n) :
        self.__id =r
        self.__name = n

    def getid(self) :
        return self.__id
    
    def getname(self) :
        return self.__name
    
    def setid(self,id) :
        self.__id = id
    
    def setname(self,name) :
        self.__name = name

obj = Student(12,"janaki")
print(obj.getname())
obj.setname("Mahek")
print(obj.name)
print(obj.getid())
obj.setid(22511)
print(obj.getid())

#================================================================================================================================

class student :
    def __init__(self,marks) :
        self.__marks = marks

    def add(self, mark):
        self.__marks+=mark

    def show(self):
        print(self.__marks)

s= student(45)
s.add(75)