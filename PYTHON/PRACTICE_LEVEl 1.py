# #(1)Find factorial
# def facto_rial(num):
#     n=1
#     for i in range(1,num+1):
#         n*=i
#     return n
# num=int(input("Enter Number :"))
# print(facto_rial(num))

#(2)check strig is palindrome 
# def palin_drome(str):
#     if str==str[::-1]:
#         return f"{str} is palindrome"
#     else:
#         return f"{str} is Not Palindrome"
# str=input("Enter string :")    
# print(palin_drome(str))


# #(3)sum of evev Number
# sum=0
# def sumofeven(l): 
   
#     return sum+=l
# l1=[12,45,78,54,21,34,51,23,26]
# filter(sumofeve)



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


#(70)
s1=['hello', 'my', 'name', 'is', 'hiren']
# print(s1)
# s2=""
# for i in range(len(s1)):
#     for j in range(i+1,len(s1)):
#         if len(s1[i])>=len(s1[j]):
#             temp=s1[i]
#             s1[i]=s1[j]
#             s1[j]=temp
#     s2+=s1[i]+ " "
# print(s2)


#(71)
# duct1={'name1': "hiren",'age1' : 25, 'Course1' : "python"}
# dict2={'name': "Atul",'age':27,'course': 'java'}
# for k,v in dict2.items():
#     duct1[k]=v

# print(duct1)

# (72)
# Q 73: Flatten a Nested List
# Write a function flatten_list(nested_list) that accepts a nested list (list containing other lists)
# and returns a flat list containing all the elements.

#(74) Print Prime Numbers in a Range
# Write a function print_primes_in_range(start, end) that accepts two numbers and prints all prime numbers between start and end (inclusive).
# def findPrime(num):
#     for i in range(2,num):
#         flag=1
#         for j in range(2,i):
#             if i%j==0:
#                 flag=0
#                 break
#         if flag==1:
#             print(i)
# n=int(input("Enter number :"))
# findPrime(n)

#(75)
# Find the Longest Word in a Sentence
# Write a function longest_word(sentence) that accepts a sentence and returns the longest word in the sentence.
# def longword(s):
#     lW=""
#     s=s.split()
#     for i in s:
#         if len(i)>len(lW):
#             lW=i
#     print(lW)
# sen="hello python , pytho high-level interpreted language"
# longword(sen)

#(76) Convert a String to Title Case
# Write a function to_title_case(sentence) that accepts a string
#  and returns the string in title case (the first letter of each word capitalized).
# def TitleCase(sen):
#     sen=sen.title()
#     print(sen)
# sentance="hello ! my name is hiren i am software engineer"
# TitleCase(sentance)

#(77)
# Q 77: Count the Occurrence of Each Character
# Write a function count_character_occurrences(string) that accepts a string and
#  returns a dictionary with the count of each character in the string.
# def count_character_occurrences(st):
#     di={}
#     for i in st:
#         di[i]=st.count(i)
#     return di

# str="python high-level interpreted language"
# print(count_character_occurrences(str))

#(78)
#Calculate Simple Interest
# Write a function calculate_simple_interest(principal, rate, time) that accepts
# the principal, rate of interest, and time, and returns the calculated simple interest.
# def calculate_simple_interest(p,r,t):
#     si=p*r*t//100
#     return si
# principle=int(input("Eneter a amount :"))
# rate=int(input("Eneter a rate :"))
# time=int(input("Eneter a time :"))
# print(calculate_simple_interest(principle,rate,time))

#(79)
#Find Unique Elements in List
# Write a function find_unique_elements(lst) that accepts a list 
# and returns a new list containing only the unique elements from the original list.
# def find_unique_elements(l):
#     l2=[]
#     for i in l:
#         if l.count(i)<2:
#             l2.append(i)
#     return l2
# l1=["python",'java','css','java','php','c','flutter','python','css','c','rectjs','js']
# print(find_unique_elements(l1))

# (80)Generate Multiplication Table
# Write a function generate_multiplication_table(n) that accepts a number n10
#and prints its multiplication table (from 1 to 10).
# def generate_multiplication_table(n):
#     for i in range(1,11):
#         for j in range(1,n+1):
#             tab=f"{i} * {j} = {i*j}"
#             print(tab)
#         print("\n",end="")
# num=int(input("Enter Number :"))
# print(generate_multiplication_table(num))

