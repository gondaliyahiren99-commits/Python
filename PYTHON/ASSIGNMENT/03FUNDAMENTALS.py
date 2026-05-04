"""                                                      
                                        =*=*=*=Core Python Concept =*=*=*=

• Understanding data types: integers, floats, strings, lists, tuples, dictionaries, sets.
Ans :
Data type :- A data type defines which type of value  store in a variable.
            Mainly Three type of Variable
            1) Numeric :
                 (A) int : Which Number is store whole number 
                            e.g. 
                            age = 26
                 (B) float : which variable a store decimal number 
                            e.g.
                            percente = 92.56
                
            2) String : String type datatype always write in quotes
                (A) str : A variable store collction of character 
                            e.g
                            Name = "Hiren"
                (B) char : A variable store a single character 
                            e,g.
                            Grade = 'a'
            
            3) bool : boolen for True or False value store
                            e.g.
                            Flag = True

            4) list : A variable can store multiple type value is represent by [] braces
                    List is mutable ,indexeble variable .jisme hum add ya remove kar sakte he
                    List me duplicate value bhi allowed he
                    syntax : 
                        list_name = [var1 , val2 , val3 , ....valn]

                    e.g.
                    li = ["python" , 25 , "python", 3.14,"cpp", True]
                    
            5) Tuple : A varibaale can store multiple value 
                    Tuple is represent by () peranrheses.
                    Tuple is immutable. means hum tuple me add ya remove nahi kr sakte
                    Tuple Don't allow duplicate value allow
                    syntax : 
                        tuple_name = (val1 , val2 , val3 .......valn)
                    e.g. 
                    t = ('hiren', 18 , 37.5 , False)

            6) set : A varibaale can store multiple value . it's represenrt by {} braces.
                    set not allow duplicate value
                    set is immutable means hum set me element add ya remove naho kar sakte
                    syntax :
                        set_name = {val1. , val2 , val3....valn}
                    e.g.
                    s = {'hiren', 21 ,3.14 ,"python",True}

            7) Dictionary : dictionary in store key and value.
                    Dictionary represent by {} braces.
                    value can duplicate
                    key not duplicate allowed
                    syntax : 
                    dictionary_name = {key1 : val1 , key2 : val2 , key3 : val3......keyn :valn}
                    e.g.
                    d = {'name' : hiren , 'course' : 'python' , 'city' : 'Ahemdabad'}

 • Python operators: arithmetic, comparison, logical, bitwise.
      OPRATERS :-
        To parform spacific operations we have to use some spacific symbols its called Operators
        And to porform operations between operands

        e.g.
        a + b
        hear a and b is operands and + is Operators.

        1) Airthmetic Operator:
                + , - , * , / , //(floro division) , **(exponentiation)
                its return a value
                e.g. 
                a,b = 10,5
                ans = a + b  | 10 + 5  | 15
                ++++++++++++++++++++++++++++++++++++
                ans = a - b  | 10 - 5  | 5
                ++++++++++++++++++++++++++++++++++++
                ans = a * b  | 10 * 5  |  50
                +++++++++++++++++++++++++++++++++++++
                ans = a / b  | 10 / 5  |  2.0
                +++++++++++++++++++++++++++++++++++++
                ans = a // b  | 10 // 5  |  2
                +++++++++++++++++++++++++++++++++++++
                ans = a ** b  | 10 ** 3  |  1000
                +++++++++++++++++++++++++++++++++++++


        2) Assigment operators:
                = (to assign a values)
                Variable me value assign karne ke liye.

            *shorthand operator: combination of airthmatic and assigmnet operator.isme left side me jo bhi variable ki value me 
            expressin work karke usme hi value assign hogi.
            ( += , -+ , *= , /+ , //+ , **= )
            e.g
                    a,b = 10,5
                a = a += b  | a += 5  | 15
                ++++++++++++++++++++++++++++++++++++
                a = a -= b  | a -= 5  | 5
                ++++++++++++++++++++++++++++++++++++
                a = a *= b  | a *= 5  |  50
                +++++++++++++++++++++++++++++++++++++
                a = a /= b  | a /= 5  |  2.0
                +++++++++++++++++++++++++++++++++++++
                a = a //= b  | a //= 5  |  2
                +++++++++++++++++++++++++++++++++++++
                a = a **= b  | a **= 3  |  1000
                +++++++++++++++++++++++++++++++++++++
            

        3) Relational operators:
            Relation oprater do value ko compre karne ke liye use hota he . its return always boolean value. wo sirf True or False return krta he.
            < > <= >= == !=
            e.g.
            a,b = 10,5
        
                 ans = a > b  | 10 > 5  |   True
                ++++++++++++++++++++++++++++++++++++
                ans = a < b   | 10 < 5  |   False
                ++++++++++++++++++++++++++++++++++++
                ans = a >= b  | 10 >= 5  |   True
                ++++++++++++++++++++++++++++++++++++
                ans = a <= b  | 10 <= 5  |   False
                ++++++++++++++++++++++++++++++++++++
                ans = a == b  | 10 == 5  |   False
                +++++++++++++++++++++++++++++++++++++
                ans = a != b  | 10 != 10  |   False
                +++++++++++++++++++++++++++++++++++++


        (4) Logical operator: 
                condition ko jodne ke liye use hota he.
                relation and logical combination 
            and : Must both condition are true
            or  : at least one condition are  true
            not :  opposite result


             a,b = 10,5
                 ans = a > b and  a!=b | 10 > 5 and 10 != 5 |    True
                +++++++++++++++++++++++|++++++++++++++++++++|+++++++
                ans = a < b  or  a > b | 10 < 5   or 10 > 5 |    True
                +++++++++++++++++++++++|++++++++++++++++++++|+++++++++
                ans =( not (a >= b )   |    !(10 > 5)       |    True
                +++++++++++++++++++++++|++++++++++++++++++++|++++++++
              
        (5) Membership operator:
           # in

            Name = "Hiren"
            if r in Name :
                print("yes")

            else : 
                print("Not")

        ~~>Output : Yes

         # not in

         Name = "Hiren"
         if n not in Name :
                print("yes")
         else :
                print("Not")

        ~~>Output : Yes
       
 • Python variables and memory allocation.
        python me memory allocate karne ki jaroorat nahi padta.
        yani agar ek variable me koi value add he or dusre varible ki memory ke compare me memory kam  he to usme dusri value add 
        karne ke liye hume memory free nahi karni padti.
        e.g.
        a = 15
        a = "hello"
        No need to  free memory
"""
#====================================================================================================================================

