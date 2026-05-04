""" 
*********************************************************9. String Manipulation*********************************************************************
# Theory:

# • Understanding how to access and manipulate strings.

1) Acces a single character of string :

        When we acess a single character of string we use index of string.
        Positive indexing  is start from 0 (left to Right)
        And nagative indexing is start from -1 (Right to Left)

        Syntax :  <varible_name>[index]

        e.g. 

        0   1   2   3    4     (positvi index)
        H   i   r   e    n
       -5  -4  -3  -2   -1     (Nagative index)

        st = "Hiren"
        print(st[0])    Acces 'H'
        print(st[3])    Acess 'e'
        print(st[-1])   Acess 'n'
        print(st[4])    Acess 'n'

2) String slicing : When we can extract parts of a string (Substring) using slicing.
    
    Syntax : s1[start : end : step]
            slicing by default 0  and end by default value string ki length leta he and by defult step +1 karta he 

        s1 = "Hiren"
        print(s1[0 : 2])  --> Hir
        print(s1[:5])     --> Hiren
        print(s1[0:])     --> Hiren
        print(s1[-1:-4:-1])  --> ner

3) Loop Throgh :
        s1 = "Hiren"
        for i in s1 :
            print(i)

    -->Output : Hiren    



# • Basic operations: concatenation, repetition, string methods (upper(), lower(), etc.).

1) Concatenation : Concatnetion use for merge string.
 e.g. 
 f_name = "Hiren "
 l_name = "Gondaliya"

full_name = f_name + l_name
print(full_name)

-->Output : Hiren Gondaliya

2) Repeatation : string to repeat
print("hi" * 3)

-->Output : hi hi hi

3) Stringe Case Method : String case method help us to string character case change
        (A) Upper Case  : to change all chaeacter into Upper Case.

                e.g.  Name = "hiren"
                      print(Name.upper())

                    -->Output : HIREN

        (B) Lower Case : to convert word of all character into lower case.

                e.g. Name = "HIREN"
                     print(Name.lower())

                -->Output : hiren

        (C)Title Case : Each word of Sentance first character convert into upper case.

                e.g. Name = "hiren gondaliya"
                     print(Name.title())

                -->Output : Hiren Gondaliya 

        (D) Capitalize : Convert the first character of the first word in a sentence to uppercase.”

# • String slicing :  When we can extract parts of a string (Substring) using slicing.
    
    Syntax : s1[start : end : step]


    slicing in start by default 0.
    end by default value Length of string.
    step by defaul +1 leta he.

    s1 = "Hiren"
    print(s1[0 : 2])  --> Hir
    print(s1[:5])     --> Hiren
    print(s1[0:])     --> Hiren
    print(s1[-1:-4:-1])  --> ner

"""


#==============================================================Lab Exercise=============================================================
#==================================================================(1)================================================================
# Write a Python program to demonstrate string slicing.
s1 = "python programning"

print(f"string is : {s1}") # ing
print(f"first 3 character : {s1[:3]}")  # ing
print(f"last 3 character : {s1[len(s1)-3:len(s1)]}") # ing
print(f"last 3 character : {s1[-3::]}")
print(f"Reverse : {s1[::-1]}") # gninmargorp nohtyp
print(f"index 2 to 6 : {s1[2:7:]}") # thon

#==================================================================(2)================================================================
# Write a Python program that manipulates and prints strings using various string methods
s1 = "    mY Name iS Hiren123    "

# Case convention
print(f"Upeer Case :{s1.upper()}")
print(f"Lower Case :{s1.lower()}")
print(f"Title Case :{s1.title()}")
print(f"Capitalize Case :{s1.capitalize()}")


s2 = "Hello123"
# Check method
print(f"is alpha :{s2.isalpha()}") #False
print(f"is Numeric  :{s2.isnumeric()}") #false
print(f"is alnumeric :{s2.isalnum()}")  #True

#  Counting
print(f"a count {s1.count('e')}") # 2
print(f"a find {s1.find('e')}") # 6
print(f"a Index : {s1.index('e')}") # 6

# Replace & strip
print(f"Replace a to @ : {s1.replace('a','@')}") # mY N@me iS Hiren123
print(f"Remove spaces from right :{s1.rstrip()}")#mY Name iS Hiren123
print(f"Remove spaces from left:{s1.lstrip()}")  #    mY Name iS Hiren123
print(f"Remove spaces bothe side :{s1.strip()}") #mY Name iS Hiren123

# Splitting & joining
print(f"string to list :{s1.split()}") #'mY', 'Name', 'iS', 'Hiren123']
print(f" Join with :{"_".join(s1)}") # _ _ _ _m_Y_ _N_a_m_e_ _i_S_ _H_i_r_e_n_1_2_3_ _ _ _
