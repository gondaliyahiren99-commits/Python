
import json
from datetime import datetime
import json
import os
from datetime import datetime

l1 = []
no = int(input("Enter How many Add :"))
for i in range(no) :
    di = {} 
    di["Name"] = input("Enter Name :")
    l1.append(di)

c_d = datetime.now()
hour= c_d.minute
print(os.getcwd())
file = f"C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//{hour}.json"
if file == f"C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//{hour}.json" :
    with open(file , "a") as f :
        json.dump(l1,f,indent= 4)
        print("if")

else :
    with open(f"C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//{hour}.json", "w") as f :
        json.dump(l1,f,indent= 4)
        print("Else")


