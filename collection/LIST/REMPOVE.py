"""
remove use to list of vlaue directky reemove(value)

var.remove(value)

"""
l1=["java","python","c","php"]
print(l1)
l1.remove("java")
print(l1)

#we want remove list of last element therefor use a pop()
#that automatically take list of last index 
l1.pop()
print(l1)

#if we want remove by index so useful pop(index)
l1.pop(0)
print(l1)


# puri listtruncate ho jayegi but variable exsist 
l1.clear()
print(l1)


#jabki del me var ke sath puri list hi delete ho jayegi
del l1
print(l1)