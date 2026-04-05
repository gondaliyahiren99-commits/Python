from random import random
import random

status = True
user_count=0
comp_count=0

while status:
    user_dice = random.randint(1,6)
    comp_dice= random.randint(1,6)

    print(f"user Dice ={user_dice} ")
    print(f"Computer Dice = {comp_dice} ")



    if user_dice+user_count<=100:
        user_count+=user_dice
    else:
        print(f,"user need dice to rech 100=",100-user_count)

    if comp_dice+comp_count<=100:
        comp_count+=comp_dice
    else:
        print(f,"computer need dice to rech 100=",100-comp_count)



    if user_count==17:
        user_count-=10
        print("Snack Bite! -10")
    elif comp_count==17:
        comp_count-=10
        print("Snack Bite! -10")
    elif user_count ==60:
        user_count-=42
        print("Snack Bite! -42")
    elif comp_count==60:
        comp_count-=42
        print("Snack Bite! -42")
    elif user_count==83:
        user_count-=19
        print("Snack Bite! -19")
    elif comp_count==83:
        comp_count-=19
        print("Snack Bite! -19")
    elif user_count==87:
        user_count-=63
        print("Snack Bite! -63")
    elif comp_count==87:
        comp_count-=63
        print("Snack Bite! -63")
    elif user_count== 93:
        user_count-=20
        print("Snack Bite! -20")
    elif comp_count==93:
        comp_count-=20
        print("Snack Bite! -20")
    elif user_count==99:
        user_count-=53
        print("Snack Bite! -53")
    elif comp_count==99:
        comp_count-=53
        print("Snack Bite! -53")
    elif user_count==4:
        user_count+=10
        print("Staircase ")
    elif comp_count==4:
        comp_count+=10
    elif user_count==9:
        user_count+=22
    elif comp_count==9:
        comp_count+=22
    elif user_count==20:
        user_count+=18
    elif comp_count==20:
        comp_count+=18
    elif user_count==29:
        comp_count+=55
    elif user_count==40: 
        user_count+=19
    elif comp_count==40:
        comp_count+=19
    elif user_count==63:
        user_count+=18
    elif comp_count==63:
        comp_count+=18
    elif user_count==71: 
        user_count+=20
    elif comp_count==71:
        comp_count+=20
   
    

    print("computr score.........!= user",comp_count)
    print("user score............!",user_count)
    print("Do you wanrt to continue........!")
    cont_inue=input("if you enter y or Y so game will statarr.....:")
    if cont_inue=="y" or "Y":
        status=True
    else:
        pass
    
    if user_count==100 :
        print("You won.............")
        status =False