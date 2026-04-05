#accept five number from user and checck pos or nag
for i in range(1,6):
    num = int(input(f"Enter {i} number :"))
    if num>0:
        print(f"{num} is posistive=")
    else:
        print(f"{num} is nagative ")