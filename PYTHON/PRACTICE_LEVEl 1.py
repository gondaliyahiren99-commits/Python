# #(1)Find factorial
# def facto_rial(num):
#     n=1
#     for i in range(1,num+1):
#         n*=i
#     return n
# num=int(input("Enter Number :"))
# print(facto_rial(num))

# #(2)check strig is palindrome 
# def palin_drome(str):
#     if str==str[::-1]:
#         return f"{str} is palindrome"
#     else:
#         return f"{str} is Not Palindrome"
# str=input("Enter string :")    
# print(palin_drome(str))

# #(3)sum of evev Number
# l1=[12,45,78,54,21,34,51,23,26]
# def Even_odd(num):
#     sum=0
#     for i in num:
#         if i%2==0:
#             sum+=i
#     return sum
   
# print(Even_odd(l1))

# #(4)find max number from list
# l2=[15,24,87,9,24,51,36,27,84,21,51,34,97,23,48]
# def Max_Find(num):
#     Max_Num=0
#     for i in num:
#         if i>Max_Num:
#             Max_Num=i
#     return Max_Num
# a=Max_Find(l2)
# print(a)

# #(5)Check prime Number
# def PrimeCheck(num):
#     flag=1
#     for i in range(2,num):
#         if num%i==0:
#             flag=0
#             break

#     if flag==1:
#         return "prime"
#     else:
#         return "Not prime"

# n=int(input("Enter Number :"))
# print(PrimeCheck(n))

# #(6)string in character count
# def StrCount(str,ch):
#      count=0
#      for i in range(len(str)):
#         if str[i]==ch:
#             count+=1
#      return count

# str=input("Enter Str :")
# ch=input("Enter ch :")
# print(StrCount(str,ch))
# l1=["hiren","mustved","jenish","Nisarg","Mahesh","dhrumil"]
# l2=[]
# def RevStr(str):
#     for i in str:
#       l2.append(i[::-1]) 
#     return l2
# RevStr(l1)
# print(l2)


# #(7)
# #(8)average of number 
# num_list=[15,24,87,9,24,51,36,27,84,21,51,34,97,23,48]
# def Avg(li):
#     sum=0
#     for i in li:
#         sum+=i
#     avg=int(sum/len(num_list))
#     return avg

# print(Avg(num_list))


# #(9)
# l2=[]
# def exp(li):
#     for i in li:
#         i+=10
#         l2.append(i)
#     return l2
# print(exp(num_list))


# s1=input("enter string :")
# if len(s1)>5:
#     print(s1.upper())
# else:
#     print(s1.lower())

# #(10)
# num=[15,14,12,17,18,21,25,26,27,51]
# DivByThree=[]
# def DivOfThree(li):
#     for i in li:
#         if i%3==0:
#             DivByThree.append(i)
#     return DivByThree
# print(DivOfThree(num))


# #(11)
# n=[5,4,2,1,8,9,7,3]
# Sq=[]
# def SquareOfN(num):
#     for i in num:
#         Sq.append(i*i)  
#     return Sq  
# print(SquareOfN(n))


# #(12)
# st=input("Enter Name :")
# count=0
# for i in st:
#     if i=='a' or i=='e' or i=='i' or i=='u' or i=='o':
#         count+=1
# print(count)


# #(13)
# def tab(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")
    
# num=int(input("Enter Number ;"))
# tab(num)


# #(14)
# lis=['python','java','DatAnaalyst','flutter','php','DataScince']
# def longString(l1):
#     max_len=lis[0]
#     for i in l1:
#         if len(i)>len(max_len):
#             max_len=i
#     return max_len
# print(longString(lis))


# #(15)
# def CheckArmst(num):
#     sum=0
#     while num>0:
#         r=num%10
#         sum+=r*r*r
#         num=int(num/10)
#     if sum==n:
#         return "Armstron"
#     else:
#         return "not"

# n=int(input("Enter n ;"))
# res=CheckArmst(n)
# print(res)


#(16)
# def DigiSum(n):
#     sum=0
#     while n>0:
#         r=n%10
#         sum+=r
#         n=int(n/10)
#     print(sum)

