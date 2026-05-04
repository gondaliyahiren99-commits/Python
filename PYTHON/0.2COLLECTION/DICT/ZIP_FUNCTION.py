"""
zip() is used to continue multiple list into single entity
"""

# l1=["dabeli","vadapav","bhel"]
# l2=[30,35,60]

# l3=list(zip(l1,l2))
# print(l3)
# d={}

# l1=["dabeli","vadapav","bhel","ragda"]#ererr nahi dega just pair vala zip hoga
# l2=[30,35,60]
# l3=list(zip(l1,l2))
# print(l3)

l1=["dabeli","vadapav","bhel"]
l2=[30,35,60]
for i in l2:
    if i>35:
        l3=(list(zip(l1,l2)))
print(l3)


"""

          dict me unzip nahi hoga : kyunki dictniory me key or value store hota he Not only key or Not only value allowed

"""
# l1=['name','age','course']
# l2=['hiren','25','python']
# l3=dict(zip(l1,l2))
# print(l3)