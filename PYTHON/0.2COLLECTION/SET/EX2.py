# we can only add valuse in set
s={1,2,3,4,5,6,1,2,3,4,2,2}
print(s)
s.add(34)
print(s)

#union
s1={1,2,3}
s2={4,2,5}

print(s1|s2)# 1,2,3,4,5

# inetrsection

print(s1&s2)#2

# difference

print(s1-s2)#1,3