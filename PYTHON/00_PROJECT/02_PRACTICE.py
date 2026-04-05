password=input("Enter password :")

number="0123456789"
char="ABCDEFGHIKJKLMNOPQRSTUVWXYZ"
symbol="!@#$%^&*()_+-=}{[:;.,/*|\~`]"

if len(password)>=8:
    for i  in char:
        flag=0
        if password[0] in char:
            pass 
        else:
            print("Enter first letter is upper :")

    for i in char:
        flag=0
        if i in symbol:
            flag=1
    
    if flag==1:
        print("Welcome")
    else:
        print("Atleast on symbol add :")