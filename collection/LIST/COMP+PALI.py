l1=["mom","word","level","madam","nayan"]

l2=[]

for i in l1:
    if i==i[::-1]:
        l2.append(f"{i} is palindrome")#with value
print(l2)

#============================================================================================================================

for word in l1:
    if word[::-1]==word:
        l2.append("palindrome")
    else:
        l2.append("Not palindrome")

print(l1)
print(l2)

#============================================================================================================================