#======================================================= Lab Exercise :  =============================================================
#============================================================(1)===================================================================
#: Write a Python program to demonstrate the creation of variables and different data types.
name = "hiren"
marks = 92
percentage = 96.75
is_eligible = True
grade = 'A'
Marks_list = [95 , 73 , 86 , 59 , 67 ]
Acct_info = { 'name ' : "hiren",
              'ac no ' : 122456,
              'branch' : 'paldi'  }
print(f" name is : {name} and type is a : {type(name)}\n")  #name = hiren type = str
print(f" percentage is : {percentage} and type is a : {type(percentage)}\n") #percentage = 96.75  type = float
print(f" is elgible for vaote  is : {is_eligible} and type is a : {type(is_eligible)}\n") #is_eligible = True type = bool
print(f" grade  is : {grade} and type is a : {type(grade)}\n\n") # grade = 'A' type = chr
print(f" marks of five subject is : {Marks_list} and type is a : {type(Marks_list)}\n") #Marks_list = [95 , 73 , 86 , 59 , 67 ]  type = list
print(f" account info is : {Acct_info} and type is a : {type(Acct_info)}\n") #Acct_info = { 'name ' : "hiren",'ac no ' : 122456, 'branch' : 'paldi'  } type =dict


#=============================================================(2)=======================================================================

#(2) : How to create variables in Python?
#In python when we creat variable then lef side write variable name and right side write value of variable.
#e.g.
#syntax : 
#          variable_name = value
mo_number = 231552 #int variable
bank_name =  'bank of baroda' #string variable
balance = 25154.23  #float variable
is_customer = True #boolean variable



#==================================================================(3)==================================================================
# : How to take user input using the input() function 
# syntax :
#      variable_name  = input("messsage")
#      input() by defult string value store ;


name = input("Enter name :") #"hiren"
num = input("enter Number :") # "156"  (by default always string valuse store solution is typcast)

#string store na kare uske liye typcast jaroori he
# syntax :
#       variable_name  =  int(input("messsage"));
num1 = int(input("enter Number :")) # 156 (typcast so no store a string value)
weight = float(input("enter Float Number :")) # 52.37 


#=======================================================================(4)=============================================================

#(4) :How to check the type of a variable dynamically using type().
 #in python type check by type function
 #      syntax :
 #            type(variable_name)

name = 'hiren'
grade = 'A'
marks = 96
percentage = 95.12

print(f" name type is : {type(name)}")   #str
print(f" grade type is : {type(grade)}")  #chr
print(f" marks type is : {type(marks)}")  #int
print(f" percentage type is : {type(percentage)}") #float



#====================================================================================================================================