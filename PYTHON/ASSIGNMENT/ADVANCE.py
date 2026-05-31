"""                                 >>>>>> Advance Python Programming<<<<<<<<<<<<
                                            1. Printing on Screen
Theory:
• Introduction to the print() function in Python.
    print ek inbuit function he. jisse consol me output dekhne ke liye print function ka use karenge.print ke perameter me agar koi string de  wo message print kar
    dega agar koi variable dege to vo variable ki value print karega and function kuch return kar raha he to perameter me function call kare to to function ki
    return value dega
• Formatting outputs using f-strings and format().
    Formating Outputs ke use se output ko atractive or readable dikhata he. jisme hum string me variable ki value  dikha sakte he.
    agar hum fstirng ka use kar rahe hee to f"{<Varialbe}" likhenge or format(variable1 , var2 ....varN) likh sakte he.
Lab:
"""
# Write a Python program to print a formatted string using print() and f-string. Practical Example:
name = "Hiren"
course = "python"
branch = "C. G. TopsTech"

print(f"my name is{name} course{course} at {branch}")   # my name is Hiren course is python at C. G. TopsTech
print("hello i am {} and my course is {}".format(name , course))

#1. Write a Python program to print “Hello, World!” on the screen."""
print("Hello")   # Hello


"""                                          2. Reading Data from Keyboard
Theory:
• Using the input() function to read user input from the keyboard.
    User ke hisab se jab value pass karni ho to input() ka use karenge.jisme variable ki value asign me input() denge or usme message print karenge.
• Converting user input into different data types (e.g., int, float, etc.).
    User hum input lenge to vo bydefult vo string me hi lega. agar dusre datatype me value chahiye to jis datatype ki value chahiye uske function me input function pass karenge.

Lab:
# Write a Python program to read a name and age from the user and print a formatted output. 
# Practical Example: 2) Write a Python program to read a string, an integer, and a float from the keyboard and display them."""
Name = input("Enter Name :")
Age =  int(input("Enter Age :"))
Percentage = 89.25
print("Name is {} and Age is {} or me {} percentage se pass hu 12th me ".format(Name , Age , Percentage) )


"""                                            3. Opening and Closing Files
Theory:
• Opening files in different modes ('r', 'w', 'a', 'r+', 'w+').
        file me read write or kuch update karne ke liye object banate time  hume uska mode likhna hota he .
    -->'r' Mode :- Fil agar Exsist he to ka data read karke koi variable store karte he or usko consol screen dikha sakte he.read mode hum r se definre kar sakte he.
    -->'w' Mode :- File agar exists nahi karti to w mode ka use karke usme kuch write kar sakte he or agar file pehle se hi exists he or w mode ka use karenge to purane data ko remove kar dega.jisko 'w' se define kiya jata he.
    -->'a' Mode :- agar file exists he or hume naya data uame add karan ho to hum w ka use nahi kar sakte jisse humara purana data remove ho jayega isiliye append mode ka use karte he. jisko 'a' se define karte he'.
    -->'r+' Mode :- jis file ko read and write karene ke liye use hota he.lekin agar file exists nahi he to wo error throgh kar sakta he.
    -->'w+' Mode :- isme bhi hum read and write kar sakte he agar file exists nahi he to new file create karega.
    -->'a+' Mode :- apend+write mode se hum file me write or append kar sakte he agar file exists nahi he to new file create kareg.

Lab:
• Write a Python program to open a file in write mode, write some text, and then close it.
Practical Example: 3) Write a Python program to create a file and write a string into it"""

f = open("Newfile.txt" ,'w') 
f.write("Hello, New file create  for example ")

f= open("Newfile.txt","r") 
data = f.read()
print(data)
f.close()

"""                                           4. Reading and Writing Files
Theory:
• Reading from a file using read(), readline(), readlines().
jab file read mode me ho to read kar ne ke liya alag alag method he.
    -->read() method se puri file ko hi hum console screen pr dikha sakte he.agar read method ke perameter value dege to utne character return kar dega.
    -->readline() method se file ki single line raed kar sakte he barbar readeline karne se har bar wo file ki next line deta he.
    -->readlines() method se puri file ko har ek line ko index ki tarah save karega. jiske karana puri file list me saved hogi. agar hume index se line acess karni ho to readlines ka use kar sakte he.

• Writing to a file using write() and writelines().
jab file 'w ' mode me ho to file me  write kar satkte he.agar file me kuch naya text write karna ho to write() ya writeline() ka use karenge.
write() se hu file me ek single word ya single string file me likhne ke liye use hota he.
agar ek se jyada string likhna ho to ye accept  nahi karega uske liye writeline() ka use se kar sakte he.jo multiple string ya word ko file me write karta he.
Lab  :    """
# L1.Write a Python program to read the contents of a file and print them on the console.
# l2.Write a Python program to write multiple strings into a file.
# L3.Write a Python program to check the current position of the file cursor using tell()
    