# num=int(input("Enter Number :"))
# DigiSum(num)

#(17)
# def Con_Up_low(s):
#     add=""
#     for i in range(len(s)):
#         if i%2==0:
#             add+=s[i].upper()
#         else:
#             add+=s[i].lower()
#     print(add)
# s1=input("Enter string:")
# Con_Up_low(s1)


#(18)
# li_st=[1,52,45,45,62,14,28,97,54,6,21,87,54,43]
# def FindSecLarge(l1):
#     large=1
#     SecLarge=0
#     for i in li_st:
#         if i>large:
#             SecLarge=large
#             large=i
#         if i>SecLarge and i<large:
#             SecLarge=i
#     print(large)
#     print(SecLarge)
# FindSecLarge(li_st)


#(19)
# i_st=[5,4,5,7,4,]
# product=[]
# def pro(li):
#     res=1
#     for i in li:
#         res*=i
#     print(res)
# pro(i_st)

#(20)
# l=['python','java','DatAnaalyst','flutter','php','DataScince']
# l2=[]
# def findeven(l1):
#     for i in l1:
#         if len(i)%2!=0:
#             l2.append(i)
#     return l2
# print(findeven(l))


#(21)
#(22)
#(23)
# l1_list=[1,52,45,45,62,14,28,97,54,6,21,87,54,43]
# l1_list.sort(reverse=True)
# print(l1_list)

#(24)
# l3=[24,51,32,24,19,43,27,13,51,26,27,82,39]
# primeNumber=[]
# def FindPrime(l3):
    
#     for i in l3:
#         flag=1
#         for j in range(2,i):
#             if i%j==0:
#                 flag=0
#                 break
#     if flag==1:
#         primeNumber.append(i)
#         return primeNumber
# print(FindPrime(l3))

#(25)
# l1=[25,-32,75,21,-45,12,-42,-87,92]
# l2=[]
# def FIndNag(lst):
#     for i in lst:
#         if i<0:
#             l2.append(i)
#     return l2

# print(FIndNag(l1))


#(26)
# l1=['hello','world','python','is ','high','level','progrmainng','language']
# def FindWord(li):
#     word=0
#     for i in li:
#         word+=1

#     return word
# print(FindWord(l1))


# (27)
#(28)
# (29)
# Num_list=[5,12,4,1,21,29,17,5,15,4,21]
# def SumofNum(l1):
#     sum=0
#     for num in l1:
#         if num>10:
#             sum+=num
#     return sum
# print(SumofNum(Num_list))

#(30)
# s1=['python','is','language','python','high','level','progrmainng','language']
# s2=[]
# def LenOfStr(s):
#     for i in s:
#         s2.append(len(i))
#     return s2
# print(LenOfStr(s1))

#(31)

#(32)
# l1=['python','is','language','python','high','level','progrmainng','language']
# l2=[]
# def CapOfStr(li):
#     for s in li:
#         s=s.capitalize()
#         l2.append(s)
#     return l2
# print(CapOfStr(l1))

#(33)
# Num_list=[5,12,4,24,21,42,17,18,15,4,21]
# New_li=[]   
# def FindDiv(l1):
#     for num in l1:
#         if num%2==0 and num%3==0 :
#             New_li.append(num)
    
# FindDiv(Num_list)
# print(New_li)


#(34)
# def CheckValid(s1):
#     if  '.' in s1 and '@' in s1:
#         print("valid :")
#     else:
#         print("Not Valid :")
# email=input("Enter email :")
# CheckValid(email)

#(35)
# Num_list=[5,12,4,24,21,42,17,18,15,4,21]
# def CountEven(l1):
#     count=0
#     for num in l1:
#         if num%2==0:
#             count+=1
#     print(count)
# CountEven(Num_list)

#(36)
# def CheckNum(s1):
#     if s1.isnumeric():
#         print(f"{s1} is numeric string")
#     else:
#         print("Not Numeric:")
# s=input("Emter s :")
# CheckNum(s)


#(37)
# d={}
# def fun(s1):
#     v=len(s1)
#     d[s1]=v
#     print(d)
# s=input("Ener Any string :")
# fun(s)


