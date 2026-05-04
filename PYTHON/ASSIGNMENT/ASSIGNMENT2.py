"""                              ******** Python Collections, functions and Modules*********

** Understanding how to create and access elements in a list.
        list create karne ke liye list ka name and aur jo bhi value likhni hoti he use square braces me likha jata he.
        usme hum har datatype ki value store kar sakte he. jese ki string,int,float or boolen.
        agar ek single value acces karni ho to indexing ka use karte he.
        or har ek value acces karne ke liye loop chala kar acess kar sakte he.

** Indexing in lists (positive and negative indexing).
        indexing Do type ki hoti he.
        1)positive indexing : 
                positive indexing start point 0 hota he aur end point sequence ki jo length hoti he waha tak hota he.
                ye left se right ke way me hoti he.

        2)nagative indexing :
                Nagative index jo right se left ke way me hoti he. uski starting point -1 hota he.
            

** Slicing a list: accessing a range of elements.
        slicing se hum extract part of list acess kar sakte he.
        l1 = ["Hello" , 1 , 3.14 , True , "45" , "python"]
        print(l1[1:5:])  

    ~~>output : [ 1 , 3.14 , True , "45"]
"""
#Write a Python program to create a list with elements of multiple data types (integers,
#strings, floats, etc.).

from math import factorial
from numpy.ma.core import sqrt
from math import floor
from math import ceil
from numpy import square
l1 = ["Hello" , 1 ,"False", 3.14 , True ,-64, "45" , "python"]
for i in l1 :
    print(i)

# Write a Python program to access elements at different index positions.
l1 = ["Hello" , 1 ,"False", 3.14 , True ,-64, "45" , "python"]
print(l1[2])  #False
print(l1[len(l1)-1])  #python
print(l1[-3])   #-64

#find length :
print(len(l1))   # 8

"""                                   2. List Operations
Theory:

#Common list operations: concatenation, repetition, membership.
Concatenation : do string ko ek me merge karne list concaenation kaha jata he.
            e.g. l1 = [1 , 2 , 3]
                 l2 = [4 , 5 , 6]
                 l3 = l1 + l2 
        Now l3 me [1,2,3,4,5,6] he.

Repetation : List me element ko bar bar repeat karne ko repetatin kehete he. isse list ko multiple time duplicate elememeta add kar sakte he
             e.g. l1 = [1 , 2 , 3]
                  l2 = l1 * 3
        Now l2 in [1 , 2 , 3 , 1 , 2 , 3 , 1 , 2 , 3]

 Membership : List me koi element exsist karta he ke nahi wo check karne ke liye ye oprater use hote he.
    l1 = [1 , 2 , 3]
    1)in : list me include he to condition true hogi
            e.g. 
            if 3 in l1 :
                print("Exsist")
    2)not in : list me nahi he wo check karne ke liye.
             if 4 in l1 :
                print("Not Exsist")
    
"""
# Write a Python program to add elements to a list using insert() and append().
# Write a Python program to remove elements from a list using pop() and remove().
l1 = ["Hello" , 1 ,"False", 3.14 , True ,-64, "45" , "python"]

l1.append("Namste")  # l1 =["Hello" , 1 ,"False", 3.14 , True ,-64, "45" , "python" , "Namste"]
# append se jo bhi add karenge wo last index pe jakar add hogi 
# agar hume koi specific index pr add karna he to insert ka use karenge

l1.insert(3 , "Welcome")    #l1 = ["Hello" , 1 ,"False","welcome", 3.14 , True ,-64, "45" , "python","Namste"]

#remove hum koi value se karna chahe tab remove () ka use karenge,
l1.remove("False")  # ["Hello" , 1 , "welcome" , 3.14 , True ,-64, "45" , "python","Namste"]
# aur specific index se karna chahe tab pop() use 
l1. pop(2) # ["Hello" , 1 , 3.14 , True ,-64, "45" , "python","Namste"]
l1.pop()  #se hum last index pe jo value hogi wo remove hogi

