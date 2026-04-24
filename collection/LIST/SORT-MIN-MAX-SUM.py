l1=[15,26,24,31,84,75,79,84,6,43,41,24]
for element in l1:
    print(element)
print(len(l1))

l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

print(min(l1))
print(max(l1))
print(sum(l1))

"""
#{max,min,sum =tabhi hoga jun listme khali numbers honge agar string huva to nhi hoga.}

"""

li=[22,93,84,"java",3,132,-103,61,True,34,14,"python",32,5,65,1,0,2,7]
print(li)
li.reverse()
print(li)

li=[22,93,84,3,132,-1000,434,53,62,3,34,61,True,34,14,23,32,5,65,1,0,2,7]
print(li)

li.sort()#ascending order me kare ga but agar string hui to erorr hogi

print(li)

li.sort(reverse=True)# descending orde sem no string 
print(li)
li=[22,93,84,3,132,-1000,434,53,62,3,34,61,True,34,14,23,32,5,65,1,0,2,7]
#method
print("count 3 kitni bar hai =",li.count(3))
print("find 3 ka index =",li.index(3,+4))