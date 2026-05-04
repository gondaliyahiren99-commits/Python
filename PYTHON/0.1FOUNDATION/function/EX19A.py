Account={
    'name':'hiren',
    'ac_no':'123456',
    'bal':2500,
    'ifsc':'BARB0MAHUVA',
    'Ac_open': False
}

def Ac_acess():
    Name=input("Enter Nmme :")
    Ac_No=input("ENter Ac NO :")
    if Name==Account['name'] and Ac_No==Account['ac_no']:
        Account['Ac_open']=True
        print("Welcome :")
    else:
        print("invalid")


def Check_Acess(open):
    def wrapper():
        if Account['Ac_open']==True:
            open()
        else:
            print("you Must Acess :")
    return wrapper

@Check_Acess
def CheckBal():
    print(f"your balance is  :{Account['bal']}")

@Check_Acess
def  DepoMoney():
    Amount=int(input(("Enter Deposite Amount :")))
    Account['bal']+=Amount


@Check_Acess
def WithdraMoney():
    Amount=int(input(("Enter Withdraw Amount :")))
    if Account['bal']>Amount:
        Account['bal']-=Amount
    else:
        print("amount Not ")

@Check_Acess
def Ac_Close():
    Account['Ac_open']=False

MENU=  """
    1 FOR AC ACESS
    2 FOR CHECK BALANCE
    3 FOR DEPOSITE MONEY
    4 FOR WITHDRAW MONEY
    5 FOR AC CLOSE
    6 FOR EXIT 
      """

status= True
while status:
    print(f"{Account['Ac_open']}")
    print(MENU)
    ch=int(input("Enter Choice :"))
    if ch==1:
        Ac_acess()
    elif ch==2:
        CheckBal()
    elif ch==3:
        DepoMoney()
    elif ch==4:
        WithdraMoney()
    elif ch==5:
        Ac_Close()
    elif ch==6:
        status=False
    else:
        print("Re-Enter Choice :")