"""                                               3. Working with Lists
Theory:
• Iterating over a list using loops.
Iter ka use  karke hum list ke sare element one by one access kar sakte he.list ke har ek element iter ghumenga or acess hoga.
• Sorting and reversing a list using sort(), sorted(), and reverse().
sort() : sorting se hum list har ek integer  element ko accending ya decendind order me kar sakte he.sort() ke use time list me sab element int type me hone chahiye.
othrwise error through hogi. sort() original list ko affect karega. wo dusre list me add nahi ho sakta

sorted() : sorted me koi bhi type ki value ko accending ya decending order me kar sakte he. sorted() ke use ke liye newlist must required he.
uske karan ye function original list safe rehti he.

reverse() : list me har ek elemnt ko right se left ki or likhna chahe tab reverse() ka use hota he.ye original list pr affect karega.

• Basic list manipulations: addition, deletion, updating, and slicing.
    addtion : hum list naya element add kar sakte he.uske liye append(),insert(),ya extend() ka use kar sakta he.
    deleteion : list me index se ya value se element ko kar skte he.
    updating : list me koi bhi element me indexx ka use kar ke update kar sakte he.
    slicing : list ko extract part ko acess kar sakte he.    
 """
# Write a Python program to iterate over a list using a for loop.
# acess all element
l1 = [5 , 7 , 2 , 8 , 1 , 3 , 9 , 4 , 6]
for i in l1 :
    print(i , end = " ")
print("")

# sort  
l1.sort()   # in accending order
print(l1)
l1.sort(reverse=True)  # in decending order
print(l1)

#sorted a list 
l1 = ["hirrn","milan","ketan","jatin","ritesh"]
l2 = sorted(l1)  #in accendin and decending
print(l2)
l3 =sorted(l1,reverse=True)  #i\ in decending order
print(l3)

 # Write a Python program to insert elements into an empty list using a for loop and append()
# l1 = []
# n = int(input("How much element enter  :"))
# for i in range(n+1) :
#     ele = input("enter ele")
#     if ele.isnumeric() :
#         ele = int(ele)
#         l1.append(ele)
#     else :
#         l1.append(ele)
# print(l2)

"""                                                   4. Tuple
Theory:

• Introduction to tuples, immutability.
        tuple ek collection datatype he jo har type ke data ko ek variable me store kar sakte he. isko round braces () likha jata he.
        tuple immutable datattype he. yani usme na to koi append or nahi  koi element remove kar sakte he.
         
• Creating  : tuple  ko create karne ke liye round brace me value likhenge.
              accessing  : tuple index based nvalue store kate he isiliye acess bhi index se karenge.
• Basic operations with tuples: 
    concatenation : Do tuple ko concaat karke ek naye tuple me concat kar sakte he. usme +(plus) oprater ka use hota he.
    repetition  : tuple me value ko repete karne ke liye repetation ka use karte he. isme *(estrict) oprater ka uese hota he.
    membership : koi element tuple me exsit karta he wo check karne ke liye in ka use karenge or 
                 tuple me exsist nahi karta wo check karne ke liye not in ka use karenge.

Lab Exercise :
"""
# Write a Python program to convert a list into a tuple.
l1 = ["python0 " , 15 , True , "java" , 3.14 , -45 , "98" ]  
t1 = tuple(l1)
print(t1)

# concatenate two tuples into one
t2 = ("flutter" , False , -24.25 , "True" , "91" , 25 )
t3 = t1 + t2
print(t3)

# access the value of the first index 
print(t3[0])

"""                                                     6. Dictionaries
Theory:
• Introduction to dictionaries: key-value pairs.
    dictionary ek coolecton he jo key oer value store karta he. dictionry ko hum {} curly braces me likkhte he. 
    dictionary mutable he. key jo duplicate nahi hoti jabki value duplicate ho sakti he.
     
• Accessing, adding, updating, and deleting dictionary elements.
Dictionary me index nahi hote uske karan usko acess , adding , update karna ho to key ka  use karenge.

• Dictionary methods like keys(), values(), and items().
Dictionery me keys() wo har ek keys  ko acess kar sakte he , value() key store har ek value ko acess karne ke liye 
or agar key or value dono ko acess karna ho to items() ka use karenge.

Lab:
• Write a Python program to create a dictionary with 6 key-value pairs.
• Write a Python program to access values using dictionary keys.
"""
di = { "Roll_No" : 12 ,"Name" : "Vinay" , "Course" : "Backend Developer" , "Grade" : "A" , "Marks" : 93 , "Percentage" : 97.25  }

for k , v in di.items() :
    print(k ,"=" ,v)


