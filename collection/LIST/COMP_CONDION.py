l1=["JAVA","PYTHOna",'c']
print(l1)

#without comprahantion

l2= []

for  name in l1:
    if len(name)>4:
        l2.append(name)
    

l2=[name for name in l1 if len(name)>4]
print(l2)