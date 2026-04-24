"""

*args : argument : tuple as perameter

**kwargs : key with arguments : dict is perameter

"""

def myfun(*args):
    for i in args:
        print(i)

myfun(12,25,14,35,"hiren")


