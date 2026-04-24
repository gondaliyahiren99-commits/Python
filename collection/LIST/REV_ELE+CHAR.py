l1=["python","java","php"]
l2=[]
for sub in l1[::-1]:
    l2.append(sub[::-1])

print(l2)


print("==========without sec. list clear================")
for i in l1[::-1]:
    l1.remove(i)
    l1.append(i[::-1])

print(l1)