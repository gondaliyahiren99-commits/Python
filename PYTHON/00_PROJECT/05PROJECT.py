import random
menu ="""
    MENU
1.ROCK
2.PAPER
3.SCISSOR
    """
choices =["ROCK","PAPER","SCISSOR"]
computer= random.choice(choices)

status = True
user_won=0
computer_won=0

while status:
    print(menu)
    computer= random.choice(choices)
    
    print()
    user_choice=input("Enter choice:").upper()
    
    if computer==user_choice:
        print("++++++++MATCH DRAW++++++++++++++++++++")
    elif computer=="ROCK" and user_choice=="PAPER" or computer=="PAPER" and user_choice=="SCISSOR" or computer=="SCISSOR" and user_choice =="ROCK":
        print("****************YUO ARE WON THE MATCH****************************")
        user_won+=1
    elif computer=="PAPER" and user_choice=="ROCK" or computer=="ROCK" and user_choice=="SCISSOR" or computer=="SCISSOR" and user_choice=="PAPER":
        print("*********************YOU LOSE GAME*********************************")
        computer_won+=1
    else:
        print("invalid choice ")
    print("Do you want to continue..............?  if yes enter YES else enter any key")
    con_tinue =input("Enter if you continue......:").upper()
    if con_tinue=="YES":
        status= True
    else:
        status=False

if user_won>computer_won:
    print("*********you won level********")
else:
    print("*******you lose level*********")          
