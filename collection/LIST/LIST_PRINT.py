

li=[12,31,4,2,"java",-42,-1,True,65.231,3.123,"python",23]

print("============================================================")

for i in range(len(li)):
    print(li[i],end="")


print("==================================")

for i in li:
    print(i,end=" ")





l1 =['python','java',90,34,True,89.35]
name=""
num=""
print(l1)
for element in l1:
    if element.isdigit:
        num+=element
    else:
        name+=element

print(num)
print(name)