# blank set
s={}
print(s)
print(type(set(s)))

#_____________________________________

# remove dublecate valuse
l1=[1,2,3,4,5,1,2,3,6,37,7,4,3,2,8,9,6,5,3,2,54,32,5,55,765,43,2]
# without set datatype
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)

#using set

l3=list(set(l1))
print(l3)