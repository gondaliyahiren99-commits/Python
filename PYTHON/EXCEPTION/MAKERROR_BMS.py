"""
all exception derived from the  Exception class 
in pyiuthon there is inbuilt class which nae in Exceptopm
"""
# class AgeException(Exception) :
#     pass

# age = int(input("Enter age"))
# if age <18 :
#     print("invalid :")
#     raise AgeException("You Are  MInor")
# else:
#     print("Eli")


balance =2000
class BalanceError(Exception) :
    pass
def balanceCheck(bal) :
    print(bal)

def Deposit(bal):
    amount=int(input("Enter Deposite Amout :"))
    if amount<0 :
        raise BalanceError("Not Valid Amount :")
    else :
        bal +=amount
        return bal
def withdraw(bal) :
    amount= int(input("Ener Deposite Amount :"))
    if amount < bal :
        bal1-=amount
        return bal
    else :
        raise BalanceError("Insufficient Balance.........!")

Menu = """
                1 for check balance
                2 for deposite
                3 for withdraw
                4  exit
    """
status= True
while status :
    print(Menu)
    ch = int(input("Ener Choice :"))
    if ch==1 :
        balanceCheck(balance)
    elif ch==2 :
        balance=Deposit(balance)
        print(balance)
    elif ch==3 :
        withdraw(balance)
        print(balance)
    elif ch>=5 and ch<=0 :
        print("Re-Enter : ")
    else :
        status =False