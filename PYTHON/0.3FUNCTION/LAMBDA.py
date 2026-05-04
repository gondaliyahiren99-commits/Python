"""lambda function :
~> lambda function is a anonymous function
~> function without any name it's called lambda function
~> using of lambda keyword we can difine lambda function

    syntax:
        var=lambda <parameter>: expresion
~> lambda function can access as many as parameter nut can return single expresion
"""

# without lambda function
def myfun(num):
    ans=num+num
    return ans
number=int(input("enter your number :"))
print(myfun(number))

# with lambda function
ans=lambda num: num+num

ans=lambda num: f'{num} is positiv' if num>0 else f'{num} is negetive'
print(ans(-1))#-1 is negetive

ok=lambda num: num%2==0# ok me true or false save hoga 
print(ok(number))