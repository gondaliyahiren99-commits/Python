class A :
    def __init__(self, name ,id) :
        self.name = name
        self.id = id
    
    def display(self) :
        print(self.name)
        print(self.id)

class B : 
    def __init__(self, name, id) :
        self.name =name
        self.id = id

    def display(self) :
        print(self.name)
        print(self.id)

class C(A , B) :
    def display(self):
        pass

c= C("hiren" , 45)
# a = A("Hiren", 123)
b = B("Hrenb", 456)
# a.display()
c.display()
b.display()

#yaha pr function overload ho raha he jo not posible he in python not same type ke function hone chahiye

class A :
    print("A")

class B(A):
    print("B")

class C(B):
    pass

c = C()