menu="""

    ----------Menu---------
    choice Your level:
    1.Normal level
    2.Medium Level
    3.Hard Level

"""
import random

print("********************NUMER GUESSING GAME *************************")

#genrate number betwen 1 to 100
print(menu)

choice=int(input("Enter choice:"))
match choice:
    case 1:
        print("Welcome to normal Level")
        computer1 = random.randint(1,10)
        
        attempt=3
        status= True
        print("your attempt :",attempt)
        while status:
            user_number=int(input("Guess Number beetwen 1 to 10 ="))

            if user_number>computer1:
                print("Enter lower Number......!")
            elif user_number<computer1:
                print("Enter upper Number......!")
            elif user_number==computer1:
                print("Right")
                print("***********congratulation******************")
                status= False
            else:
                print("enter valid number")
            attempt-=1
            print("Remaining Attempt :",attempt)
            if attempt==0:
                print("===================Better luck Next time================")
                break

    case 2:
        print("Welcome to mid level")
        computer1 = random.randint(1,50)
        
        attempt=5
        status= True
        print("your attempt :",attempt)
        while status:
            user_number=int(input("Guess Number beetwen 1 to 50  ="))
            if user_number>computer1:
                print("Enter lower Number......!")
            elif user_number<computer1:
                print("Enter upper Number......!")
            elif user_number==computer1:
                print("Right")
                print("***********congratulation******************")
                status= False
            else:
                print("enter valid number")
            print(computer1)
            attempt-=1
            print("Remaining Attempt :",attempt)
            if attempt==0:
                print("===================Better luck Next time================")
                break
          
    case 3:
        print("Welcome to Hard level")
        computer1 = random.randint(1,100)
        
        attempt=10
        status= True
        print("your attempt :",attempt)
        while status:
            user_number=int(input("Guess Number beetwen 1 to 100 ="))
            if user_number>computer1:
                print("Enter lower Number......!")
            elif user_number<computer1:
                print("Enter upper Number......!")
            elif user_number==computer1:
                print("Right")
                print("***********congratulation******************")
                status= False
            else:
                print("enter valid number")
                
            print(computer1)
            attempt-=1
            print("Remaining Attempt :",attempt)
            if attempt==0:
                print("===================Better luck Next time================")
                break
            status= False

    case _:
        print("invalid choice")