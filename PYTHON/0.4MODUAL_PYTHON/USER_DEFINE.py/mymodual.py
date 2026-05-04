def fac(num):
    f=1
    for i in range(1,num+1):
        f*=i
    return f
def even_odd(num):
    if num%2==0:
        return 'even'
    else:
         return 'odd'