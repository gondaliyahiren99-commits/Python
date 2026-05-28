from os import truncate
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
import dataclasses
from random import random
from time import time
import time
import random
print("______________________________________________________________Welcome To KBC______________________________________________________________")
Que = [
    {       'q':"Who is prime minister of india ?",
            'op':["Narendra Modi" , "Salman Khan" ,"Akshay Kumar" ,"Anil Kapoor"],
            "ans": "Narendra Modi",
            "50-50":["Narendra Modi" , "Salman Khan" ]
    }
    ,      
    {
            'q':"who is finance minister ?",
            'op':["Jaya Bacchan" ,"Dropdi Murmu" , "Maduri Dixt","Nirmala Sitaraman"],
            'ans': "Nirmala Sitaraman",
            "50-50": ["Jaya Bacchan","Nirmala Sitaraman"]
    
    },
    {
            'q':"How much long Sea of Gujrat?",
            'op':["1500" ,"1300" , "2000 ", "1600"],
            'ans': "1600",
            "50-50": ["2000","1600"]
    },
    {
            'q':"what is indian currencyr ?",
            'op':["Doolar" ,"Ruppe" , "Chandi ","Sonu"],
            'ans': "Ruppe",
            "50-50": ["Ruppe","Chandi"]
    }
 ]
prize=[1000,2000,5000,10000,20000,40000,80000,160000,320000,640000,125000,2500000,5000000,10000000]
i=1
status = True
choice= """
        Click 1. for answer
        Click 2. for lifeline
        Click 3. for exit the game
        """.upper()
Life_Line=["for 5050","phone a friend","skip"]
game_in = True
if game_in:
    prizeWOn= 0
    random.shuffle(Que)
    name = input("Enter User Name : ")
    for n,Q in enumerate(Que,1):
        print(f"Que No {n} for {prize[n]}")
        print(f"Que {n} : { Q['q']}")
        random.shuffle(Q['op'])
        for ch,op  in enumerate( Q['op'],97):
            print(f"\t({chr(ch).upper() }). {op}")
            if Q['ans']== op:
                Q['ans']=chr(ch).upper()
        print(choice)
        chice_in = True
        ch=int(input("Enter Choice :"))
        while chice_in:
            if ch>0 and 4>ch :
                if ch==1:
                    ans = input('Enter Answer(A/B/C/D) : ').upper()
                    if Q['ans'] ==ans:
                        print("Right  Congrats.....!")
                        prizeWOn=prize[n]
                        print(f"YOU WON {prizeWOn}\n\n")
                    else:
                        prizeWOn=0 if n>3 else prize[n]
                        game_in=False
                        break
                
                elif ch==2:
                    print(Life_Line)
                    ch =input('Enter Lifeline No :')
                    # if Life_Line[ch]
                    if ch ==1:
                        pass
                    else :
                        pass
               

                chice_in=False
            else:
                print("Enter Valid chioce :::")
        if game_in==False:
            print(prizeWOn)
            break


