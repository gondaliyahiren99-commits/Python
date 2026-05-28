
class InsufficientBalance(Exception):
    pass

def ATM(balance,with_amt) :
    if with_amt > balance :
        raise InsufficientBalance("insufficient balance :")
    else :
        print("succefully")

balance = 5000
withdraw =int(input("Enter amount"))

try :
    ATM(balance,withdraw)
except InsufficientBalance as e  :
    print(e)