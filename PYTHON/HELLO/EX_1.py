"""
QUE  1: ACCEPT A NUMBER FROM THE USER AND FIND THE FACTORIAL OF THE NUMBER USING A FUNCTION WITH A PARAMETER AND RETURN TYPE.
"""
def findfact(num):
    fact =1
    while num>0 :
        fact*=num
        num-=1
    return fact
n= int(input('Enter Number : '))
print(findfact(n))