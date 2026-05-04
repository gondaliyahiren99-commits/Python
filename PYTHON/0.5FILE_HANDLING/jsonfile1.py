import os
import json
d = {   "id" : 1 ,
        "naem" : "hiren" ,
        "score" : 78
    }
print(d)

with open("C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//jsonfilwrite1create.json","w") as f :
    json.dump(d,f,indent=4) #what where kese (dump for write in json)
    print("succesfully")
print(os.getcwd())

#newline = "" isnt work in json file 
#just for csv