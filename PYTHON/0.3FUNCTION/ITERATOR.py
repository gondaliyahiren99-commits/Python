'''
itrator is an object which is though iterate each eliment one by one
list,tuple,dictionary all are iterator
'''

l1=[10,20,30,40,50]
obj=iter(l1)
print(next(obj))#10
print(next(obj))#20
print(next(obj))#30