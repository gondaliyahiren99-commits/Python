"""
QUE  2: WRITE A FUNCTION THAT ACCEPTS A STRING AND RETURNS TRUE IF THE STRING IS A PALINDROME, AND FALSE OTHERWISE.
"""
# def PalindromeCheck(s):
#     if s == s[::-1]:
#         print("palindrome")
#     else:
#         print('Not')
# st = input("Enter String :")
# PalindromeCheck(st)



s="maram"
flag =1
for i in range(0,len(s)):
    if s[i]!=s[len(s)-i-1]:
        flag =0
        break
    i+=1
if flag ==1:
    print("yesj")
else :
    print('Not')