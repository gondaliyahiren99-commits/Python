student=[]

for i  in range(1,6):
    marks=int(input("student marks and name"))
    name=input("Enter name :")
    if marks>70:
        student.append(name)
    

print("TOPPERS")
for st in student:
    print(st) 

        

    
    


