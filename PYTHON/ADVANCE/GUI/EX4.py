from tkinter import Label
from tkinter import StringVar
from tkinter import *
import random
sc = Tk()
"""
tkinter variable 

"""
USER_NAME = StringVar()

display_msg = StringVar()
display_msg.set(" ")

user_ch_tk = StringVar()
user_ch_tk.set("")

computer_ch_tk = StringVar()
computer_ch_tk.set("PENDING")

USER_SCORE= IntVar()
USER_SCORE.set(0)
COM_SCORE= IntVar()
COM_SCORE.set(0)

u_score = 0
com_score = 0

def myGame(user) :
    
    global user_ch_tk,computer_ch_tk,USER_SCORE,COM_SCORE,u_score,com_score,USER_NAME

   
    user_ch_tk.set(user)
 
    l1 =["ROCK","PAPER","SCISSOR"]
    computer_ch = random.choice(l1)
    computer_ch_tk.set(computer_ch)
    if user==computer_ch :
       print("DRAW")

    else :
        if user=="ROCK"and computer_ch=="PAPER" or user=="PAPER" and computer_ch=="SCISSOR" or user=="SCISSOR" and computer_ch=="ROCK":
            com_score+=1
            COM_SCORE.set(com_score)

        elif user=="ROCK" and computer_ch=="SCISSOR" or user=="PAPER" and computer_ch=="ROCK" or user=="SCISSOR" and computer_ch=="PAPER":
            u_score+=1
            USER_SCORE.set(u_score)

    if u_score ==com_score :
        display = f"{user_name.get()} WON"

sc.geometry("800x500")
sc.config(background="#0A7C6E")
sc.title("ROCK PAPER SCISSOR")

title_text = Label(sc,text="**Welcome to Game**",font=("Arial",18,"bold"),bg ="#F9BAD9",fg = "white")
title_text.pack()

user = Label(sc,text="USER_NAME :-",font=("arial",10,"bold" ),bg="#FF6B35",fg="black").place(x=20,y=200)
user_name= Label(sc,textvariable=USER_NAME,font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=120,y=200)
e1 = Entry(sc,textvariable=USER_NAME).place(x=130,y=200)

btn1 = Button(sc,text="ROCK",width=6,height=1,font=("arial",18,"bold"),bg="#F59E0B",fg="black",command=lambda : myGame("ROCK"))
btn1.place(x=100,y=80)

btn2 = Button(sc,text="PAPER",width=6,height=1,font=("arial",18,"bold"),bg="#F59E0B",fg="black",command=lambda : myGame("PAPER"))
btn2.place(x=350,y=80)

btn3 = Button(sc,text="SCISSOR",width=7,height=1,font=("arial",18,"bold"),bg="#F59E0B",fg="black",command=lambda : myGame("SCISSOR"))
btn3.place(x=600,y=80)

user_choice = Label(sc,text="USER_CHOICE :-",font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=270,y=200)
U_CHOICE = Label(sc,textvariable=user_ch_tk ,font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=380,y=200)
#u_score
Label(sc,text="USER_SCORE :-",font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=520,y=200)
#U_SCORE

com_ch = Label(sc,text="COM_CHOICE  :-",font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=270,y=300)
COM_CHOICE = Label(sc,textvariable=computer_ch_tk,font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=380,y=300)
#com_score
Label(sc,text="COM_SCORE   :-",font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=520,y=300)
 #COM_SCORE
Label(sc,textvariable=COM_SCORE,font=("arial",10,"bold"),bg="#FF6B35",fg="black").place(x=630,y=300)

#display message 
Label(sc,textvariable=display_msg,font=("arial",10,"bold"),width=20 ,bg="white" , fg= "black").place(x=380,y=400)

sc.mainloop()

#material  ui color
