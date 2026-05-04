l1=[]
even_list=[]
odd_list=[]

for i in range(1,6):
    num=int(input("Enter Number:"))
    l1.append(num)
    
l1.append("Hello")
print(l1)
for n in range(len(l1)):
    if type(l1[n])==str:
        continue
    elif l1[n]%2==0:
        even_list.append(l1[n])
    else:
        odd_list.append(l1[n])
   

print(odd_list)
print(even_list)