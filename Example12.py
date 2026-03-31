marks = int(input("Enter marks"))

if marks>=0 and marks<=100:
    if marks>60:
        print("A")
    elif marks>50:
        print("B")
    elif marks>40:
        print("C")
    elif marks>30:
        print("fail")
else:
    print("invalid")
    