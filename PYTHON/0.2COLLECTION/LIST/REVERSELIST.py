l1=["Java","python","php","Mern"]
print(l1)
for i in l1[::-1]:
    l1.remove(i)
    l1.append(i[::-1])

print(l1)