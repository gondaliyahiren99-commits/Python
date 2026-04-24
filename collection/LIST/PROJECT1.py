import random

Team_List=['MI','CSK','RR','RCB','GT']
BAT_BALL=['BAT','BALL']
Toss_List=['HEAD','TAIL']
USER_SCORE_BORD=[0,0,0,0]
OP_SCORE_BOARD=[0,0,0,0,]

print("      ",end="")
for i in Team_List:
    print(f" {i} ",end="")
print("\n")
status=True
while status:
    User_Team=input("Enter Your Team :").upper()
    if User_Team in Team_List:
        status=False
    else:
        print("Re-Enter Your Team :")
print(f"   YOUR TEAM IS:- {User_Team}    \n*************************************** ")
Team_List.remove(User_Team)
OP_Team=random.choice(Team_List)
print(f"   OPOSITE TEAM IS:- {OP_Team}    \n***************************************") 
print("\n\n                                          <<<<<<<<<<<<<<<<<<<<<<   IT'S TOSS TIME >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>               ")

status=True
while status:
    Toss_Result=random.choice(Toss_List)
    print(Toss_Result)
    U_Toss_choice=input("Enter Your Toss Choice HEAD FOR 'H' or 'h'OR TAIL FOR 'T' <OR> 't'  :").upper()
    if U_Toss_choice ==Toss_List[0][0] or U_Toss_choice==Toss_List[1][0] or U_Toss_choice==Toss_List[0] or U_Toss_choice==Toss_List[1]:
        if U_Toss_choice==Toss_Result[0] or U_Toss_choice==Toss_Result:
            print("\n\n                                  <<<  Congrats! YOU WON THE TOSS  >>>>>            ")
            status=False
            User_Turn=input("Select BAt Or Ball :").upper()
            if User_Turn==BAT_BALL[0]:
                    print(f"\n\n        *=*=*=*=*=*=*={User_Team} IS BATTING   *=*=*=*=*=*=*=")       
                    status=False
                    print("--------------------Let's Play-------------------")
                    status=True
                    free_hit=True
                    while status:
                        if USER_SCORE_BORD[2]==6:
                            USER_SCORE_BORD[2]=0
                            USER_SCORE_BORD[3]+=1
                        if USER_SCORE_BORD[3]<1 and USER_SCORE_BORD[1]<2:
                            BALL_PROB=[0,1,2,3,4,5,6,"WICKET","WIDE","NO BALL"]
                            input("PressEnter>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            if input:
                                BALL_ACT=random.choice(BALL_PROB)
                                if BALL_ACT==BALL_PROB[7]:
                                    print(f"------------------its {BALL_PROB[7]}------------------")
                                    USER_SCORE_BORD[2]+=1
                                    USER_SCORE_BORD[1]+=1
                                    print(f"SCORE BOARD :{User_Team} :{USER_SCORE_BORD[0]}/{USER_SCORE_BORD[1]} {USER_SCORE_BORD[3]}.{USER_SCORE_BORD[2]} (overs)")
                                elif BALL_ACT==BALL_PROB[8]:
                                    print(f"------------------its {BALL_PROB[8]}------------------")
                                    USER_SCORE_BORD[0]+=1
                                    print(f"SCORE BOARD :{User_Team} :{USER_SCORE_BORD[0]}/{USER_SCORE_BORD[1]} {USER_SCORE_BORD[3]}.{USER_SCORE_BORD[2]} (overs)")
                                elif BALL_ACT==BALL_PROB[9]:
                                    print(f"------------------its {BALL_PROB[9]}------------------")
                                    USER_SCORE_BORD[0]+=1
                                    print(f"SCORE BOARD :{User_Team} :{USER_SCORE_BORD[0]}/{USER_SCORE_BORD[1]} {USER_SCORE_BORD[3]}.{USER_SCORE_BORD[2]} (overs)")
                                    print(f"--------------------------ITS FRRE HIT---------------------")
                                    FREE_HIT="ACTIVE"
                                elif BALL_ACT>=BALL_PROB[0] and BALL_ACT<=BALL_PROB[6]:
                                    print(f"------------------its {BALL_ACT}s Run------------------")
                                    USER_SCORE_BORD[0]+=BALL_ACT
                                    USER_SCORE_BORD[2]+=1

                                    print(f"SCORE BOARD :{User_Team} :{USER_SCORE_BORD[0]}/{USER_SCORE_BORD[1]} {USER_SCORE_BORD[3]}.{USER_SCORE_BORD[2]} (overs)")
                            if (USER_SCORE_BORD[1]<2 and USER_SCORE_BORD[3]<2)!=True:
                                status=False
                    print(f"{OP_Team} NEED {USER_SCORE_BORD[0]+1} RUN IN 6 BALL TO WIN") 
                    while status:
                        if OP_SCORE_BOARD[2]==6:
                            OP_SCORE_BOARD[2]=0
                            OP_SCORE_BOARD[3]+=1
                        if OP_SCORE_BOARD[3]<1 and OP_SCORE_BOARD[1]<2:
                            BALL_PROB=[0,1,2,3,4,5,6,"WICKET","WIDE","NO BALL"]
                            input("PressEnter>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            if input:
                                BALL_ACT=random.choice(BALL_PROB)
                                if BALL_ACT==BALL_PROB[7]:
                                    print(f"------------------its {BALL_PROB[7]}------------------")
                                    OP_SCORE_BOARD[2]+=1
                                    OP_SCORE_BOARD[1]+=1
                                    print(f"SCORE BOARD :{User_Team} :{OP_SCORE_BOARD[0]}/{OP_SCORE_BOARD[1]} {OP_SCORE_BOARD[3]}.{OP_SCORE_BOARD[2]} (overs)")
                                elif BALL_ACT==BALL_PROB[8]:
                                    print(f"------------------its {BALL_PROB[8]}------------------")
                                    OP_SCORE_BOARD[0]+=1
                                    print(f"SCORE BOARD :{User_Team} :{OP_SCORE_BOARD[0]}/{OP_SCORE_BOARD[1]} {OP_SCORE_BOARD[3]}.{OP_SCORE_BOARD[2]} (overs)")
                                elif BALL_ACT==BALL_PROB[9]:
                                    print(f"------------------its {BALL_PROB[9]}------------------")
                                    OP_SCORE_BOARD[0]+=1
                                    print(f"SCORE BOARD :{User_Team} :{OP_SCORE_BOARD[0]}/{OP_SCORE_BOARD[1]} {OP_SCORE_BOARD[3]}.{OP_SCORE_BOARD[2]} (overs)")
                                    print(f"--------------------------ITS FRRE HIT---------------------")
                                    FREE_HIT="ACTIVE"
                                elif BALL_ACT>=BALL_PROB[0] and BALL_ACT<=BALL_PROB[6]:
                                    print(f"------------------its {BALL_ACT}s Run------------------")
                                    OP_SCORE_BOARD[0]+=BALL_ACT
                                    OP_SCORE_BOARD[2]+=1
                                

                
            elif User_Turn==BAT_BALL[1]:
                print(f"\n\n        *=*=*=*=*=*=*={OP_Team} IS BATTING   *=*=*=*=*=*=*=") 
                status=False
        else:
            print("You lose the toss ")
            Op_TEam_Turn=random.choice(BAT_BALL)
            if Op_TEam_Turn==BAT_BALL[0]:
                print(f"\n\n        *=*=*=*=*=*=*={OP_Team} IS BATTING   *=*=*=*=*=*=*=") 
                status=False
            
            else:
                print(f"\n\n        *=*=*=*=*=*=*={User_Team} IS BATTING   *=*=*=*=*=*=*=")
                status=False

    else:
        print("Not valid Enter Valide:")
    


        


  