#(38)
# l1=[15,-29,-21,14,12,-21,18,-19,-20]
# l2=[]
# def FindNagSq(li):
#     for i in li:
#         if i>0:
#             l2.append(i*i)
#     print(l2)
# FindNagSq(l1)


#(39)
# l1=['python','is','prograning','language','and','hihg','level','language']
# l2=[]
# def StWithlen(st):
#     for i in range(len(st)):
#         l=len(st[i])
#         res=f"{st[i]}={l}"
#         l2.append(res)
#     return l2
# print(StWithlen(l1))


#(40)
# def ChkPerfect(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
    
#     if sum==n:
#         return n
         
                
# num=int(input("Enter Number :"))
# print(ChkPerfect(num))

#(41)
# def WithoutWowel(st): 
#     new_st=""
#     for i in st:
#         if i!='a' and i!='e' and i!='i' and i!='o' and i!='u' and  i!='A' and i!='E' and i!='I' and i!='O' and i!='U' :
#             new_st+=i
#     return new_st
# print(WithoutWowel("hiren"))


#(42)
# l1=[15,24,17,81,35,64,24,18,91]
# l2=[]
# def DivOfTwo(lst):
#     for i in  lst :
#         l2.append(int(i/2))
#     return l2
# print(DivOfTwo(l1))

#(43)
# l1=[1,2,3,0,0,4,0,5,0]
# def FindAvg(li):
#     count=0
#     sum=0
#     for i in l1:
#         if i!=0:
#             count+=1
#             sum+=i

#     avg=int(sum/count)
#     print(avg)
# FindAvg(l1)


#(44)
# name='hiren nd'
# surname='gonhhhhdaliya'
# common=""
# print(name)
# print(surname)
# for i in range(len(name)):
#     for j in range(len(surname)):
#        if name[i]==surname[j]:
#         common+=name[i]
#         break
            
# print(common)

#(45)
# s1="python is programing language and widly used"
# s1=s1.split()
# def LongWord(s):
#     l_w=s1[0]
#     for i in s:
#         if len(i)>len(l_w):
#             l_w=i
#     return f"{l_w} is length {len(l_w)}"
# print(LongWord(s1))

#(46)
# l1=[15,21,47,54,12,23,61,24]
# def MedFind(l):
#     for i in range(len(l)):
#         for j in range(0,len(l)):
#             if l1[j]>=l1[i]:
#                 temp=l1[i]
#                 l1[i]=l1[j]
#                 l1[j]=temp

#     m=int(len(l1)/2)
#     print(l1[m])
# MedFind(l1)


#(47)
# l1=[80,160,14,20,26,16,28,40,72]
# l2=[]
# def SmalNm(l):
#     for i in l:
#         if i %4==0 and i%5==0:
#             l2.append(i)
#     small=l2[0]
#     for i in l2:
#         if small>i:
#             small=i
#     print(small)
# SmalNm(l1)

#(48)
# divisor_list=[]
# def DivisorNum(num):
#     for i in range(1,num+1):
#         if num%i==0:
#             divisor_list.append(i)
#     return divisor_list
# n=int(input("Enter Number :"))
# print(DivisorNum(n))

#(49)
# s1="Hello welcome To python programing language"
# s1=s1.split()
# s2=[]
# print(s1)
# for i in range(0,len(s1)*2,2):
#     s1.insert(i+1,s1[i][::-1])
# print(s1)

#(50)
# l1=['kohli','ajmer','elephant','mumbai','israel','america','eagle']
# l2=[]
# def VoweStart(l):
#     for i in l:
#         if i.startswith(('e','a','i','u','o')):
#             l2.append(i)
#     print(l2)
# VoweStart(l1)

#(51)
#def CheckValid(s1):
#     if  '.' in s1 and '@' in s1:
#         print("valid :")
#     else:
#         print("Not Valid :")
# email=input("Enter email :")
# CheckValid(email)

#(52)
# s1="hi5re7n@4gma9i.com"
# def DigitSum(s):
#     sum=0
#     for i in s:
#         if i.isnumeric():
#             sum+=int(i)
#     print(sum)
# DigitSum(s1)

#(53)