with open("sample.txt",'w') as f :
    f.write("Hello My name is hiren")
    print(f.tell()) # file ke cursor ki current position batata he.
  
with open("sample.txt",'r') as f :
    data = f.read()
    print(data)


"""                                               5. Exception Handling
Theory:
• Introduction to exceptions and how to handle them using try, except, and finally.
        Jab programer ko koi code ke part risky lage yani ki error ane ki posibility ho tab programer pura programe crash na ho agar error aye to ek mesage de or programe smoothly run ho uske liye exception handling jaroori he.
        try ye exception handling ka wo part he jisme programer jo risky code ho usme likhta he. agar try vale part me error to wo execpt part me jayega. waha programer koi message deta he console me ki kya error he.finaly vale part me likha code always run karega. agar try or except me return statement he to bhi finale vala run karega,jab
        koi simple stament return ke bad run nahi hota.  
• Understanding multiple exceptions and custom exceptions.
    programe me alag alag type ki error atit he.jab humne multiple except part diye ho or multiple error likhi ho to jis type ki error ho us hisab se except vala part execute hoga.
    custom exception jab programer khudki error banata he.use custom exception kehte he.jisme class ka use karnge aur jab bhi error bulana ho to raise keyword se class ka name likhe to error raise hogi.
Lab:
Practical Examples: 7) Write a Python program to handle exceptions in a calculator. 8)
Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
9) Write a Python program to handle file exceptions and use the finally block for closing
the file. 10) Write a Python program to print custom exceptions."""

try :
    number1 = int(input("Enter Number :"))
    number2 = int(input("Enter Number :"))

    op = input("Enter Oprater :")
    if op == "+":
        print(number1+number2)
    elif op=="-":
        print(number1-number2)
    elif op=="*":
        print(number1*number2)
    elif op=="/":
        print(number1/number2)
    else:
        print("invalid....!")
except ZeroDivisionError :
    print("0 ke siva koi bhi value enter karo....")
except ValueError :
    print("Only Number can input.....")
finally :
    print("always run")



"""                                         6. Class and Object (OOP Concepts)
Theory:
• Understanding the concepts of classes, objects, attributes, and methods in Python.
• Difference between local and global variables.
Lab:
• Write a Python program to create a class and access its properties using an object.
Practical Examples: 11) Write a Python program to create a class and access the properties
of the class using an object. 12) Write a Python program to demonstrate the use of local and
global variables in a class."""
class Sample:
    Name = "Hiren"
    def display(self,course):
        self.couse = course
        print(self.Name)
        print(self.course)

obj = Sample()
print(obj.display("python"))

"""
                                                 7. Inheritance
Theory:
• Single, Multilevel, Multiple, Hierarchical, and Hybrid inheritance in Python.
    imheritace yani jab koi parent class apni property ka acess child class ko de usko inheit bolte he.
    -->sigle() : koi ek parent koi ek child ko acess de to wo single inheritance he,
    -->Multiple() : jab koi child ek se jyada parent ke pass se property ka acess le to us multiple       inheritance he.
     -->Multiple(): Jab koi class koi base class ko inherit kare or base class sub class ko inherit kare usko Multiple inherit kehte he. jisme sub class hota he wo dono  ke acess le sakte he.
     -->Hierarchical : koi ek parent mutiple child ko property acess de usko Hierarchical kehte he.jisme dono class parent ki property use kar sakte he.
     -->Hybrid : jisme Hierarchicle or mutiple k a combine hota he.
     koi parent class ek se jyada child class ko acess deta he and child class uske child class ko acess dega
     
• Using the super() function to access properties of the parent class.
    parent class aur child class me same method use ho to parent class ka method access ke liye super() ka use kiya jata he.agar super() ka use na kare to child class parent claass ko acess nahi kar sakta.agar super() ka use na kare to parent class ka specific name likh ke acces karna padta he.
Lab:
• Write Python programs to demonstrate different types of inheritance (single, multiple,
multilevel, etc.).

"""
# SINGLE  INGERITANCE
class Parent :
    def display(self) :
        print("parent class")

class Child(Parent):
    pass

c = Child()
c.display()

# MULTIPLE INHERITANCE
class Parent1 :
    def display1(self):
        print("parent 1 class")

class Parent2 :
    def display2(self):
        print("parent 2 class")

