"""                                         :::generator:::
generator is a spacial function which is generate some state of value and store in a one place and return
as per the requirement

normal function perform any operation and return value but generator dose not return it just store value 
and save state and return using (yield) keyword
"""

def myfun():
    return 1
    return 2
    return 3
# return hamesha pehli value return karega aur remain ko chhod dega
print(myfun())#1
print(myfun())#1
print("="*100)
def mygenerator():
    yield 1
    yield 2
    yield 3
obj=mygenerator()
print(next(obj))#1
print(next(obj))#2
print(next(obj))#3
print(next(mygenerator())) #1 (every time start se start hoga)
print(next(mygenerator())) #1
print(next(mygenerator())) #1
#print(next(obj))# 4 nhi hai to erorr aye gi



def fun(l) :
    for i in range(len(l)) :
        yield l[i]
l1 = [15,24,87,24,36]
r = fun(l1)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
