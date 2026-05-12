class Student :
    name = "Vicky"
    def display(self,name,subject) :
        self.n1 = name
        self.s1 = subject
        print(f"name : {self.n1}")
        print(self.name)       #  Vicky  ~~> in class declare data member direct acess by seelf keyword  

obj =Student()
obj.display("A","python")


#=========================================================
# class Student :
#     def fun(self,name) :
#         self.name = name
#         b = iter(self.name)
#         print(next(b))
#         print(next(b))

            

# c =Student()
# c.fun([1,2,3,4,5,6,7,8,9,10])

#=========================================================
class Student :
    def __info(self, name , roll) :
        self.name = name
        self.roll = roll
        print(f" name : {self.name} id : {self.roll}")

        
    def publicofinfo(self , name , roll):
        self.__info(name , roll)
S = Student()
S.publicofinfo("hiren" , 256)

print(S.roll)