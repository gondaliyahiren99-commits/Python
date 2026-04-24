name="hiren"
print("1st Method :",name[::-1])


#==================================================
rev=""
s=len(name)
for i in range(1,s+1):
    rev+=name[s-i]

print("2nd Method:" ,rev)


#===================================================
reverse=""
surname="Gondaliya"
for i in range(len(surname)):
    reverse=surname[i]+reverse
print("3rd Method",reverse)
#========================================================



rev=""
for i in surname:
    rev=i+rev
    
print(rev)


#reverse string ke liye nahi hota just for list