"""                                                      7. Working with Dictionaries
Theory:
• Iterating over a dictionary using loops.
        dictionary me key acess karne  ke liye only dictionary pr loop chalayenge. agar hume sirf value acees karni ho to dict_Name.values()
ka use karenge and dono ko eksathe acess karne ke liye hum dict_name.itens() pr loop chalayenge
• Merging two lists into a dictionary using loops or zip().
        Detail = ["name" , "course" , "Marks" , "prcentage"]
        Value = ["Kohli" , "python" , 67 , 45.73]
        di = dict(zip(Detail,Value))
        isme first Detsil ki list he wo key ke liye use hogi jab dusri value vali key ki value ki tarah store hogi.zip() function
    list 1 me se 1 element lega jisko wo key banayega uske bad second list me 1 element acess karega usko key me value ki targh 
    store karega. ese turn by turn key or value store karenge.
    
• Counting occurrences of characters in a string using dictionaries.
        s = "programming"
        count = {}

        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        print(count)

Lab:
• Write a Python program to update a value in a dictionary.
• Write a Python program to merge two lists into one dictionary using a loop.
Practical Examples: 15) Write a Python program to update a value at a particular key in a
dictionary. 16) Write a Python program to separate keys and values from a dictionary using
keys() and values() methods. 17) Write a Python program to convert two lists into one
dictionary using a for loop. 18) Write a Python program to count how many times each
character appears in a string"""


"""                                                    8. Functions
Theory:
• Defining functions in Python.
function ek block of code hota he jiska use jaroorat padne pr kar sakte he.
dunction reusability badhhata he . function ko def keyword se define hota he .
python me function ki defination likhi jati he jisme function ko kya work or kese karna he. uska code likha jata he.
function calling : jab bhi code ki jaroorat hoti he tab function ko call karengr.

• Different types of functions: with/without parameters, with/without return values.
 function ke four types he.
 with perameter without return  and with return: function ke perameter me value pass karnge lekin function kuch return nahi karega.
 jab with return vala value return karta he.
 without perameter without return and with return : function ke perametre me kuchh pass nahi karenege or wo return bhi nahi karega.
 jab wit return me vo value return karta he.

• Anonymous functions (lambda functions).
Lambda function ek without define name vala function he jisko single leine likhna hota he.lambda jab code ko chhota ,simple or readable ke karan use hota he.
lambda function ek single value return karga. isko lambda function se define kar sakte he.

Lab:
"""
# Write a Python program to print a string using a function
def strprint() :
    s = input("Enter string Value :")
    print(s)
strprint()

# a parameterized function that takes two arguments and prints their sum.
def sumOfNumber(x , y) :
    print(x+y)
a  =  int(input("enter number :")) 
b = int(input("enter number :"))
sumOfNumber(a,b)

#rite a Python program to create a lambda function with one expression.
a = lambda a : a*a 
print(a(5))

#a Python program to create a lambda function with two expressions.
res = lambda a , b: (a+b , a*b)
print(res(14,14))

"""                                                       9. Modules
Theory:
• Introduction to Python modules and importing modules.
        Moduales yani ek file josme code likha hota he .Ek modules file .py files hoti he.jisme bahot sare function , variable , 
class include hote he. us files ka use kar ke code ko short , readable banata he. modules ko use karne ke liye hum import keyword
ka use karke use kar sakte he.python me modules user-define or inbult dono hote he.
• Standard library modules: math, random.
        math or random jo python ki inbuilt library he.
        math library ka use mainly use math calculaton ke liye use hota he.complex calculation ko fast or simple karne ke liye bahot
jaroori he .jese ki square , power etc.random library ka use randome
 data genrate karne ke liye use hota he. random number , character ya fir humne di hui choice mese random  element nikalne ke liye.
• Creating custom modules.
        Custom modules se user khud apne modules banata he or usko use kar sakta he. modules me  variable , function , class hote he.
usko use karne ke liye import me file ka pthe or koi specific function ko use karna he to from me uska name likhenge. nahito * karke sab function
or class ka use kar sakte he.
"""
# Write a Python program to import the math module and use functions like sqrt(), ceil(),floor().
import math
# Value of Pi
print( math.pi)  #pi ==> 3.14
print(square(5))  # square of 5 ==> 25
print(ceil(50/3)) # above valu e==> 17
print(floor(50/3)) #below value ==> 16
print(sqrt(16)) # squre root of 16 ==> 4
print(pow(4))  #power of 4 ==> 16
print(factorial(5)) # factorial  of 5  ==> 120

# Write a Python program to generate random numbers using the random module.: 
import random
number = random.randint(1,100)
print(number)
