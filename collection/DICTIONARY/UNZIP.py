"""unzip= is a opposite procees to zip function

zip which is used to merge or continue multiple list into.
single object

unaip which is used to split zipped object into seprate variable

there is no such keyword like unaip

"""

l1=["dabel","Vada"]
l2=[2,3]
record=list(zip(l1,l2))

print(record)

item,price=zip(*record)
print(item)
print(price)