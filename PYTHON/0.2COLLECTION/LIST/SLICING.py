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


""""Ager slicing se append kiya to original list pe affect karega 
    wo jis index diye he uski value hatake(Remove karke) assing vali jitni bhi value he wo a jayegi"""
lst = [15 , 12 , 13 , 14 , 17 , 18 , 15]
lst[:2]=[22 , 25 , 27]
lst[2:5]
print(lst)

lst2 = [22 , 33 , 44 , 55 , 66 , 77 , 88]
lst2[1:1] =[1 , 2 , 3 , 4 , 5 , 6]
print(lst2)   #[22 , 1 , 2 , 3 , 4 , 5 , 6 , 33 , 44 , 55 , 66 , 77 , 88]

lst3 = [44 , 55 , 66 , 77 , 88 , 99 , 11 , 22 , 33]
lst3[3:6] =[]
print(lst3)      #[44 , 55 , 66 , 1 , 11 , 22 , 33]
"""iska matlab slicing di hui sari index ki value remove karke aisgn ki sari value aooend karega us index se"""