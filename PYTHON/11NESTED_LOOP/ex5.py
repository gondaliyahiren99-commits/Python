# n=int(input("Enter n :"))
for row in range(1,6):
    for space in range(6-row):
        print(" ",end =" ")
    for col in range(row,0,-1):
        print(col,end=" ")
    print()

