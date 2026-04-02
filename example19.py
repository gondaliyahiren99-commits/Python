for i in range(1,6):
    print("hello",end =" ")


print()

for i in range(1,6):
    print(f"({i}) hello")


print()

for i in range(5,0,-1):
    print(f"({i}) hello")

#chech prime number
n=int(input("Emter n :"))
count=0
for i in range(1,):
    if n%i == 0:
        count=count+1

if count>2:
    print("primt")
else:
    print("Not prime")