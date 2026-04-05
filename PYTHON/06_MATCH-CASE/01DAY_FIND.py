day = int(input("Enter day :"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wedday")
    case 4:
        print("Thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid")