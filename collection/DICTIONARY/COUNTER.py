from collection import defautdict
d=defautdict(int)
print(d)

list=["java","python","android","java","python"]

for word in list:
    d[word]=d[word]+1

print(d)


#=======================================================================

from collections import Counter


list=["java","python","android","java","python"]

data=Counter(list)

print(data)
