name ="HIREN"
print(name.isupper()) #true

name=input("Enter name ;").upper()  #ab ye user ki har ek char
                                   # ko uppercase me store karega chahe user lower input kare

name="hiren"
print(name)
name=name.isupper()
print(name)#False
#---------------------------



name="mustved12@gmail.com"#numbers or spaciell symbols meter nhi karte isme
if name.isupper():
    print("true")
else:
    print("false")
#---------------------------


name="muSTved"  
if name.islower():
    print("lower carecter.")
elif name.isupper():
    print("upper carecter.")
else:
    print("mix carecter.")

#output :- mix character 




print("hiren".upper())#MUSTVED

print("HIREN".lower())#mustevd

name=input("enter your name :").upper()#enter your name :hiren
print(name)#HIREN

name=name.lower()
print(name)

name=input("enter your name :".upper()).upper()#ENTER YOUR NAME :python
print(name)#PYTHON

print(name.capitalize())# isme string ka first character upper hoga
#e.g neme=my name is hiren | output : My name is hiren

print(name.title())# space ke badd har ek pehle charcter ko upper me convert karta he 
#e.g neme=my name is hiren | output : My Name Is Hiren