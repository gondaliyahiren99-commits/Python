menu = """

MENU 

press 1: play game 
press 2: pause game
press 3: exit game

"""
print(menu)

choice = int(input("Enter your choice"))

match choice:
    case 1:
        print("Welcome")
    case 2:
        print("pause game")
    case 3:
        print("Thank you")
    case _:
        print("invalid")