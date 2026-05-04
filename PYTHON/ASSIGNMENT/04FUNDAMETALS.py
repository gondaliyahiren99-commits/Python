"""


#Introduction to conditional statements: if, else, elif.
        in python if , if else and elif are decion making statement.
        They help to take decions based on condition.
        if condition is true block of code will execute.

        1) if statements:-
        The if statement is true the code inside if runs.
        if wali condition agar true hogi to andar ka code execute hoga.

                e.g.
                age = 25 
                if age>18 :
                    print("eligible")
                ~~~>outpt : eligible

        2) if...else statements :-
                when if condition is true so if block of code will execue but
                if condition become false its execute else part.
                e.g.
                age = 15 
                if age > 18 :
                    print("Eligible")
                else :
                    print("Not Eligible")
        ~~~>outpt : Not Eligible

        3)if.....elif statements :-
                when we have multipul condition to check we use elif statement.
                agar hamari pehli condition true hogi to vo baki conditoion check nahi karega
                e.g.
                age = 32
                if age < 13 and age >8 :
                    return "minor"
                elif age < 25 and age > 18 :
                    return "younger"
                elif age >25 :
                    return "oldage"

# Nested if-else conditions.
    when we have condition inside another condition.jab condition ke andar condion ban rahi ho rahi ho tab use hota he.
    iski jagana and opeater ka use ho sakta he but condition kaha pr False ho rahi he Uske output ke liye use karte he.
    

            is_male = True
            
            if age > 18 :
                if is is_male :
                    print("Eligible")
                else:
                    print("above 18 but not male")
            else: 
                print("not above 18 :")

"""
#====================================================================================================================================

#======================================================= Lab Exercise :  =============================================================
#============================================================(5)===================================================================
#Write a Python program to find greater and less than a number using
num = int(input("Enter Number :"))
if num > 85 :
    print(f"{num} is greter Than 85 and less 100")
elif num > 70 :
    print(f"{num} is grater than 70 and less than 85")
elif num > 50 :
    print(f"{num} is grater than 50 and less than 70")
elif num > 30 :
    print(f"{num} is grater than 30 and less than 50")
else :
    print("below 30")

#============================================================(6)===================================================================
# Write a Python program to check if a number is prime using if_else.
n = int(input("Enter Number to check prime or Not :"))
flag = 1
for i in range(2,n-1):
    if n % i == 0 :
        flag = 0 
    
if flag == 1 :
    print("prime Number")
else:
    print("Not")
#============================================================(7)===================================================================
# Write a Python program to calculate grades based on percentage using if-else ladder.
percentage = int(input("Enter marks :"))
if percentage > 90 :
    print("A")
elif percentage > 75 :
    print("B")
elif percentage > 55 :
    print("C")
elif percentage > 35 :
    print("D")
else :
    print("Fail")


#============================================================(8)===================================================================
# Write a Python program to check if a person is eligible to donate bloodusing a nested if.
age = int(input("Enter Age :"))
Weight = int(input("Enter Weight :"))

if age > 18 :
    if Weight >= 55 :
        print("Eligible To Donate : ")
    else: 
        print("Your weight is loose :")
else :
    print("Your age is not eligible :")