#(81)reate a Dictionary from Two Lists
# Write a function create_dict(keys, values) that accepts two lists, keys and values, and
#  returns a dictionary where the keys are from the first list and the values are from the second list.
# def create_dict(keys, values):
#     di=dict(zip(keys,values))
#     return di

# l1=['name','course','marks','city','rollno']
# l2=['hiren','python',93.75,'ahmedabad',37]
# print(create_dict(l1,l2))

#(82)
# Check if Two Strings are Anagrams
# Write a function is_anagram(str1, str2) that accepts two strings and
#  checks if they are anagrams of each other (i.e., they contain the same characters in different orders).
# def is_anagram(s1, s2):
#     is_ana=1
#     for i in s1:
#         if s1.count(i)!=s2.count(i):
#             is_ana=0
#     if is_ana==1:
#         print("yes")
#     else:
#         print("Not") 
# str1=" i2 am hiren"
# str2=" nai2 mher i"
# is_anagram(str1,str2)

#(83)
# Count Occurrences of Words in a Sentence
# Write a function count_word_occurrences(sentence) that accepts a sentence 
# and returns a dictionary with the count of each word in the sentence.
# def count_word_occurrences(s):
#     s=s.split()
#     di={}
#     for i in s:
#         di[i]=s.count(i)
#     print(di)    
# sentance="python java css java php c flutter python css c rectjs js"
# count_word_occurrences(sentance)

#(84)
# Remove Duplicates from a List of Strings
# Write a function remove_duplicates(lst) that accepts a list of strings
#  and returns a new list with duplicate strings removed.
# def remove_duplicates(li):
#     new_lst=[]
#     for i in li:
#         if i not in new_lst:
#             new_lst.append(i)
#     print(new_lst)
# lst=["python",'java','css','java','php','c','flutter','python','css','c','rectjs','js']
# remove_duplicates(lst)

#(85)


#(85)
#Find the Most Frequent Element in a List
#Write a function find_most_frequent(lst) that accepts a list of elements and 
# returns the most frequent element in the list. If there are multiple frequent elements, return any one of them.
# def find_most_frequent(li):
#     count=0
#     for i in li:
#         if li.count(i)>count:
#             count=li.count(i)
#             fre_ele=i
#     print(fre_ele)

# lst=[1,'java',3.14,'java','php','python','flutter','python','python',3.14,1,'rectjs','js']
# find_most_frequent(lst)


#(87)
#Merge Two Dictionaries
#Write a function merge_dicts(dict1, dict2) that accepts two dictionaries and merges them into one.
#  If there are overlapping keys, the values from the second dictionary should overwrite the values from the first.d
# def merge_dicts(di1, di2):
#     for k,v in  di2.items():
#         di1[k]=v
#     return di1
# dict1={'name':'hiren','city':'junagadh', 'course':'python'}
# dict2={'city':'ahemdabad', 'year': 2025}
# print(merge_dicts(dict1,dict2))


#(88)
#Count the Occurrence of Each Item in a List
#Write a function count_items(lst) that accepts a list of items and returns a dictionary 
# where the keys are the items from the list, and the values are the number of times each item appears.
# def count_items(li):
#     pass
#     di={}
#     for i in li:
#         di[i]=li.count(i)
#     return di
# lst=[1,'java',3.14,'java','php','python','flutter','python','python',3.14,1,'rectjs','js']
# print(count_items(lst))


#(89)
#Create a Dictionary from Two Lists
#Write a function create_dict(keys, values) that accepts two lists: one containing keys and the other containing values. 
# The function should return a dictionary with the keys from the first list and the corresponding values from the second list.
# def create_dict(keys, values):
#     di=dict(zip(keys,values))
#     print(di)
# lst1=['name','surname','roll_no', 'marks','course']
# lst2=['hiren','gondaliya',132,87.32,'python']
# create_dict(lst1,lst2)

#(90)
#Remove Duplicates from a List and Keep Order
#Write a function remove_duplicates(lst) that accepts a list and removes any 
# duplicate elements while keeping the original order of the elements.
# def remove_duplicates(li):
#     for i in li:
#         if li.count(i)>1:
#             i=li.index(i)
#             li.pop(i+1)
#     print(li)

# lst=[1,5,7,8,5,4,1,8,9,3,7,5,2]
# remove_duplicates(lst)


#(91)
#  Sort a Dictionary by Value
# Write a function sort_dict_by_value(d) that accepts a dictionary 
# and returns a new dictionary sorted by its values in ascending order.
# def sort_dict_by_value(d):
#     di2={}
#     d{}
# di={'hiren':5,'nisarg':1,'jenish':4,'mustved':2,'neel':3}
# sort_dict_by_value(di)

