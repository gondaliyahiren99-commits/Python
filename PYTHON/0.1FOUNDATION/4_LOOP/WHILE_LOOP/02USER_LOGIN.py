u_email = "a@gmail.com"
u_password = "123456"
userbame = "Admin"

menu = """
    menu 
press 1 for logn
press 2 for register
press 3 for extt

  
     """

status =True
while status:
    print(menu)

    choice = int(input("Enter choice :"))
    match choice:
        case 1:
            print("LOGIN")
            email =input("Enter email")
            password = input("Enter password")

            if email ==u_email and password ==u_password:
                print("login")
            else:
                print("invalid")

        case 2:
            print("REGISTER")
            uaer_name = input("Enter Name:")
            uaer_password =int(input("Enter password"))
            

        case 3:
            print("EXIT")
            status = False


    print("Do you want to continue...........yes or no :") 
    con_tinue=input("enter yes if you wnat to continue:").upper()
    if con_tinue=="YES":
        status=True
    else:
        status=False 
                

       


