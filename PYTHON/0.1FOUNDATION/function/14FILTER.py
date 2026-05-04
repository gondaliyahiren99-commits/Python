"""
filter() : filter fun return only thse ele from an iterartion fulfill spacific conditiion



mpa : fun aply on each ele and perform opration and return each element but 

filter(fun,ite)


l1=[1,2,3,4,5,6,7]
l2=list(filter(lambda num : num%2==0  , l1))
print(l2)2,4,6
agar condition he to filter number return karta he jabki map true or false return karta he
"""


l1=[12,24,25,15,18]

def findEven(num):
    if num%2==0:
        return "Even"
l2=list(map(findEven,l1))
print(l2)


# l3=[12,24,25,15,18]

# def findEven(num):
#     if num%2==0:
#         return "Even"
# l4=list(filter(findEven,l3))
# print(l3)
# print(l4)