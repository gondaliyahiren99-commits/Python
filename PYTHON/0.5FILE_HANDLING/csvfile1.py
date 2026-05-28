

# data =  [
#             ["Sr_No" , "Name" , "Subject"],
#             [1 , "aaa" , "python"] ,
#             [2 , "bbb" , "java"] ,
#             [3, "ccc" , "cpp"]
#         ]

# with open("C://Users//Hiren//OneDrive//Documents//GitHub//Python//PYTHON//0.5FILE_HANDLING//csvfilecreate2.csv","w") as k :
#     # obj = csv.writer(k)
#     # obj.writerows(data)

# #this not append to writerows
#     csv.writer(k).writerows()
   

import csv 
vehicle =[
    ["Name" , "Sale" , "Profit" , "Lose"],
    ["B<W" , 45 , 600 , 0] ,
    ["Maruti" ,50 , 0 , 40000]

]

with open("car.csv","w") as f :
    obj = csv.writer(f)
    obj.writerows(vehicle)