# con vert into int
l1=['21','3','82','65','70','43']
def myfun(num):
    return int(num)
l2=list(map(myfun,l1))
print(f"{l1}\n{l2}")
print("="*100)

l4=list(map(lambda num: int(num),l1))
print(l4)
print("="*100)


l3=list(map(int,l1))
print(l3)
