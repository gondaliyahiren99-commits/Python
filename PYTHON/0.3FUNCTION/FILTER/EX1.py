#save only even numbers
l1=[12,23,34,54,72,27,62,1,87,92]
def myfun(num):
    if num%2==0:
        return num
l2=list(filter(myfun,l1))
print(f"{l1}\n{l2}")




# lambda
l3=list(filter(lambda num: num%2==0,l1))
print(l3)