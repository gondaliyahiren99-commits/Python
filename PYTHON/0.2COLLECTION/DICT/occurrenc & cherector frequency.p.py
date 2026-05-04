                    #imp
d={}
name=input("enter your name :".upper())
for i in name:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)

#2 method
from collections import defaultdict

d=defaultdict(int)
print(d)#defaultdict(<class 'int'>, {})

list=["java",'python','php','python','c++','java','python']

for i in list:
    d[i]=d[i]+1

print(d)

#3 method
from collections import Counter

list=["java",'python','php','python','c++','java','python']

data=Counter(list)
print(data)