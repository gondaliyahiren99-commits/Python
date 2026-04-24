"""
I
IN
IND
INDI
INDIA
"""

word="INDIA"

for seq in range(0,len(word)):
    for char in range(0,seq+1):
         print(word[char],end=" ")
        

    print()