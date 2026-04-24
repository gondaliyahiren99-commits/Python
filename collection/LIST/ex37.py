# s1={1,2,5}
# s2={3,2,4}


# #union
# print(s1 | s2)

# #intersection
# print(s1&s2)

# #diff
# print(s1-s2)

# print(s2-s1)


# from random import random
# l1=[15,"hiren",True,"ramesh",25,False]
# print(l1.index('hiren'))
# l1_alpha=[]
# l1_bool=[]
# l1_num=[]
# for i,v in enumerate(l1):
#      if type(v)==int:
#         l1_num.append(i)
#      elif type(v)==bool:
#         l1_bool.append(i)
#      elif type(v)==str:
#         l1_alpha.append(i)
#      else:
#         pass

  
# print(l1_alpha)#[1,3]
# print(l1_num)#[0,4]
# print(l1_bool)#[2,5]


l1=[15,'hiren',-31,False]
Num=[]
name=[]
bo_ol=[]
for i in l1:
   if type(i)==int:
      Num.append(i)
   elif type(i)==bool:
      bo_ol.append(i)
   else:
      name.append(i)
print(l1)
print(Num)
print(name)
print(bo_ol)



#no output clear
l1=[]
for i in range(5):
   val=input("Enter Val :")
   if val.isalpha():
      l1.append(val)
   elif val.isnumeric():
      val=int(val)
      l1.append(val)
   else:
      val=bool(val)
      l1.append(val)
print(l1)