class Child(Parent1 , Parent2):
    pass

c = Child()
c.display1()
c.display2()


# MULTILEVEL INHERITANCE
class Class_Main():
    def display1(self):
        print("This  main class")

class Base_Class(Class_Main) :
    def display2(self):
        print("This is base class")

class Sub_class(Base_Class):
    pass

s = Sub_class()
s.display1()

# HIERARCHICAL INHERITANCE
class Parent_Class :
    def p_display(self):
        print("This is parent 1 Class") 

class Child1(Parent_Class):
    pass

class Child2(Parent_Class):
    pass

c1 = Child1()
c2 = Child2()

c1.p_display()
c2.p_display()

# HIBRID INHERITANCE
class A :
    def __init__(self,name) :
        self.name = name 
    
class B(A) :
    B_age = 23
    def displayB(self):
        print(self.name)
    
class C(A):
    C_course= "python"
    def displayC(self):
        print(self.name)

class D(B,C) :
    def displayD(self):
        print(self.name)
        print(self.B_age)
        print(self.C_course)
d = D("Hiren")
d.displayB()


"""                                                  8. Method Overloading and Overriding
Theory:
• Method overloading: defining multiple methods with the same name but different parameters.
    do se jyada class me same name ke function or usme differnt perameter ho to wo function overloading he.lekin ye python me directly support nahi karta 
• Method overriding: redefining a parent class method in the child class.
    jab parent class or child class me same name ki  nethod use kare ,to call karne se wo tabwo huemsh  child ka method dega . tabhi usi ka solutiion ke lye
Lab:
• Write Python programs to demonstrate method overloading and method overriding.
Practical Examples: 19) Write a Python program to show method overloading. 20) Write a
Python program to show method overriding."""
# METHOD OVERLOADING
class Add :
    def TotalSumm(self ,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        return self.a+self.b+self.c
    
a = Add()
print(a.TotalSumm(15))
print(a.TotalSumm(15,15))
print(a.TotalSumm(15,15,15))

# METHOD OVERRIDING
class A :
    def display(self) :
        print("A CLASS HEAR")
    
class B(A) :
    def display(self):
        super().display(self)
        print("B CLASS HEAR")
    
b = B()
b.display()

"""                                                    9. SQLite3 and PyMySQL (Database Connectors)
Theory:
• Introduction to SQLite3 and PyMySQL for database connectivity.
SQLlite3 python ka inbuilt databse he . isme alaag se databse server uinstall karne ki jaroorat nahi he.isko easy use kar sakte he. ise lightweight database bhi kehte he. ye small application aur testing ke liye use hota he.
PyMySQL python ka MySQL databae se conncet karne ke liye use hota he. ye MySQL ke srver ke sath kaam karta he.
• Creating and executing SQL queries from Python using these connectors.
~~>  sabse pehle connection create karte he.concetion ke bad curser declare karte he . bad me SQL ki query likhte jisko cursor se execute karte he.agar naya data dala he to usko con ke use database me save kar dege.
Lab:"""
#Write a Python program to connect to an SQLite3 database, create a table, insert data, and
# fetch data.

import pymysql
con =pymysql.connect(host="localhost",
user ="root",
password="root")
cursor=con.cursor()
cursor.execute(' create database if not exists my_dbms')
print("succefully")
con.commit()
con.close()
con =pymysql.connect(host="localhost",
user ="root",
password="root",
database="my_dbms")
c = con.cursor()
c.execute("create table if not exists student(id int, name varchar(20),subject varchar(20))")
con.commit()
con.close()

con =pymysql.connect(host="localhost",
user ="root",
password="root",
database="my_dbms")
c = con.cursor()
q=("insert into student(id,name,subject) values(%s,%s,%s)")
args =(101,"Jecob","python")
c.execute(q,args)
con.commit()
con.close()
"""                                 10. Search and Match Functions
Theory:
• Using re.search() and re.match() functions in Python’s re module for pattern
re ek modual he . jo string me pattrn search karne lke liye use hota he. jisme seach() or match() do function he. jisse strtring me koi bhi word ko search kar sakte he.search() jo puri string me se word ko search karta he jab ki match() jo sirf string ki starting position me hi word ko searh karta he.e.g. 
        import re
        stringg= "python is programing language"
        re.match(r"python",stringg)   #  match
        re.match(r"language",stringg) # not match
        re.search(r"language",stringg) #  match
        re.search(r"programing",stringg) #  match
    
matching.
• Difference between search and match.
        re.search jo puri ki puri string me se me word find kar sakata he jab ki re.match() wo sirf starting position me word he ya nhi wahi check karega.
"""