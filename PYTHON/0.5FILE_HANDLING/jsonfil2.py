import json
import json
l1 = []

no = int(input("how much data input : "))
for i in range(no) :
    d = {}
    d["Roll_no"] = int(input("Enter Roll No :"))
    d["Name"] = input("Enter Name : ")
    d["Subject"] = input("Enter Subject :")
    d["Score"] = int(input("Enter Score :"))
    l1.append(d)

with open("C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//jsonfile2create.json", "w") as m :
    json.dump(l1,m,indent=4)