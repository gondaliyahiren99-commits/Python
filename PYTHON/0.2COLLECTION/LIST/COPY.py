l1=[1,2,3,4,5,6]
print(l1)
l2=l1

print(l2)
l2.remove(5)
print(l1)
print(l2)


s1=[1,2,3,4,5,6]
s2=s1[::]
s2.remove(1)
print(s1)
print(s2)

"""
agar copy() use nahi karenge to l2 me remove or append karenge to l1 me bhi affected hoga

ya fir 

l2=l1[::]  ka use karo isse pehli list pr asar nahi hoga

"""