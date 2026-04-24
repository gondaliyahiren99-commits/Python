"""
 to add new element in exisiying list but at this time we want to add multiple element

    var_name.ectend( [v1,v2......] )

    """
# """
# l1=[10,20,30,40]

# print(l1)
# i=0
# while i<len(l1):
#     if l1[i]%2==0:
#         print("index {} of number {} is even :".format(i,l1[i]))
#     else:
#         print("index {} of number {} is odd :".format(i,l1[i]))
#     i+=1
# l1.extend([50,70,80]) #add multiple valu at same time
# print(l1)


# t1=(1,2,3,4,5,6,8,9,3,9,3,4,3,11,12)
# print(len(t1))
# print(t1[0])
# i=0

# print(t1.count(3))

# print(t1.count(4))
# while i<len(t1):
#     if t1[i]%2==0:
#         print("index is {} ={} is even".format(i,t1[i]))
   
#     else:
#         print(f"{i} ={t1[i]} is not even ")
#     i+=1

#acess first and last element
l1=["k",15,"Hiren",5,"vishal",True,"Hello",45,"55"]
# print(l1)
# middle=len(l1)//2
# print(l1[0],l1[-1],l1[len(l1)-1])
# print(l1[len(l1)//2])


l1.extend(["hiren",45,False,"Namste"])

print(l1)

l2=[45]
if not l2:
    print("Empty")
else:
    print("not Empty")

print(l2)