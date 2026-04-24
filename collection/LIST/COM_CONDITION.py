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