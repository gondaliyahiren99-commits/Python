"""
inbuilt function and method
"""
l1=[54,35,21,55,55,2,21,211,2112,255]
print(l1)
for i in range(len(l1)):
    print(f"{i} index : {l1[i]}")
print(f"length of list{len(l1)-1}")

print(f"max : {max(l1)}")
print(f"min : {min(l1)}")
print(f"sum : {sum(l1)}")

l1.reverse()
print(l1)

l1.sort()   #ascending order
print(l1)

print(l1)
l1.sort(reverse=True) #Descending order