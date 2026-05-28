"""
QUE  28: WRITE A FUNCTION THAT ACCEPTS A STRING AND REMOVES ALL DUPLICATE CHARACTERS FROM THE STRING.
"""
st = "Heloo my name is hiren  my".split()
new= ""
for i in st:
    for j in range(len(i)):
        if i[j] not in new :
            new+=i[j]
        else:
            continue
    new+=" "
print(new)