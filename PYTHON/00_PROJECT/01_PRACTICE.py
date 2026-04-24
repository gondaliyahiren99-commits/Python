balance = 40000
password= "123456"
email="admin@gmial.com"
Name="hiren"
Acount_Number="123456789"
Bank_name="Bank Of Baroda"
trans_id="12456"

status = True
while status:
    Menu =                  """
            1.show balance your account
            2.deposite amount
            3.Withdraw amonut
            4.Exit
                        """
    print(Menu)
    choice = int(input("Enter choice :"))
    match choice:
        case 1:
            print(balance)
        case 2:
            amount= int(input("Deposite ammoount :"))
            balance+=amount
            print(balance)
        case 3:
            
            user_password= input("Enter your password:")
            user_emial= input("Enter your email")
            if user_emial==email:
                if user_password==password:
                    amount =int(input("Enter withdraw Amount :"))
                    if balance>amount:
                        balance-=amount
                    else:
                        print("Insufficient")
                else:
                    print("password wrong")
            else:
                print("your email wrong")

            print("Yuor Remainng bal:",balance)
                        

        case 4:
            print("your transaction is complate :")
            status=False
        case _:
            print("your transction is complate :" )
            
    print("Do you want to continue !: if yes press y or Y:")
    return_menu=input("Enter if you continue fro menu :")
    if return_menu =="y" or "Y":
        status =True 


    print("do you want receipt :")
    print("Bank Holder NAme: ",Name)
    print("Account Number:",Acount_Number)
    print("transaction id :",trans_id)
    print(balance)
 
