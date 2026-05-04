# l1=[15,25,41,78,35,12,42,18,19,76]
# def sum_val(num):
#     sum=0
#     while num>0:
#         r=num%10
#         sum+=int(r)
#         num/=10
#     return sum
  
# l2=list(map(sum_val,l1))
# print(l2)

l2=[15,24,75,41,21,31,14,4,21,28]
def sort_val(num):
    for i in range(len(l2)):
        if l2[i+1]<=num:
            return  (l2.insert(i+1,num) ,l2.insert(l2.index(num),l2[i]))
    

l3=list(filter(sort_val,l2))
print(l3)

