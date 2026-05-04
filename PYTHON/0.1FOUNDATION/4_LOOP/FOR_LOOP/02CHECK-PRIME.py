
result=False
for i in range(5,0,-1):
    print(f"({i}) hello")

#chech prime number
n=int(input("Emter n :"))
count=0
for i in range(2,n):
    if n%i == 0:
        result=True
        
if result==True:
    print("prime")
else:
    print("Not prime")

