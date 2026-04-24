l1=[ "even" if i%2==0 else "odd" for i in range(1,6)]
print(l1)

l1=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,6)]
print(l1)

l1=[ f"{i} is even"  if i%2==0 else f"{i} is odd" for i in range(1,6)]
print(l1)

l1=["pos" if i>0 else "nag" for i in range(1,6)]
print(l1)


