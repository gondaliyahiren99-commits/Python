"""
QUE  3: WRITE A FUNCTION THAT ACCEPTS A LIST OF NUMBERS AND RETURNS THE SUM OF ALL EVEN NUMBERS IN THE LIST.
"""

from functools  import reduce
def sumoflist(l):
    l=reduce(lambda a ,b : a+b,l)
    print(l)
sumoflist([1,2,3,4,5,6,4])
