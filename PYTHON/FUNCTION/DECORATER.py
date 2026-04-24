data= {
    'email' : 'h@',
    'password': '123456',
    'username': 'hiren',
    'is_looged' : False

}
def login():
    email = input("Enter emial")
    password=input("Enter password :")
    if email==data['email'] and password==data['password']:
        print("succesfully :")
        data['is_logged']=True
    else:
        print("invalid :")


def checkloogin(myfun):
    def wrapper():
        if data['is_looged']==True:
            myfun()
        else:
            print("you must login for this :")
    return wrapper
def dashboard(myfun):
    def wrapper():
         if data['is_looged']==True:
            print("welcome")
         else :
            myfun()
    return wrapper
            

   



@checkloogin
def dashboard():
    print("Welcome to dashboard :")

@checkloogin
def profile():
    print("welcome to profile")

@checkloogin
def logout():
    data['is_looged'==False]





menu="""
        MENU
    1 for login
    2 for dashbord
    3 for profil
    4 for loged out
    5 for Exit
"""
status=True
while status:
    print(menu)
    ch=int(input("Enter choice :"))
    if ch==1:
        login()
    elif ch==2:
        dashboard()
    elif ch==3:
        profile()
    elif ch==4:
        logout()
    else:
        status=False