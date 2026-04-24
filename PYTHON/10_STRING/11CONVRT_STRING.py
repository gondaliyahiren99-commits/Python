s1 = "Py1T*Hon"
s2=""

for char in s1:
    if char.isupper():
        s2+=char.lower()

    elif char.islower():
        s2+=char.upper()
    else:
        s2+=char        


print("s1 :",s1)
print("s2 :",s2)