#simple  

class a :
    def displayA(self) :
        print("A class")

class b(a) :
    def displayB(self) :
        print("class a is hear :")
        print("B")

obj = b()
obj.displayA()
obj.displayB()



#===================================================================
#ith init and super init

class Student :
    def __init__(self , name ,course) :
        self.name = name
        self.course = course 
    

class Hiren(Student) :
    def __init__(self,name,course):
        super().__init__(name,course)
  
        
    def display(self) :
        print(self.name)
        print(self.course)

h = Hiren("Hiren", "python")
h.display()


#================================================================

#iinherit ke karan init auto call hoga jab child ka object create karenge

class Vehicle :
    def __init__(self,speeed) :   #__init__() jo constructer he wo call tab hoga jab object crate time 
        self.speed = speeed 

class Car(Vehicle) :
    def CarSpeed(self) :
        return self.speed
    
C=Car(60)
sp=C.CarSpeed()
print(sp)

#==================================================

class Person() :
    def __init__(self,voice, name) :
        self.voice = voice
        self.name = name 

class Student(Person):
    def __init__(self , voice , name) :
        super().__init__(voice, name)  #jab oarent class or child claas dono me __init__() use ho tab super().__ini__ka use hota he
        #jo object time args me di gai value ko lekar parents class me diye gaye __init__() me pass karega or saved karega
        

    def Display(self) :
        print(self.name , self.voice)
N  = input("ANimal Name : ")
V = input("ENter Voice : ")
S= Student(V, N)
S.Display()

#==========
# import os
#=====================================================================
# import json
from datetime import datetime
#prnding add to jsom file please create json and alll deta


class DicCreate :
    di = {}
    def set(self, n , r , s)  :
        self.name = n
        self.Roll = r
        self.subject = s
        sub= {}
        sub["Roll"] = self.Roll
        sub["Subject"] = self.subject
        self.di[self.name] = sub
    
    def display(self) :
        print(self.di)

    # def  jsonfile (self) :
    #     pass
d = DicCreate()
n= int(input('Enter Number Add detasil : '))  
for i in range(1 , n) :
    name = input("Enter Name :" )
    roll =  int(input("Enter student id : "))
    s = input("Enter Subject ;")
    d.set(name , roll, s)
     
d.display()



# class  A : 
#     def __init__(self , name) :
#         self.name = name

# class B(A) :
#     def __init__(self , name , sur) :
#         super().__init__(name) 
#         self.surname = sur

#     def dis(self) :
#         print(self.name , self.surname)

# b = B("Hiren" , "Gondaliya")
# b.dis()


# class Animal :
#     def __init__(self ,eat) :
#         self.eat = eat

#     def EAtis(self) :
#         print(self.eat)

# class Dog(Animal) :
#     def __init__(self, eat , voie) :
#         super().__init__(eat)
#         self.voice = voie

#     def display(self) :
#         print(self.eat , self.voice)


# d = Dog("Biladi" ,  "Miyauuaooooo....!")
# d.display()
# d.EAtis()
