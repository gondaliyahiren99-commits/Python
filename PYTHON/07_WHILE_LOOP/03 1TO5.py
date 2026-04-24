# status = True

# while status:
#     num = int(input("ENter number :"))

#     if num<0:
#         status = false





s=True
i=0
while i<=5:
    j,k,p=0,5,1
    while k>=i:
        print(" ",end="")
        k-=1
    while j<=i:
        print("*",end="")
        j+=1
    while p<=i:
        print("*",end="")
        p+=1
    print()
    i+=1
i=4
while i>=0:
    j,k,p=5,0,1
    while j>=i:
        print(" ",end="")
        j-=1
    while k<=i:
        print("*",end="")
        k+=1
    while p<=i:
        print("*",end="")
        p+=1
    print()
    i-=1