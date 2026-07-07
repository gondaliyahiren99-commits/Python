"""
QUE  74: PRINT PRIME NUMBERS IN A RANGE
WRITE A FUNCTION PRINT_PRIMES_IN_RANGE(START, END) THAT ACCEPTS TWO NUMBERS AND PRINTS ALL PRIME NUMBERS BETWEEN START AND END (INCLUSIVE).

"""
s=int(input("Enter Start Number : "))
e=int(input("Enter Last Number : "))
primta_number=[]
for i in range(s,e+1):
    is_primme=True
    for j in range(2,i):
        if i%j==0:
            is_primme=False
            break
    if is_primme and i>1:
        primta_number.append(i)
print(primta_number)
