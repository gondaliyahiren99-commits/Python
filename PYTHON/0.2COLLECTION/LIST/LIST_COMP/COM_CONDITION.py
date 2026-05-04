"""
with condition
when olly one condition: 

l1=[ value(left)  loop(center)     condition]
"""


l1=[]
for i in range(1,6):
    if i%2==0:
        l1.append(i)

print(l1)

#with compreheton

l1=[ i for i in range(1,6) if i%2==0]

print(l1)


l2=[i for i in range(1,6) if i<3]
print(l2)


#====================================================================
# find even or odd number

l1=[]

#without list comprehension

for i in range(1,11):
    if i%2==0:
        l1.append("even")
    else:
        l1.append("odd")

print(l1)

# with list comprehension
l2=["even" if i%2==0 else "odd" for i in range(1,11)]
print(l2)

#save like tuple or list

l3=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,11)]
print(l3)
print(l3[0][0])
print(l3[1][1])


l4=[[i,"even"] if i%2==0 else [i,"odd"] for i in range(1,11)]
print(l4)
print(l4[0][0])
print(l4[0][1])