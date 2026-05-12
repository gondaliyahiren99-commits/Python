from tkinter import StringVar
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import * 

screen = Tk()
screen.geometry("350x250")
screen.config(background="#9575cd")

msg_entry_tk = StringVar()

display_msg_tk = StringVar()
display_msg_tk.set("")

Surname = StringVar()
Surname.set("")

def setMessage():
    global display_msg_tk,msg_entry_tk
    display_msg_tk.set("Hi, "+msg_entry_tk.get())

name = Label(screen,text="Enter your name : ",font=("Arial",10,'bold'),bg="#9575cd")
name.place(x = 20,y = 30)

Label(screen,text = "Enter Your Surname",font=("Arial",10,"bold"),bg="#9575cd").place(x =20,y=70)

e1 = Entry(screen,textvariable=msg_entry_tk).place(x = 160,y=35)

btn = Button(screen,text="Submit",bd=2,width=6,height=1,bg="#7e57c2",fg="white",activebackground="#5e35b1",activeforeground="#e8eaf6",command=setMessage)
btn.place(x = 130,y = 100)
e2 = Entry(screen).place(x=160,y=70)

display_msg = Label(screen,textvariable=display_msg_tk,font=("Arial",10,'bold'),bg="#9575cd")
display_msg.place(x = 100,y = 160)

screen.mainloop()