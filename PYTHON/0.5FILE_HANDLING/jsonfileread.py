import json
data = ""
h ="C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//jsonfilwrite1create.json"
with open(h,"r") as j :
    data = json.load(j)
print(data)
print(data["naem"])
