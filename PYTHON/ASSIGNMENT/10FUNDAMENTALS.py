from functools import reduce
"""                             *=*=*=*= 10. Advanced Python (map(), reduce(), filter(), Closures and Decorators) =*=*=*=*
# Theory:
• How functional programming works in Python.
    FUNCTION : Function is  block of code. that code is use again and again when we need.

                Syntax : def <FunctionName>():
                                statement

        1) Function Define :
         sabse pehle function define karna rehta he.
        usme function me kya task hoga  or kese hoga uska code likhenge.

        2) Function Call : 
        Function Define ke baad jab bhi hume code ki jaroorat ho 
        tab use call karte he .

        python me function declare ki jaroorat nahi.

                e.g. 

                        def printhello():         #(function defune)
                                print("Hello")

                        printhello()              #(function call)

         -->Output : Hello


# • Using map(), reduce(), and filter() functions for processing data.

1) map() : The map() function in Python is used to apply a function to every item of an iterable
 (like a list, tuple, etc.) and return a new result.
 
 syntax : map()
• Introduction to closures and decorators.
       Closures : Ek function apne outer function ke variables ko yaad rakhta hai, even after outer function khatam ho jaye.

                e.g. def outer():
                        x = 10
                        def inner():
                                print(x)
                        
                        return inner 

                    f = outer()

                    f()
2)filter : filter() function wo map ki tarah sequuence ke har ek  iterator pe work karega.
           filter function condion bassed work karta he.
           agar condion true hui to wo iterator ya uspe kiya gaya expresion return karega nahi to skip karega.

           e.g. 

                l1 =[1,2,3,4,5,6,7]

                l2=list(filter(lambda a :  a%2 ==0,l1))

                print(l2)


        -->Output : [2 , 4 , 6]

• Introduction to closures and decorators.

        Decoraters :
                Ek function jo dusre function ko perameter me leta he or return karta he uski value.

                Jab bhi hume function me extra functionality add karni ho tab  decoraters ka use karte he.

                e.g.   

                def message(myfun) :
                        print("Hello")
                        myfun()
                        print("good morning")

                @message
                def namemessage():
                        print("hiren")


        -->Output : Hello
                    Hiren
                    good morning

        Closures :

                function apne najik me jo bhi function ki variable ki value store kar sakta he he.

h=fun()
h()
                  
                

"""
#==============================================================Lab Exercise=============================================================
#==================================================================(1)==================================================================
#Write a Python program to apply the map() function to square a list of numbers. 
l1 = [15 , 34 , 24 , 12 , 22 , 18 , 19]
l2 = list(map(lambda a : a**2 ,l1))
print(l2)


# #==================================================================(2)==================================================================
# Write a Python program that uses reduce() to find the product of a list of numbers.
l1 = [1 , 2 , 3 , 4 , 5]
obs = reduce(lambda a,b:a*b,l1 )
print(obs)

#==================================================================(3)==================================================================
# Write a Python program that filters out even numbers using the filter() function.
l1 = [23 , 65 , 24 , 37 , 15 , 16 , 19 , 32 , 84]
l2 = list(filter(lambda a :a%2==0 , l1))
print(l2)

