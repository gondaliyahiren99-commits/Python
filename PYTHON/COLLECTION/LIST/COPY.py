l1=[10,2,3,40,50,30]
l2=l1
print(l1)
print(l2)


#without copy fun use affected both list
l2.remove(40)
print(l1)
print(l2)


l2.append(800)
print(l1)
print(l2)


# not affected
l2=l1.copy()
print(l1)
print(l2)


#without copy fun use affected both list
l2.remove(40)
print(l1)
print(l2)


l2.append(800)
print(l1)
print(l2)