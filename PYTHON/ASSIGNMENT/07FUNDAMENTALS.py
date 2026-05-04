"""• Defining and calling functions in Python.
    function Defining :
        function defining me define karna padta he ke hume kya output chahiye or kya logic rahega.

    function calling :
        function calling mjab bhi code ki jarrorat ho tab bas function ko call karte he.
        function ko call karte hi function define me likha pura code execute hoga.

• Function arguments (positional, keyword, default).
    functional positional : function call ke time jo value pehle likhi hoti he wo pehla variable 
    jo function perameter me likha hota he usme jata he  .wese hi position pr depend rehta he .

    keyword : function keyword yani function call ke time hum function oeremeter me jo variable likhte he wo function call me 
    variable likh ke usme variable assign karte he . taki value usi variable me jaye. isme position ki tarah confusion nahi rehta.


• Scope of variables in Python.
    Globale Declare : jab  hum variable ko function ke bahar declare karte he tab kahi pr bhi uska use kar sakte he.
                    but agar variable ko function ke andar declare karne pr variable ko bahar acess nahi kar sakte.

• Built-in methods for strings, lists, etc.
    built in method
    upper()  : har ek character ko upper case me convert ke liye.
    lower() : caharcter ko loer case me convert karne ke liye.
    title() : string har ek word ka pehla character ko uppercase me convert karta he.
    capitilize() : string me sirf first word ka first character ko upper me convert karta he.

"""

#==============================================================Lab Exercise=============================================================
#==================================================================(1)================================================================
#Write a Python program to print "Hello" using a string.
def fun(st):
    return st
s1 = input("enter string :")
print(fun(s1))

# #==================================================================(2)================================================================
# #Write a Python program to allocate a string to a variable and print it.
def funone(st):
    s2=st
    return s2
s1 = input("Enter String :")
print(funone)


#==================================================================(3)================================================================
#Write a Python program to print a string using triple quotes.
def sprint(s1):
    print(s1)

s = """Hiren"""
sprint(s)
#==================================================================(4)================================================================
#Write a Python program to access the first character of a string using
def acess0index(s):
    return s[0]

s1 = "Hiren"
print(acess0index(s1))
#==================================================================(5)================================================================
#Write a Python program to access the string from the second position onwards using slicing.
def findsec(s1):
    print(s1[1:2])
name = "Hiren"
findsec(name)
#==================================================================(6)================================================================
#Write a Python program to access a string up to the fifth character.
def findfifth(l):
    print(l[6])
lan = "pythonprograming"
findfifth(lan)

#==================================================================(7)================================================================
#Write a Python program to print the substring between index values
def SubVal(s2):
    s2 = s2[1:5]
    return s2
s = input("Enter String : ")
print(SubVal(s))

#==================================================================(8)================================================================
#write a Python program to print a string from the last character.
def lastChar(s):
    print(s[-1])

s1 = "hiren"
lastChar(s1)
#==================================================================end================================================================