# from tkinter import constants
# from tkinter import constants
# from tkinter import Menu
# from tkinter import *
# from tkinter import messagebox


# # sc= Tk()
# # sc.config(background="blue")

# # #agr hume yeh box ko screen [r kakha ] )dilhana je
# # sc.geometry("500x500+100+50")
# # sc.title("Notepad")


# # #new 

# # def newComand():
# #     text_area.delet(1.0,end)
# # #menubar
# # menu_bar = Menu(screen)

# # def openCommand():
# #     file = filedia;oges,askopenfi;ename(fi;etypes=[("Text Document" ,"*.Text*"),("All file","*.*")])
# #     if file :
# #         f = open(file,"r")
# #         data = f.read()
# #         text_area.delte(1.0,end)
# #         text_area.insert(END,data)
# #         f.close()


# # #savee
# # def SaveCommand():
# #     file = filedia;oges,askopenfi;ename(fi;etypes=[("Text Document" ,"*.Text*"),("All file","*.*")])
# #     if file :
# #         data = text_area.get(1.0,END)
# #         f = open(file,"w")
# #         f.write(data)
# #         f.close()


# #     #exit 
# # def exitCommand():
# #     screen.destroy()

# # def aboutusof():
# #     messa.showinfo("eny string")

# # #file menu
# # file_menu = Menu(menu_bar,tearoff=0)

# # file_menu.add_command(label="NEw" ) # new option create
# # file_menu.add_command(label="Open", command= openCommand)
# # file_menu.add_command(label="Save",command=SaveCommand)
# # file_menu.add_separator() # single line create 
# # file_menu.add_command("Exit")
# # file_menu.add_cascade(label="File",menu=file_menu)

# # #aboutmenu
# # about_menu = Menu(menu_bar,tearoff=0)
# # about_menu.add_command(label="About  Us")
# # about_menu.add_cascade(label= "File",menu = file_menu)

# # #helpmenu
# # help_menu =Menu(menu_bar,tearoff=0)
# # help_menu.add_command(label="Help")
# # help_menu.add_cascade(label="Help",menu=help_menu)
# # sc.config(menu=menu_bar)
# # sc.mainloop()

# sc = Tk() # window create karta he
# sc.geometry("450x450+1000+100") # widow mw size create karata he
# sc.title("My Notepade")   # upper ka title deta he 
# sc.config(background="#4dd0e1") # uske bg ke liye 

# # help ka message show karne ke liye
# def show():
#     messagebox.showinfo("HELP","SORRY WE CANT HELP TO YOU\
#         \n ITS YOUR PROBLEM\n HANDLE IT")

# #file se bahat nikalne ke liye
# def Bahar():
#     sc.destroy()

# m_b = Menu(sc) # ye topp meu bar creaate karta he
# file_menu = Menu(m_b,tearoff=0) # ye drop down menu bar create karta he (inside menu jo temporary hota he)
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Close")
# file_menu.add_command(label="Save")
# file_menu.add_separator()
# file_menu.add_command(label="Exit",command=Bahar)
# m_b.add_cascade(label="File",menu =file_menu)  # menu ye inbuilt he koi object nahi he ye  file_menu ko File se attech karega



# a_b = Menu(m_b,tearoff=0)
# a_b.add_command(label="About Us")
# m_b.add_cascade(label="About",menu = a_b)



# he_lp = Menu(m_b,tearoff=0)
# he_lp.add_command(label ="help",command=show)
# m_b.add_cascade(label="HELP",menu=he_lp)



# vie_ww = Menu(m_b,tearoff=0)
# vie_ww.add_command(label="statu Bar")
# vie_ww.add_command(label="Word Wrap")
# m_b.add_cascade(label="view",menu=vie_ww)



# view2 = Menu(m_b,tearoff= 0)
# view2.add_command(label="Helo")
# m_b.add_cascade(label="VIEW2",menu=view2)



# sc.config(menu =m_b)  #screen pr visible karna
# sc.mainloop() #application ko continuasolly run karna-->tab hi screen visible 


#==========================================================


from tkinter import StringVar
from io import StringIO
from tkinter import COMMAND
from tkinter import Button
from tkinter import font
from tkinter import Label
from tkinter import *
s = Tk()
s.geometry("250x400+900+20")
s.config(background="pink")

#variable
n1 = IntVar()
n1.set("    ")

n2 = IntVar()
n2.set("   ")

n3= StringVar()
n3.set("")

display_ans = IntVar()
display_ans.set(0)


#line
Label(s,text="____________________________________________________________________________",font="bold",bg="pink").place(x=0,y=100)

def add():
    global n1,n2,n3,display_ans
    num1 = n1.get()
    num2 = n2.get()
    op = n3.get()
    dis_messag= display_ans.get()
    if op == "+":
        ans = num1+num2+dis_messag
        display_ans.set(ans)

def reset():
    #5+5*5=30
    global n1,n2,n3,display_ans
    

#num1
Button(s,text="Enter Number 1 :",font=('arial',10,"bold"),bg = "yellow",bd=6).place(x=5,y=150)
Entry(s,textvariable=n1,font=("arial",15,"bold"),bg="white",bd=6,).place(x=125,y=150)

# #oprater
# Entry(s,textvariable=n3,font=("arial",10,"bold"),width=7,bg="white",bd=5).place(x=70,y=200)

# #num2
# Button(s,text="Enter Number 2 :",font=('arial',10,"bold"),bg = "yellow",bd=6).place(x=5,y=250)
# Entry(s,textvariable=n2,font=("arial",15,"bold"),bg="white",bd=6).place(x=125,y=250)

#ans
Button(s,text="ANS",font=("arial",10,"bold underline"),bg="black",fg="white",command=add,bd=6).place(x=80,y=300)

#reset
#ans
Button(s,text="Reset",font=("arial",10,"bold underline"),bg="black",fg="white",command=reset).place(x=150,y=300)

#display_ans
Label(s,textvariable=display_ans,font=("arial",20,"bold"),bg="pink",fg="black").place(x=200,y=80)

# # + Button
# Button(s,text="+",font=("arial",20,"bold"),fg="black").place(x=200,y=330)


s.mainloop()

