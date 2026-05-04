data={'email':'a@gmail.com','pas':"123456",'name':'mustved','check_login':False}
def login():
    email=input("enter your email :").lower()
    pas=input("enter your password :")
    if email==data['email'] and pas==data['pas']:
        print('successfully login'.upper())
        data['check_login']=True
    else:
        print('invalid data!!'.title())

def decorator(fun):
    def wapper():
        if data['check_login']==True:
            fun()
        else:
            print("---------------login first------------".upper())
            return 0
    return wapper
@decorator
def dashbord():
    print("........welcom to dashbord.....")
@decorator
def profile():
    print('walcom to profile')
@decorator
def logout():
    print('::logout successfully::')
    data['check_login']=False
while 1:
    menu=int(input("""
                                :MENU:
                            press 1 for login
                            press 2 for dashbord
                            press 3 for profile
                            press 4 for logout
                            press 5 for EXIT
    
    enter your choice :"""))
    if menu==1:
        login()
    elif menu==2:
        if dashbord()==0:
            continue
    elif menu==3:
        profile()
    elif menu==4:
        logout()
    else:
        break