from random import random
import random
print("Welcome to housie game")
player= int(input("Enter Number Of player :"))

ticket_list=[]
di = {}
tic=0
tic_gen = int(input("Enter how much per player ticket genrate :"))
n= player*tic_gen
if 90>=n:
    end= 10
else:
    end =n
#ticket list create per player 
while tic<n:
    ticket= random.randint(1,end)
    if ticket in ticket_list:
        continue
    else:
        ticket_list.append(ticket)
        tic+=1
#name of player
for i in range(player):
    name= input("Enter Name :")
    di[f"{name}"] = []

# per player ticket disribution
for k in di.keys():
    status=True
    i=0
    while status :
        if tic_gen>i :
            t= random.choice(ticket_list)
            di[k].append(t)
            ticket_list.remove(t)
            i+=1
        else:
            status=False
print(di)
status = True
while status :
    
    num=random.randint(1,10)
    print(num)
    input("Enter.......")
    if input :
        for k in di:
            if num in di[k]:
                di[k].remove(num)
                print(di)
                if len(di[k])==0:
                    status=False
                    break
                    print(di)
            else:
                continue
# from random import random
# import random
# di ={ "hiren": [1,2,3],
#       "Mahesh" : [4,5,6]
#     }
# status = True
# while status :
#     num= random.randint(1,10)
#     print(num)
#     i= input("Enterr..........>>>>>>>>>>>>>")
#     if i :
#         for j in di:
#             if num in di[j]:
#                 di[j].remove(4)
#                 print(di)
#                 if not di[j] :
#                     print(f"{j} is winner...")
#                     break
#                     status=False
#             else:
#                 break
