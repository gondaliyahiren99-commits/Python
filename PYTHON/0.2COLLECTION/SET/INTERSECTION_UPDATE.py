# intersection_update(other)
# Ye current set ko modify karta hai aur sirf common elements rakh deta hai.
s1={1,2,3}
s2={3,4,5}
s2.intersection_update(s1) # Pehle(s2) Ke Sare Element Remove Karke Ye Jo Dono Me Common Ho Usko Pehle Set Me  Dalega 
# Ye Hamesha Pehle Me Add Karega Or Agra Print Karega To None Return Karega
print(f"s1={1,2,3} s2={3,4,5} s2.intersection_update(s1) = {s2}\n")  # {3}


# difference_update(other)
# Ye current set se common elements hata deta hai.
s1={1 , 2 , 3}
s2={3 , 4 , 5}
# isme Jo Pehle Likha Ho s2 Usme Jo Element Common He Usko Save Karega. Ye s2 Me store KArta Return None
s2.difference_update(s1)  # {1,2}
print(f"s1={1 , 2 , 3} s2={3 , 4 , 5} s2.difference_update(s1) = {s2}\n")


# symmetric_difference_update(other)
# Ye current set ko dono ke unique elements se update karta hai.
a = {1, 2, 3}
b = {3, 4, 5}
s2.symmetric_difference_update(s1)  # {1 , 2 , 4 , 5}
print(f"a = {1, 2, 3} b = {3, 4, 5} s2.symmetric_difference_update(s1) = {s2}\n")

# issubset(other)
# Check karta hai ki pehle set ke saare elements dusre set me hain ya nahi.
a = {1, 2}
b = {1, 2, 3, 4}
print(f"a = {1, 2} b = {1, 2, 3, 4} a.issubset(b) = {a.issubset(b)}\n")  # True

"""
a = {1,2}
b = {1,2,3,4}
1 ✔
2 ✔
Isliye True
"""

a = {1, 5}
b = {1, 2, 3}

print(f"a = {1, 5} b = {1, 2, 3} a.issubset(b) = {a.issubset(b)}\n")

"""Output

False

Kyuki 5 b me nahi hai.Isme Check Karega Ki a Ki PuriKiPuri Value b Me He Ya Nahi"""

"""
issuperset(other)
Check karta hai ki current set me dusre set ke saare elements hain ya nahi."""

a = {1, 2, 3, 4}
b = {2, 3}
print(f"a = {1, 2, 3, 4} b = {2, 3}a.issuperset(b)= {a.issuperset(b)}\n") #True



"""
isdisjoint(other)
Check karta hai ki dono sets me koi common element hai ya nahi."""
a = {1,2}
b = {3,4}

print(f"a = {1,2} b = {3,4} a.isdisjoint(b) = {a.isdisjoint(b)}\n")