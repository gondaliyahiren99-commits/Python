for i in range(1,5):
    number = int(input(f"Enter number {i}"))
    if number%2==0:
       result = "Even :"
    elif number%2!=0:
        result = "odd :"
    else:
        result="Zero :"
print(result)