#(92)
#Sum All Values in a Dictionary
#Write a function sum_dict_values(d) that accepts a dictionary where the values are numbers. 
#The function should return the sum of all values in the dictionary.
# def sum_dict_values(d):
#     sum=0
#     for k,v in d.items():
#         sum+=v
#     print(sum)

# di={'hiren':5,'nisarg':1,'jenish':4,'mustved':2,'neel':3}
# sum_dict_values(di)

#(92)
#Find the Key with the Maximum Value in a Dictionary
#Write a function find_max_key(d) that accepts a dictionary and returns 
# the key that has the highest value. If there are multiple keys with the same maximum value, return any one of them.
# def  find_max_key(d):
#     max=0
#     for k,v in d.items():
#         if v>max:
#             max=v
#     print(max)
    
# di={'hiren':4,'nisarg':1,'jenish':5,'mustved':2,'neel':3}
# find_max_key(di)

#(93)
#List of Keys with Minimum Value
#Write a function min_value_keys(d) that accepts a dictionary and returns 
# a list of keys that have the minimum value in the 
# def min_value_keys(d):
#     min_val=min(d.values())
#     l1=[]
#     for k,v in d.items():
#         if min_val==v:
#             l1.append(k)
#     print(l1)

# di={'hiren':4,'nisarg':1,'jenish':5,'mustved':2,'neel':3}
# min_value_keys(di)


#(94)
#Combine Multiple Lists into a Dictionary
# Write a function combine_lists_to_dict(keys, values) that accepts two lists, one containing keys and 
# the other containing values. The function should combine them into a dictionary and return it. 
# If there are more values than keys, ignore the extra values
# def combine_lists_to_dict(keys, values):
#     di=dict(zip(lst1,lst2))
#     return di

# lst1=['name','surname','roll_no' 'marks','f_name','course','f']
# lst2=['hiren','gondaliya',132,92.32,'python','hiren']
# print(combine_lists_to_dict(lst1,lst2))

#(95)

#Q 96: Check if a Dictionary Contains a Specific Key
#Write a function contains_key(d, key) that accepts a dictionary and a key. 
# It should return True if the key exists in the dictionary and False otherwise
#

#(97)
#Flatten a List of Lists
#Write a function flatten_list_of_lists(lst) that accepts a list of lists (a nested list) 
#and returns a flat list containing all the elements of the inner lists.
# def flatten_list_of_lists(lst):
#     l2=[]
#     for i in lst:
#         for j in i:
#             l2.append(j)
            
#     print(l2)
# l1=[['python','java'],['c','c++'],['.net','flutter']]
# flatten_list_of_lists(l1)



#(98)
#Find the Difference Between Two Lists
#Write a function find_difference(lst1, lst2) that accepts two lists and returns 
# a new list containing elements that are in the first list but not in the second.
# def find_difference(l1, l2):
#     l3=[]
#     for i in l1:
#         if i not in l2:
#             l3.append(i)
#     print(l3)
# l1=[10,20,25,3,4]
# l2=[5,4,2,1,2]
# find_difference(l1,l2)

#(99)
#Group List Elements by Frequency
#Write a function group_by_frequency(lst) that accepts a list and groups the elements based on their frequency.
#The function should return a dictionary where the keys are the frequencies and the values are lists of elements that occur that many times.

# def group_by_frequency(lst):
#     di={}
#     for i in lst:
#         di[lst.count(i)]=I
#         if lst.count(i) in di:
#             d[
            

    

# li=[1,5,4,7,4,4,7,8,2,6,6]
# group_by_frequency(li)

#(100)
#Find the Common Keys in Two Dictionaries
#Write a function find_common_keys(dict1, dict2) that accepts two dictionaries and returns 
#a list of keys that appear in both dictionaries.


#(101)
#Update Dictionary Values Based on Another Dictionary
#Write a function update_dict(d1, d2) that accepts two dictionaries. 
#It should update the values of d1 with the values from d2 where the keys match. If a key from d2 does not exist in d1, it should be added.


#(102)
#Find the Longest Key in a Dictionary
#Write a function longest_key(d) that accepts a dictionary and returns the key with the longest length.
# di={'name':'hiren','course':'python','sub':'math'}
# l_k=""
# for k,v in di.items():
#     print(k)
#     if len(k)>len(l_k):
#         l_k=k
# print(l_k)


