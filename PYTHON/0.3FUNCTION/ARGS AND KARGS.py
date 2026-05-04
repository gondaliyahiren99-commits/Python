"""
args & kwargs:
~> args : argument: tuples as a parameter
~> kwargs : key with argument: dictionary as a parameter
"""

#args

def myfun(*val):
    print(val)
myfun("hiren",1 ,True, 3.14 , "python" , "53")


#args
def myfun(*val):
    ele=list(val)
    print(ele)
myfun(12,33,65,7,64,34,54,12,6,524,12,44,65,6,64,58,49,75)


#kwargs

def myfun(**a):
    for k,v in a.items():
        print(f"{k} = {v}")
    b=[]
    for k,v in a.items():
        b.append((k,v))
    num1,num2=zip(*b)
    print(num1)
    print(num2)
    print(b)
myfun(name='mustved',subject='python',score=67)