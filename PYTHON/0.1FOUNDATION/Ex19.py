data= {
    'email' : 'h@',
    'password': '123456',
    'username': 'hiren'

}
def login():
    email = input("Enter emial")
    password=input("Enter password :")
    if email==data['email'] and password==data['password']:
        print("succesfully :")
    else:
        print("invalid :")

def dashboard(myfun):
    email = input("Enter emial")
    password=input("Enter password :")
    if email==data['email'] and password==data['password']:
        print("welocome to dashboard :")
    else:
        myfun()

def profile():
    email = input("Enter emial")
    password=input("Enter password :")
    if email==data['email'] and password==data['password']:
        print("WELCOME TO PROFILE :")

menu="""
        MENU
    1 for login
    2 for dashbord
    3 for profil
    4 for exit
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
        status=False
