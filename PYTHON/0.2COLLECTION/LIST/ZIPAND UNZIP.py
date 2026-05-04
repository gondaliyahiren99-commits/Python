l1 = [15,12,14,32]
l2= [21,24,28,27]
l3=list(zip(l1,l2))
print(l3)



name = ['dabeli','vadapav','pakoda','bhel']
price =[35 , 30  , 20]
menu  = list(zip(name,price))
print(menu)



n,p =list(zip(*menu))
print(n)
print(p)
