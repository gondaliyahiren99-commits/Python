class student :
    name= "Hiren"
    def __init__(self) :
        print("Elcome")
    
    def __del__(self):
        print("del")
     
obj = student()
del obj
