import json
import os
from datetime import datetime

l1 = []
l2=[]

current = datetime.now()
hour = current.hour 

ch=input("Do you want Enter data press y :: ").upper()
while ch=="Y" :
    di ={}
    di["Name"] = input("Enter Name :")
    di["Age"] = input("Enter Age :")
    di["Vac_Name"] = input("Enter Vaccine Name :")
    di["Gender"] = input("Enter Gender :")
    di["Time"] = f"{current.time()}"
    l1.append(di)
    ch = input("DO YOU WANT TO CONTINUE :").upper()

os.chdir(os.getcwd()+"\\00_PROJECT\\MODUAL_PROJECT")  #directory change 
if os.path.exists(f"{hour}.json")  :
    with open(f'{hour}.json',"r") as f :
        data=json.load(f)
    l2=data+l1
   
    with open(f'{hour}.json',"w") as f :
        d=json.dump(l2,f,indent=4)
        
else :  
    with open(f'{hour}.json',"w") as f :
        json.dump(l2,f,indent=4)



# l1 =[12,21,23]
# l2 =[45,56,67]
# l3=l1+l2
# print(l3)