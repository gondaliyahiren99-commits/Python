"""
ASCII  converstion 
#a A to Z
# a to z
# 0 to 9(string or character)
# any character like *
ki ascii valu hogi
"""


char=input("enter a character :")[0]#"python" me se  khali first ka (p)ascii value btaye ga agar hum 
                           #[0]isko htake isme ek se jyada value denge to erorr hoga fir ascii nhi hoga  
print(char)#p
ascii_val=ord(char)
print(ascii_val)

name=65
name=chr(name)
print(name)#A


num=input("Enter number :")# yaha pr hum number ko ascii value hogi pr vo string type me hogi
#(0 se 9) me but string honi chahiye qtherwise typeerror show hoga int ka ascii nahi hoti
ascii_value1=ord(num)
print(ascii_value1)