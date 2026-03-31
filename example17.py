num = int(input("Enter number :"))

match num:
    case num if num > 0:
        printf("Number is positive")
    case num if num < 0:
        print("Nagative")

    case _:
        print("Zero")