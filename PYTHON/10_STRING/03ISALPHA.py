s1 = "python"

if s1.isalpha():
    print("Valid")
else:
    print("Not valid :")
#output--> valid


s2 = "python123"

if s2.isalpha():
    print("Valid")
else:
    print("Not valid :")
#output--> Not valid


name =input("Enter Name :").isalpha()
print(name)
#yaha sirf tru or false return karega 

"""

    #===============================================:alpha:====================================================
    var.isalpha() 
    when string in only store alphabet tab true karega otherwise false karega

    ye sirf alphabet ko true karega 
     when true:-
     -alphabet
     -No Number
     -No Space 
     -No special character


"""        
                                                                                       
name="hiren"
print(name)
print(name.isalpha())#true
#--------------------------------------
name="hiren@gmail.com"# yaha pr @ hone ke karam false return karega 
print(name)
print(name.isalpha())#false
#--------------------------------------

name=input("enter your name:").isalpha()
print(name)#true or false
print("=======================================")



name="hirengondaliya"
for i in range(len(name)):
    if i.isalpha:
        flag=1
    else:
        flag=0

if flag==1:
    print("ok")
else:
    print("no")
"""
=================================================:numbers:==================================================
 var.isnumeric() 
 when string store only number then return is true 

when true :-
-sting in only Digit store
-No alphabet
-No Space 
-No special character
-No Nagative (Only posistive) #kyunki wo string me hone ke karan (-) ko char ki tarah dekhega na ki minus 
"""               
# same as alphabet there is store alphabet here is only nuber
number="12345123"
print(number)
print(number.isnumeric())#true
#--------------------------------------
number="12-3-45_672"# kyunki wo string me hone ke karan (-) ko char ki tarah dekhega na ki minus 
            
print(number)
print(number.isnumeric())#false
#--------------------------------------

number=input("enter your number:").isnumeric()
print(number)#true or false

print("-----------------------------------")

name=input("enter a name:".upper())
if name.isalpha():
    print("name is alpha=",name)
elif name.isnumeric():
    print("name is numbers=",name)
else:
    print("mix name.")
"""
=======================================================:isalnum():=========================================
when  string in both are include Number and Alphabet 

when True:-
-No spacial character
-No space
-Number in string
-alphabet
                                                    
"""

name1="Hiren"
name2="123456"
name3="hiren4545"
name4="hiren 12"
name5="hiren@123"
print(name1.isalpha())#True
print(name2.isalnum())#True
print(name3.isalnum())#True
print(name4.isalnum())#False
print(name5.isalnum())#False


