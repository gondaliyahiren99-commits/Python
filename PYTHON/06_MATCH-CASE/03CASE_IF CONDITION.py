# num = int(input("Enter number :"))

# match num:
#     case num if num > 0:
#         printf("Number is positive")
#     case num if num < 0:
#         print("Nagative")
#     case _:
#         print("Zero")



print("============================================================")
num=int(input("Enter Number :"))
match num:
    case num if  num%2==0 and num>0:
        print("Even and positive")
    case num if num%2==0 and num<0:
        print("Even or Nagative")
    case num if num%2!=0 and num<0:
        print("odd or Nagative")    
    case num if num%2!=0 and num>0:
        print("odd or positive")
    case _:
        print("Zero")