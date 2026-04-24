"""
slicing : piece of element

"""

l1=["java","python","android","php","flutter"]

print(f"fetch first 3 element :{l1[0 :3]}")#"java","python","android"
print(f"fetch first 3 element :{l1[ :3]}")# sby default start index 0 hi lega=["java","python","android"]
print(f"fetch last 2 element :{l1[-3:-1]}")#"php","flutter"
print(f"fetch first 3 element :{l1[0:-1]}")#"java","python","android","php","flutter"
print(f"fetch first 3 element :{l1[-1::-1]}")#"flutter","php"
print(l1[0:-3])
print(l1[0][::-1])#(reverse)