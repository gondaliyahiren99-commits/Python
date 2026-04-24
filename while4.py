for i in range(6):
    for j in range(i):#i ka first 0 hoga and j ka bhi first 0 hoga to first vala nhi jaega ander 0=0 X
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
    
for i in range(1,6):
    for j in range(i):
        print(j+1,end="")
    print()
o=1
for i in range(1,6):
    for j in range(i):
        print(o,end="")
        o+=1
    print()