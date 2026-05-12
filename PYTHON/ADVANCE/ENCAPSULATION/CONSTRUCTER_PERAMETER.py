class student :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def diplay(self) :
        print(self.fname)
        print(self.lname)

fname= input("Enter fname : ")
lname = input("Enter lname : ")
 

obj = student(fname,lname)
obj.diplay()