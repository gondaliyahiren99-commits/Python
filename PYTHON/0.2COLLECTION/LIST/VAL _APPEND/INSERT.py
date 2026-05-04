"""
add new element from user and store at specific index position


  list_name.insert(index,value)
"""

l1=[1,12,25,27,26]
print(l1)

l1.insert(1,1001)
print(l1)

print("========================================================================================================")

st_name=[]
for i in range(5):
    name=input("Enter name :")
   
    marks=int(input("Enter Marks:"))
    if marks>=90:
        result=f"pass student name is {name} with {marks} marks"
        st_name.insert(i,result)
print(st_name)