#(54)
# def DefGrade():
#     Marks=int(input(("Enter Marks :")))
#     if Marks>=0 and Marks<=100:
#         if Marks>85:
#             print("GRADE A")
#         elif Marks>70:
#             print("GRADE B")
#         elif Marks>50:
#             print("GRADE C")
#         elif Marks>35:
#             print("GRADE D")
#         else:
#             print("FAIL")
#     else:
#         print("Invalid ")
# DefGrade()

#(55)

#(56)
# st="hello my name is hiren"
# def WordCount(s):
#     s1=s.split()
#     return len(s)
# print(WordCount(st))

# Q 57: Find Missing Number in Sequence
# Write a function find_missing_number(numbers) that accepts a list of numbers from 1 to N, with one number missing. The function should return the missing number.






#(57)
# li=[15,24,87,51,15,78,24,36,51]
# l2=[]
# for i in li:
#     if i not in l2:
#         l2.append(i)
# print(l2)


# Q 58: Find Common Elements in Two Lists
# Write a function find_common_elements(list1, list2) that accepts two lists and returns a list containing the common elements from both lists.
# l1=['guido','van','rosum',True,'python',1991]

# l2=['pyyhon','is','programing','van',1991,'rossum']
# l3=[]
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)

# Q 59: Sum of Positive and Negative Numbers
# Write a function sum_positive_and_negative(lst) that accepts a list of integers and returns a tuple with the sum of all positive numbers and the sum of all negative numbers.
# l1=[15,12,-34,-12,-10,-5,16,24]
# e=0
# o=0
# for i in l1:
#     if i>0:
#         e+=i
#     else:
#         o+=i
# t=(e,o)
# print(t)

#(60)


# l1=[1,2,3,4,7,8,9]
# l2=[]
# def FindNum(li):
#     for i in range(1,l1[-1]):
#         if i not in l1:
#             l2.append(i)
#     return l2
# print(FindNum(l1))

#(62)
# def PrimFind(n):
#     for i in range(2,n):
#         flag=1
#         for j in range(2,i-1):
#             if i%j==0:
#                 flag=0
#                 break

#         if flag==1:
#             print(f"{i}:prime")
# num=int(input("Enter Number :"))
# PrimFind(num)
   
#(63)
# l1=[]
# def fibo(n):
#     a=0
#     b=1
#     l1.extend([a,b])
#     for i in range(n):
#         c=a+b
#         l1.append(c)
#         a=b
#         b=c
#     print(l1)
# num=int(input("Enter Number :"))
# fibo(num)

#(64)
# l1=[1,3,5,7,8,9]
# l2=[2,4,6,8,10]
# l3=list(zip(l1,l2))
# print(l3)

#(67)
# l1=['java','python','css','html','php']
# l2=[i[::-1] for i in l1]
# print(l2)


# length=int(input('Enter length :'))
# PassGen(length)


#(68)

#(110)
# l1=[True,"hiren","python",3.14]
# l2=['python','develop','by','van','roosum']
# l3=l1+l2
# di=dict(map(lambda i : (l3.index(i),i),l3))
# print(di)

s1="hello my name is hiren".split()
print(s1)
s2=""
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        if len(s1[i])>=len(s1[j]):
            temp=s1[i]
            s1[i]=s1[j]
            s1[j]=temp
    s2+=s1[i]+ " "
print(s2)


#(111)
# di={}
# if len(di)==0:
#     print("Empty")
# #110   
# l1=[12,45,8,74,85,43,73,62,98,75,42,1,3]
# e=0
# o=0
# for i in l1:
#     if i%2==0:
#         e+=1
#     else:
#         o+=1
# print(f"even is : {e}\nodd is : {o}")
#112
#(113)
# l1=[1,2,3]
# l2=[3,4,5]
# l3=set(l1+l2)
# print(l3)


#(114)
# l1=[1,4,5,7,8,6,2,3]
# di={}
# for i in range(len(l1)):
#     di[l1[i]]=l1[i]**2
# print(di)


# (115)
# l1=['hiren',25,True,"python","programning",3.14]
# di={}
# for i in range(len(l1)):
#     di[i]=l1[i]
# print(di)



