"""

                                             *=*=*= 6. Generators and Iterators =*=*=

Theory:






• Understanding how generators work in Python.

    Genrator : 
        genrator is a special type of function.
        which is genrate some state of value and store in a place and return as per the requirement. returns values one by one 
        return ki jagah yeild keyword use hota he.

        When next() is called:
        function jo value yeild me hogi wo return karega.
        ab wo apna position save kar lega.

        Next next() call:
        resumes from where it stopped
        remembers its state between calls

        normal function perform any opration and return value but genrator does not return 
        it just store value and save satatement and return using of yeid keyword.

• Different beetwen return and yeild :

    yeild value store kar ke rakhta he jabki return store nahi karega.
    yeild har bar call pr next value return karega or return pehli value pr hi return ho jayega.Dusre return statement ko ignore karega

• Understanding iterators and creating custom iterators.
    itrator wo har ek element pr one by one jata he.
    one time pe ek hi memory store karta he.
    apni position yad rakhta he .
    
"""
#Write a generator function that generates the first 10 even numbers.
def genrat_num(n):
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10

obj = genrat_num(n=1)
print(next(obj))


#• Write a Python program that uses a custom iterator to iterate over a list of integers

l1 = [15,16,24,18,19]

obj = iter(l1)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
