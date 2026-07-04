s1={"Toomy",1,"India","MArsh",12.25,True}
s2={"Jerry",12.25,"India",1,256}
print(s2.difference(s1))   # Ye Sirf Jo Data first Yaha s2 Liya He To Wo Sirf S2 Ke Element Jo s1 Me Nahi He Wo Lega {"Jerry",256}
print(s2.symmetric_difference(s1)) # Jo Dono Me Uniq Ho Na Duplicat Na Common Dono Me 

# intersection_update(other)	Set ko common elements se update karta hai.
# difference_update(other)	Common elements remove karke set update karta hai.
# symmetric_difference_update(other)	Set ko symmetric difference se update karta hai.
# issubset(other)	Check karta hai ki set dusre set ka subset hai ya nahi.
# issuperset(other)	Check karta hai ki set dusre set ka superset hai ya nahi.
# isdisjoint(other)
print(s1.intersection_update(s2))