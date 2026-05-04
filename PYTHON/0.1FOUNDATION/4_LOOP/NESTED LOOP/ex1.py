"""
when loop inside another loop this is called nested for loop


nested for loop :

suntax:

    for var in sequence:
        for var in sequence:
            statement
"""

for i in range(6):#yaha pr i ka index 0 aur j ka index 0 start hoga to wo andar jayega nahi kunki 0 row pe 0 col creat
    for j in range(i):
        print(" * ",end="")
    print()



for row in  range(1,6):
    for col in range(1,6):
        print(" * ",end=" ")
    print()

    """
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    """