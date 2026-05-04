from numpy import square
from numpy._core.defchararray import upper
l1=["java",'python','php','android','flutter']
def myfun(name):
    return name.upper()

l2=list(map(myfun,l1))
print(f"{l1}\n{l2}")

#with lambda
l3=list(map(lambda n: n.title(),l1))
print(l3)


#               OR

#jab hume inbulit fumction hii use karna hota to hum direct use without lambda fun ka karenge
#but must write as a iter str 
l4=list(map(str.upper,l1))
print(f"l4 :{l4}")#                  



