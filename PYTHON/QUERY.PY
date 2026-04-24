# #FID ALL INDEX OF F and append in list

# l1=[]
# name="abcfefsfaggdgvhhjjhdj"
# print(name.find("f",+6))
# ind=0
# for i in name:
#     ind=i.find("f",+ind)
# #     l1.append(ind)
    

# # print(l1)




# # print("=====================================")
# # [name1],[num1],[name2],[num2]
# # [name1,num2,name2,num1]


# # s1="Hiren age 24 and brother age is 30"

# # for i in range(len(s1)):
# #     if ord(s1[i])>=48 and ord(s1[i])<=57:
# #         print(s1[i],end="")
# #     elif ord(s1[i])>=58 and ord(s1[i])<=47:
# #         print(s1[i],end="")
# #     else:

# # name=[]
# # num=[]
# # l1=[]
# # l1.extend(("Hiren","python","java",1,2,14,18,))
# # print(l1)

# # l1.append("hello!")
# # print(l1)

# # l1.insert(2,"C")
# # print(l1)
# # for i in l1:
# #     if type(i)==str:
# #       name.append(i)
# #     else:
# #         num.append(i)
        
# # print(l1)
# # print(name)
# # print(num)

# # username=input("Enter UserName :")
# # Name,Surname=username.split(" ")
# # print(username)
# # print(Name)
# # if username.isalpha:
# #   print("YEs")
# # print(Surname)

# # num="7hjdbbjb"
# # flag=1
# # for i in range(len(num)):

# #   if num[i].isalpha:
# #     flag=0
# #     break
# #   else:
# #     print("NoT")
# # if flag==1:
# #   print("Valid")



# # #====================================================
# # s1="Hiren is 15243 and Ketan more than 45012 "
# # print(len(s1))
# # num=""
# # name=""
# # for var in range(len(s1)):
# #     if ord(s1[var])>=48 and ord(s1[var])<=57:
# #         num




# num=12
# name='hiren'
# name1='ramesh'
# num2=45

# #output=['hiren][ramesh][1245]
# print(f"{name}".split(),end=" ")
# print(f"{str(num)+ str(num2)}".split(" "),end="")
# print(f"{name1}".split(),end=" ")
# print("\n")

# name1="mohammed"
# name2="mustved"
# number1=12
# number2=23

# print(f"{name1.split()}",end="")
# print(f"{number1}{number2}".split(),end="")
# print(f"{name2.split()}")
# num=int(input("Enter Name :"))
# for i in range(2,num):
#     for j in range(2,num-1):
#         flag=1
#         if i%j==0:
#             flag=0
#             break
#     if flag!=0:
#         print(i)

# L2=[]
# L1=[15,25,14,18,75,94,85,35]

# for i in L1:
#     sum=0
#     while i>0:
#         r=i%10       
#         sum+=r
#         i//=10
#         print(i)
    
#     L2.append(sum)
# print(L2)


# li=[1,2,3,4,5,6,7]
# def sq(x):
#     return x*x


# sq_list=list(map(sq,li))
# print(sq_list)


# l2=list(map(lambda num : f"{num}=even" if num%2==0 else f"{num}=odd",li))
# print(l2)


# num=lambda x : f"{x} is positive " if x>0 else f"" 
# print(num(-34))


l1=["java","python","php","css"]

l2=[]
for i in range(len(l1)):
    for j in range(len(l1[i])):
       if l1.count(l1[i][j])>1:
            l1.pop(i.index(j))
print(l1)
      
print(l2)
# l1="i am hiren " 
# l2=[]
# for i in l1:
#     if i== " ":
#         continue
#     if i not in l2:
#         l2.extend([i,l1.count(i)])
# ['i', 2, 'a', 1, 'm', 1, 'h', 1, 'r', 1, 'e', 1, 'n', 1]
# print(l2)


