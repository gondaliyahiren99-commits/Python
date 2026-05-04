import my_module as my

print(my.fac(5))
print(my.even_odd(5))

#or
import my_module 
print(my_module.fac(4))

#or
from my_module import fac,even_odd
print(fac(5))
print(even_odd(6))