import numpy as ny
ans=ny.array([1,2,3,4,5])
print(ans)
#-------------------- adding 5 number
l1=[1,2,3,4,5]
l2=[i+5 for i in l1]
print(f"{l1}\n{l2}")

import numpy as ny

num=ny.array([1,2,3,4,5])
num=num+5
print(num)

# -------------------
arry=ny.zeros((2,3))
print(arry)
arry=ny.ones((3,3))
print(arry)
arry[0][1]=5
print(arry)