#(103)
#Check if a List Contains Only Unique Elements
#Write a function is_unique(lst) that accepts a list and returns True
# if all the elements are unique, and False if any element appears more than once.
# l1=['python','c','java','php','c','c++']
# is_unique=True
# for i in l1:
#     l1.remove(i)
#     if i in l1:
#         is_unique=False
#         break
#     l1.append(i)
# if is_unique==True:
#     print("uniqqu")
# else:
#     print("Not")


    
#(104)
# Convert a Dictionary to a List of Tuples
#Write a function dict_to_tuples(d) that accepts a dictionary and returns 
#a list of tuples where each tuple contains a key-value pair from the dictionary.
# di={'product':'waffer',
#     'price':500,
#     'disc': 120,
#     'type': 'Masala'}
# t=[]
# for k,v in di.items():
#     t.append((k,v))
# print(t)


#(105)
#Find Missing Numbers in a List
#Write a function find_missing_numbers(lst, n) that accepts a list of integers and a number n.
# The list contains integers from 1 to n with some numbers missing. The function should return a list of the missing numbers.
# l1=[1,2,3,4,5,6,8,9]
# for i in range(1,len(l1)+1):
#     if i not in l1:
#         mis_num=i
# print(mis_num)

#(106)
#Split a List into Two Lists
#Write a function split_list(lst) that accepts a list and splits it into two lists. 
# The first list should contain the first half of the elements, and the second list should contain the second half.
# lst=['name','hiren','course','python','year',2025,'baranch','C G ROAD']
# l1=[]
# l2=[]
# for i in range(len(lst)):
#     if i<len(lst)//2:
#         l1.append(lst[i])
#     else:
#         l2.append(lst[i])
# print(l1)
# print(l2)

#(107)
#Sum All Even Keys in a Dictionary
#Write a function sum_even_keys(d) that accepts a dictionary with integers as keys and 
# returns the sum of all keys that are even numbers.
# di={1:'python',2:'java',3:'css',4:'php'}
# s=0
# for i in di:
#     i=int(i)
#     if i%2==0:
#         s+=i
# print(s)

#(108)
#: Create a Frequency Dictionary from a List
#Write a function create_frequency_dict(lst) that accepts a list and returns a dictionary
# where the keys are the elements of the list, and the values are the count of how often each element appears.
# l1=[1,5,4,8,5,3,4,1,5,8,4,1,5,5]
# di={}
# for i in l1:
#     di[i]=l1.count(i)
# print(di)


#(109)
#Merge Two Lists into a Dictionary with List Indices as Keys
#Write a function merge_lists_into_dict(list1, list2) that accepts two lists of equal length 
# and merges them into a dictionary where the keys are the indices (0 to n-1) and the values are the elements from both lists.
# l1=['name','course','year']
# l2=['hiren','python',2026]
# l3=list(zip(l1,l2))
# sub={}
# di={}
# for i in range(len(l3)):
#     sub={l1[i] :l2[i]}
#     di[i]=sub
# print(di)

#(110)
# e=0
# o=0
# l1=[12,42,1,78,13,31,52,21,33]
# for i in l1:
#     if i%2==0:
#         e+=1
#     else:
#         o+=1
# print("even is {} and odd is {}".format(e,o))


#(111)
#Check if a Dictionary is Empty
#Write a function is_empty(d) that accepts a dictionary and returns True 
# if the dictionary is empty, otherwise False.
# is_empty=False
# di={}
# if len(di)==0:
#     is_empty=True

# if is_empty:
#     print("yes")
# else:
#     print("Not")

#(112)
#Remove Keys from Dictionary Based on a Condition
#Write a function remove_keys_by_condition(d, condition) that accepts a dictionary and 
#removes the keys where the corresponding values satisfy a condition. For example, removing all keys with values greater than a specific threshold.
# di={'name':'hiren','course':'python','brnch':'TopsTech','language':'english'}
# di2={}

# for k,v in di.items():
#     if len(v)<6:
#         continue
#     else:
#         di2[k]=v
# print(di2)



#(113)
#Find the Union of Two Lists
#Write a function find_union(lst1, lst2) that accepts two lists and returns a new list 
# that contains the union of both lists (all elements from both lists without duplicates).
# l1=[1,2,3,4,5]
# l2=[2,1,4,7,8]
# l3=list(zip(l1,l2))
# for i in l1:
#     if i not in l3:
#         l3.append(i)
#     else:
#         continue
# for i in l2:
#     if i  not in l3:
#         l3.append(i)



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

