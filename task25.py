pos=0
nag=0
for i in range(1,6):
    num = int(input("Enter number "))
    if num>0:
        print("positive")
        pos=pos+1
    else:
        print("nagative")
        nag= nag+1

print("total positive number =",pos)
print("total nagative number=",nag)