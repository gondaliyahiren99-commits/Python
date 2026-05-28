import random
import time
print("\n\n")
print("\t\t" + "=" * 50)
print("\t\t   *=*=*=*=> WELCOME TO HOUSIE GAME <=*=*=*=*")
print("\t\t" + "=" * 50)
game_active = True
player= int(input("\n\n\t\t\tEnter Number Of player :  ".upper()))
ticket_list=[]
di = {}
tic=0
tic_gen = int(input("\t\t\tEnter how much per player ticket genrate :  ".upper()))
print("\n\t\t\t---------------------------------------------------")
n= player*tic_gen
# kaha tak ticket genrate ki range rakhni he
end = 90  if n<90 else n

#ticket list create per player
while tic<n:
    ticket= random.randint(1,end)
    if ticket in ticket_list:
        continue
    else:
        ticket_list.append(ticket)
        tic+=1
print("\n")
# name of player
di={}
for i in range(player):
    name = input(f"\t\t\tenter name player  {i +1}    :  ".upper())
    di[name] = []

# per player ticket disribution
print("\n\t\t\t" + "=" * 50)
print("\t\t\t   *=*=*=*=>ticket genrate per player <=*=*=*=*".title())
print("\t\t\t" + "=" * 50)
time.sleep(4)
for k , v in di.items():
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
    print(f"\t\t\tplayer :  {k}\n\t\t\tticket : {v}\n".upper())
#random tickete
lst=[i for i in range(1,end)]

# game start 
if  game_active :
    random.shuffle(lst)
    for i in lst:
        input("\t\t\tEnter for ticket >>>>>>>>>>>\n\n".upper())
        print(f"\t\t\t<<Ticket no is::>> {i}\n".upper())
        # time.sleep(2)
        if input:
                for k,v in di.items():
                    if i in v:
                        # print(f"BEFORE REMOVE {di}")
                        v.remove(i)
                        print(f"\t\t\t  <<  MATCH ! >> {k} Remaining tickets: {len(v)} ticket is :{v}".upper())
                        # print(f"AFTER REMOVE {di}")
                        if not v:
                            print(f"\t\t\t\tContratulation ! player {k}".upper())
                            print(f"\n\t\t\t\t<<<<<<<<<<<<<<<<<<<<<< {k} is winner>>>>>>>>>>>>>>>>".upper())
                            print("\n\t\t\t\tGame Over !".upper())
                            game_active=False
                            break
                    else :
                        print(f"\t\t\t\t          {k}  Remaining tickets: {len(v)} ticket is :{v}".upper())
                    print("\n")   
        if not game_active :
            break
