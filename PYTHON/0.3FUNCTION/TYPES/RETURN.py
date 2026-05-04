d={}
def registration():
    print("\n---------------------------------------")
    email=input('\nenter your email :'.upper())
    if email in d:
        return print("this name is alredy exist!!\n".upper())
    pas=input("enter your password :")
    name=input("enter your name :".upper()).title()
    d[email]={'name':name,'password':pas}
    return print('registration done successfully..\n'.upper())
def login():
    print("\n-----------------------:Login:------------------------------\n")
    email=input("enter your email :".upper())
    if email not in d:
        return print("-----------:register first:------------")
    pas=input("enter your password :".upper())
    if pas!=d[email]['password']:
        return print("possword dose not match....\n\n")
    return print(f"---------------------:wlcome {d[email]['name']}:-----------------------")
while 1:
    ch=int(input("""
                                ::menu::
                        press 1 for registration
                        press 2 for login 
                        press 3 exit
    
    enter your choice :""".upper()))
    if ch==1:
        registration()
    elif ch==2:
        login()
    elif ch>=4 or ch<=0:
        print("\n\n\t\twrong input\n--------------------------------------".upper())
        continue
    else:
        break