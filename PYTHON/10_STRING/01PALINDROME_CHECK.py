

"""
for reverse :-
    -use slicing
    var[::-1]
    
                0   1  2  3  4 (positive indexing)
    e.g. name = "h  i  r  e  n"
                -5 -4 -3 -2 -1(Nagative indexing)
    by default start -1(n) se hoga
    by default end   -5(h) se hoga

"""


name ="python"
print(name[::-1])

#check palindrome

s1="mom"
s2="mom"


#=============================================================================================
if s1==s2[: :-1]:
    print("palindrome :")
else:
    print("Not")

#without slicing ravverse
surname= "Gondaliya Hiren"

rev=""
for ch in surname:
    rev=ch+rev
print(rev)
