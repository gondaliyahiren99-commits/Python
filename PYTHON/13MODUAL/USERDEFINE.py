def findfact(num):
    f=1
    for i in range(num+1):
        f*=1

    return f

def CheckEven(num):
    if num%2==0:
        print("Even")
    else:
        print("odd")