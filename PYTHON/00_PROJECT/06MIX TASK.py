
# res="even" if num%2==0 else "odd" "
# print(res)

# def check_num():
#     num=int(input('Enter Number :'))
#     if num==0:
#         print("zero")

#     elif num%2!=0:
#         print("odd")
    
#     else:
#         print("Even")
    

# check_num()

# def check_num():
#     num=int(input('Enter Number :'))
#     if num>0:
#         print("Positive")

#     elif num<0:
#         print("nagative")
    
#     else:
#         print("Zero")
    

# check_num()

# a=10
# b=20
# c=15
# if a>b:
#     if a>c:
#         print(a)
# elif b>c:
#     print(b)
# else:
    # print(c)

"""year=int(input("Enter Year :"))
if year%4==0:
    if year%400==0:
        print("Yes")
else:
    print("not")"""

# num=int(input("Enter Number :"))
# if num%5==0
#     if num%10==0:
#         print("BY 5 OR 10 :")
#     else:
#         print("ONLY 5 :")
# else:
#     print("NO 5 And 10 :")

# s1=input("Enter String :")
# if s1==s1[-1::-1]:
#     print("PALINDROME :")

# else:
#     print("not")


# marks=int(input("Enter Marks :"))
# if marks<=100 and marks>0:
#     if marks>=85:
#       print("A")
#     elif marks>=70:
#         print("B")
#     elif marks>=50:
#         print("C")
#     elif marks>=35:
#         print("D")
#     else: 
#         print("FAIL")
# else:
#     print("INVALID")

# num=int(input("Enter Number :"))
# if num>0 and num<10:
#     print("range")
# else:
#     print("Not ")


# ch=input("Enter Char :").upper()
# if ch=='A' or ch=='E'or ch=='O' or ch=='I' or ch=='U':
#     print("Vowel")
# else:
#     print("CONSONET")

# num=int(input("Enter Number"))
# for i in range(2,num-1):
#     flag=1
#     if num%i==0:
#         flag=0
#         break
# if flag==1:
#     print("primr:".upper())
# else:
#     print("not prime".upper())

"""

loop

"""
# for i in range(0,100,2):
#     print(i)
# sum=0
# num=int(input("Enter Number :"))
# for i in range(num+1):
#     sum+=i
# print(sum)

# num=int(input("Enter Number"))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

# a=0
# b=1
# print(a)
# print(b)
# for i in range(5):
#     c=a+b
#     print(c)
#     if c==5:
#         break
#     a=b
#     b=c

# num=int(input("Enter Number"))
# for i in range(1,num):
#      flag=1
#      for j in range(2,i-1):
#         if i%j==0:
#             flag=0
#             break
#      if flag==1:
#         print(i)
    
# s1="hiren"
# vowel=0
# for i in s1:
#     if i=='a'or i=='i'or i=='o'or i=='u'or i=='e':
#         vowel+=1
# print(vowel)