"""
reduse function is a similer like map and filter
which is preform spacific operation of each iterator and provide collection result
"""
from functools import reduce
l1=[1,2,3,4,5]
obj=reduce(lambda num1,num2: num1+num2,l1)# sume ki tra hi kam karta hai 1 or 2  plus karega =3 
print(obj)# fir fir 3+3=6+4=10+5 dictionary me kam ayega list me to sum ka hi use hoga
# han agar multiplication karna ho tab iska use kar sakte hai 
obj=reduce(lambda num1,num2:num1*num2,l1)
print(obj)#1*2=2*3=6*4=24+5=120