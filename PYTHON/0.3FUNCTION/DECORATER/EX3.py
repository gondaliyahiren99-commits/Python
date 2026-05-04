data={'email':'a@gmail.com','pas':"123456",'name':'mustved'}
def login():
    email=input("enter your email :").lower()
    pas=input("enter your password :")
    if email==data['email'] and pas==data['pas']:
        print('successfully login'.upper())
    else:
        print('invalid data!!'.title())
def dashbord():
    email=input("enter your email :").lower()
    pas=input("enter your password :")
    if email==data['email'] and pas==data['pas']:
        print('welcom to desh board')
    else:
        print('invalid data!!'.title())
def profile():
    email=input("enter your email :").lower()
    pas=input("enter your password :")
    if email==data['email'] and pas==data['pas']:
        print('welcom to profile')
    else:
        print('invalid data!!'.title())
while 1:
    menu=int(input("""
                                :MENU:
                            press 1 for login
                            press 2 for dashbord
                            press 3 for profile
                            press 4 for exit
    
    enter your choice :"""))
    if menu==1:
        login()
    elif menu==2:
        dashbord()
    elif menu==3:
        profile()
    else:
        break
    