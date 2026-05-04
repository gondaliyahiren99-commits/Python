l1=["JAVA","PYTHOna",'c']
print(l1)

#without comprahantion

l2= []

for  name in l1:
    if len(name)>4:
        l2.append(name)
print(l2)
    

l3=[name for name in l1 if len(name)>4]
print(l3)

#================================================
#only if (leftside)
l4 = [i for i in range(1,11) if i%2==0]
print(l4)
