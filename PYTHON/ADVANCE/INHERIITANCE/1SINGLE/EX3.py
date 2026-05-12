# class Animal :
#     def __init__(self,voice) :
#         self.voice=voice

#     def show(self) :
#         print(self.voice)

# class Dog(Animal) :
#     def Bark(self):
#         print(self.voice)
    
# obj = Dog("Bhau..")
# obj.Bark  
# obj.show()

#============================================================

# class A :
#     def __init__(self,name):
#         self.name = name


# class B(A):
#     def __init__(self,name,year):
#         super().__init__(name)
#         self.year = year

#     def show(self):
#         print(self.name , self.year)

# b = B("Hiren" , 2027)
# b.show()

#======================================================================


# class Student :
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll

# class Marks(Student) :
#     def __init__(self,m1,m2,m3):
        
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def totalmarks(self):
#         self.total =  self.m1+self.m2+self.m3
#         print(self.total)

#     def percentOfst(self,s):
#         self.per = self.total//3
#         print(self.per)
#         print(s.name)
#         print(s.roll)

# m1 = int(input("Enter Marks 1 :"))
# m2 = int(input("Enter Marks 2 :"))
# m3 = int(input("Enter Marks 3 :"))

# n= input("ENter name : ")
# r= int(input('enter id : '))
# s = Student(n ,r )
# m = Marks(m1,m2,m3)
# m.totalmarks()
# m.percentOfst(s)


class Area :
    age = 32
    course = "python"

    def __init__(self, val):
        self.val = val
     
    def show(self):
        print(self.val)
        print(self.course)
        print("parent")
        print("#"*10)

class Circle(Area):
    val =5000
    def __init__(self,val,name):
        super().__init__(val)
        super().show()
        self.name = name 
    
    def show(self):
        print(self.age)
        print(self.val)
        print("child")
        print("#"*10)


c = Circle(2500,"Hiren")
c.show()