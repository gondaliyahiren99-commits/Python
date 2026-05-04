"""

                                                  =*=*=*=*2. Programming Style  =*=*=*=
Theory:

• Understanding Python PEP 8 guidelines.
PEP  8 giidline use to make code clean, readable, and consistent for all developers.
It helps in better teamwork, easier debugging, and maintaining code efficiently.

1)Indantation :
    indantation mean adding space at begining of line to define block of code.
    Use 4 Space at line starting or Tabs
    indantation mostlyu use in condion,Loop ,Function ,class to define block of code.
    e.g name="hiren"
        if type(name)==str:
            print("string")

    must add in syntax(else error): 
        if type(name)==str:
        print("string")

2)Line Length :
    Maximum 79 characters per line
    If code characters more than 79 Break long lines using \ or parentheses
    total = (price * quantity +
            tax_amount)
    

    or
    total = price * quantity +\
            tax_amount

3)Naming Convation :
    Naming Conventions mean giving meaningful and consistent names to variables,functions,classes,etc.
    So the code is easy to read and understand.
    -Variable Name :
        kisi ka price stor karna he to variable x ki jagah price or lowercase me.
        e.g. price=500
    -Function Name : 
        Function he wo kis kaam ke liye use kiya he jeseki Marks ka Average Ke liye short and meanigful 
        or lowercase me
        e.g. marks_avg()
    -Class Name : 
        Class me kya store he uske hisab se pr Name pascalcase me hona chahiye
        e.g. Class StudentDetails
    -Constant value :
        Agar koi constant Value he to usko Upercase me likhenge
        e.g. PI=3.14

4)Whitespace :
    All Token after use whitespace
    x = 15

5)Import Use:
    Put on top
    One import per line
    Top Order :     
                -Standerd Library
                -Third-party libraries
                -Local imports

6) Comments :
    Use Comment clear for code information and Readable and Understable for other and teamworker
    # Simple Intrest
    si = (p * r * n)/100

7)Blank Lines:
    Use 2 blank lines before functions/classes
    Use 1 blank line inside functions (if needed)

8) Use is :
    in_word = True
    if in_word == True #its bad

    if inword is True : # No compare of boolean Value


* Indentation, comments, and naming conventions in Python
Indantation :
        Indantation means define block of code 
        python me block of code ka use nahi hota isiliye jab bhi hum statment ko block of code me likhna chahe tab use hota he.
        ye tab ya fir 4 space se indantation creat karte he
        e.g.
        if age>18:
            print("Eligible")
            print("Go for Vote")
        print("You can drive ")

        isme jaha pr indantation he wo if ke anadar he baki sab condition ke bahar
        agar condition false hui to bhi condition ke bahar ka statment execute hoga


Comment :
        Comment mean information of code so enyone can understand the code
        interpreter not execute this line
        Two types Of Comment :
        1) One-Line :
            Use for one line 
            it's Represent by #
            e.g.    
                    # This is comment

        2)Multiple-Line:
            Use for Multiple Line
            it's represent by three Quotes
            e.g.
                    "/"/"
                    This 
                    is 
                    Multiple Line comment 
                    "/"/"


Naming Conventions :
       Naming Conventions mean giving meaningful and consistent names to variables,functions,classes,etc.
       So the code is easy to read and understand.
            -Variable Name :
                    kisi ka price stor karna he to variable x ki jagah price or lowercase me.
                    e.g. price=500
            -Function Name : 
                    Function he wo kis kaam ke liye use kiya he jeseki Marks ka Average Ke liye short and meanigful 
                    or lowercase me
                    e.g. marks_avg()
            -Class Name : 
                    Class me kya store he uske hisab se pr Name pascalcase me hona chahiye
                    e.g. Class StudentDetails
            -Constant value :
                    Agar koi constant Value he to usko Upercase me likhenge
                    e.g. PI=3.14
"""
"""
Lab Exercise :
Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guide
"""
#sum of 1 to N Number
def SumOfNumber(n):
    total_sum = 0    #varibale declare
    for i in range(1 ,n) :
         total_sum += i

    print( total_sum)

number = int(input("Enter Number : "))
SumOfNumber(number)