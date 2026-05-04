l1 = ["Hello","this","is","python2.0","progrmanin","522","lamjj"]
l2=[]
l3=[i[:4] if type(i)==str and i.isalpha() else l2.append(i) for i in l1 ]
print(l2)
print(l3)
#jo bbhi element save nahi hoga vaha pr none save save