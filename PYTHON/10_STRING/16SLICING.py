'''
string slicing
+   0    1   2   3   4   5  (positiv index)
    p    y   t   h   o   n
-  -6   -5  -4  -3  -2  -1  (nagetiv index) isme 0 nhi hota

fetch first 2 charector fromgiving string
***string index me end vala index show nahi karta****
'''
name="JAYANT"
"""


                 0     1    2    3    4    5 (positive index)
                 J     A    Y    A    N    t
                -6    -5   -4   -3   -2   -1(Nagative index)
"""
# print(name[0:3])# JAY [last ka char index 3 ka fetch nahi karega]

# print(name[:3])# JAY [start value me khch na likhne se wo start me 0 lega (positve index me )]

# # fetch last 3 chrecter
# print(name[-3:-1])# ye last ka <t> nhi dikhaye ga |output: on

# print(name[-3:])

# size=len(name)
# print(name[size-3:size])
print(name[:-3:]) #agar start me kuch na likheto nagative index start position 0 rahega

print(name[::-1])  #tnayaj yaha pr step -1 karne se wo nagtive index samjega or wo start value -1 se end tak jayega

print(name[-1::])