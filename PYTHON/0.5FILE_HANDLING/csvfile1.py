import csv 

data =  [
            ["Sr_No" , "Name" , "Subject"],
            [1 , "aaa" , "python"] ,
            [2 , "bbb" , "java"] ,
            [3, "ccc" , "cpp"]
        ]

with open("C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//csvfilecreate2.csv","w") as k :
    # obj = csv.writer(k)
    # obj.writerows(data)

#this not append to writerows
    csv.writer(k).writerows()
   