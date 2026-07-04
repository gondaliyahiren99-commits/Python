s1={1,"JIo",3.14,False,"Army"}
s2= s1.copy()
print(s2)

s2.add(5)
print(s2)


# Agar .copy() Nahi kiya To Ye Jab 5 Ko s2 Me Add Karenge To Wo s1 Me Bhi Add hoga
s1={1,"JIo",3.14,False,"Army"}
s3=s1
s3.add(5)
print(s1)  # {False, 1, 3.14, 5, 'Army', 'JIo'}
print(s3)   # {False, 1, 3.14, 5, 'Army', 'JIo'}