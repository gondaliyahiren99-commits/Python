# from tkinter import *

# reen = Tk()

# reen.geometry("600x300")
# reen.title("MY App")

# text = Label(reen, text= "Welcome to MyGUI APP",font = ("Arial",26,"Bold"),bg= "purple",fg ="white") 
# text.pack()

# reen.mainloop()

# from tkinter import *

# s = Tk()

# label = Label(s, text="Hello Tkinter")
# label.pack()

# s.mainloop()

# #=================================================================================================================

from tkinter import *

reen = Tk()

def act():
    print("Button Clicked")

btn = Button(reen, text="Click", command=act)
btn.pack()

reen.mainloop()

#=================================


