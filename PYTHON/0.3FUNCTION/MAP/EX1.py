# #without map
l1 = [15 , 48 , 34 , 18 , 37 , 94 , 25 , 15 , 21]
l2 = []
for i in l1 :
        l2.append(i + 5)
print(l2)

#with map function
l3=list(map(lambda num: num+5,l1))
print(l3)

print("="*50)

# #with and without lambad map
l1 = [15 , 48 , 34 , 18 , 37 , 94 , 25 , 15 , 21]
l2 = []
def findecven(a) :
    if a%2 == 0 :
       return a
    
l2 = list(map(findecven ,l1))
print(l2)


# #with lambad
l1 = [25 , 24 , 18 , 76 , 54 , 23]
l2=list(map(lambda num:f"{num} even" if num%2==0 else f"{num} odd",l1))
print(l2)


