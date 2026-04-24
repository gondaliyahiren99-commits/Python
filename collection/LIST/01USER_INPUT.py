# use by append()
# l1=[]
# for i in range(6):
#     num=int(input("Enter Number :"))
#     l1.append(num)
# print(l1)


#by onsert
l2=[]
# for i in range(5):
#     n=int(input("Enter N :"))
#     l2.insert(i,n)
# print(l2)


for i in range(5):
    n=int(input("Enter Number :"))
    l2.extend([n])
print(l2)