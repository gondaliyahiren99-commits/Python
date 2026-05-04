import random
Menu ="""
        MENU
    1 REGISTRATION
    2 USER INFO
    3 RESET PASSWORD
    4 ALL USER
    5 KYC
    6 EXIT 
"""
Menu0=  """
        1 as Bank Mangae
        2 as User
        """
roll=True
while roll:
    print(Menu0)
    roll=int(input("Enter YOuur roll :"))
    if roll==1:
        User_data={}
        status=True
        while status:
            User_info={}
            print(Menu)
            ch=int(input("ENTER YOUR CHOICE :"))
            if ch==1:
                print("--------------WELCOME TO NEW MEMBER------------")
                email=input("Enter your Email :".upper())

                if email==User_info:
                    print("Alredy Exisist :")
                else:
                    name=input("Enter NAme :".upper())
                    Mo_NO=input("Enter Your Phone Number :".upper())
                    Pass_word=input("Enter Password :")
                    Account_No=int(input("ENter ACCT NO"))
                
                    if len(Mo_NO)==10:
                        User_info['name']=name
                        User_info['Phone_No']=Mo_NO
                        User_info['password']=Pass_word

                    User_data[email]=User_info
            elif ch==2:
                while status:
                     Find=input("-----------Enter Emai Find User info---------:")
                     if Find in User_data:
                        print(f"{User_data[Find]}")
                        break
                     else:
                        print("Re-Enter :")
                        
            elif ch==3:
                print("RESET PASSWORD :")
                find=input("Enter User NAme or Mo_No:")

                input("SEnd OTP pres Enter>>>>>>>>".upper())
                if input:
                    otp=random.randint(1000,9999)
                    print(otp)
                    status=True
                    while status:
                        User_Otp=int(input("Enter OTP :"))
                        if User_Otp==otp:
                            NEW_PASSWORD=input("Enter NEW PASSWORD :")
                            User_data[find][Pass_word]=NEW_PASSWORD
                            print("==========Password changed succesfully ===========")
                            break
                        else:
                            print("RE-ENTER...............")
            elif ch==4:
                print("::::::::WELCOME TO ALL ::::::")
                print(User_data[email])

            elif ch==5:
                Kyc_status=True
                while Kyc_status:
                    Menu2=  """
                    1 ADHAR CRD
                    2 PAN
                    3 EXIT
                    """
                    print(Menu2)
                    ch=int(input("Enter Choice :"))
                    if ch==1:
                        print("Welcome to Adhar KYC :")
                        while status:
                            user=input("Enter Email :")
                            Adhar_Number =input("Enter Adhar Number :")
                            if len(Adhar_Number)==12:
                                User_data[user]['ADHAR']=Adhar_Number
                                break
                            else:
                                print("Re-Enter Adhar Number:")

                    elif ch==2:
                        print("Welcome To PAN KYC :")
                        pan_kyc=True
                        while pan_kyc:
                            user=input("Enter Email :")
                            PAN_NO =input("Enter Adhar Number :").upper()
                            if len(Adhar_Number)==5:
                                User_data[user]['PAN']=PAN_NO
                                break
                            else:
                                print("Re-Enter PAN NO :")
                    
                    elif ch==3:
                        break
            elif ch==6:
                        break           
                 
       
    elif roll==2:
        print("WELCOME TO CUSTOMER :")
        BANK_MANAGMENT={}
        ACCOUNT={}
        balance=int(input('balance :'))
        ACCOUNT['name']=name
        ACCOUNT['balance']=balance

        BANK_MANAGMENT[Account_No]=ACCOUNT
        print(BANK_MANAGMENT)
        transaction_Menu= """

                    1 show balance1
                    2 withdarw
                    3 Deposite
                    4 pin change
                    5 exit
                        """.upper()
        tran_status=True
        while tran_status:
            print(transaction_Menu)
            acct=input("Enter Account NUmber :")
            tra=int(input("Enter Your choice :"))
            if tra==1:
                valid=True
                while valid:
                    print(f"your balance is :{BANK_MANAGMENT[acct][balance]}")
            elif tra==2:
                amount=int("Enter Withdraw Amount :")
                if BANK_MANAGMENT[acct][balance]>amount:
                    BANK_MANAGMENT[acct][balance]-amount
                else:
                    print("indufiicient balannce :")
                print(f"After Withdraw your balance is {BANK_MANAGMENT[acct][balance]}")
            elif tra==3:
                Depo_ampunt=int("Enter Deposite Amount :")
                BANK_MANAGMENT[acct][balance]+Depo_ampunt
                print(f"After Deposite your balance is {BANK_MANAGMENT[acct][balance]}")
            elif tra==4:           
                print("RESET PASSWORD :")
                find=input("Enter User NAme or Mo_No:")
                input("SEnd OTP pres Enter>>>>>>>>".upper())
                if input:
                    otp=random.randint(1000,9999)
                    print(otp)
                    status=True
                    while status:
                        User_Otp=int(input("Enter OTP :"))
                        if User_Otp==otp:
                            NEW_PASSWORD=input("Enter NEW PASSWORD :")
                            User_data[find][Pass_word]=NEW_PASSWORD
                            print("==========Password changed succesfully ===========")
                            break
                        else:
                            print("RE-ENTER...............")
                elif tra==5:
                    break
    else:
        print("invalid Re enter")

