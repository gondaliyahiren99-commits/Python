"""
accept name from user and check character fre
"""
d={}

name=input('Enter name :')

for char in name:
    if char in d.keys():
        d[char]=d[char]+1
    else:
        d[char]=1

print(d)