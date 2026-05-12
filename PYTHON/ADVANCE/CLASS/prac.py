class Add :
    l1 =[]
   
    def student(self,name,roll) :
        a={}
        self.name =name
        self.id =roll

        a["Name"] = self.name
        a["Roll_No"]=self.id
        self.l1.append(a)         
obj =Add()
for i in range(2) :
    n = input("Enter NAme")
    num =int(input("Enter NUmber :"))
    
    obj.student(n,num)
print(obj.l1)