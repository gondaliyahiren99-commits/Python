#map function jo condition vali value true hogi to save karega but 
#flase me bhi vo none save karega

l1=['java','python','php','ai','flutter']
def myfun(name):
    if len(name)>4:
        return name
    else:
        return  None

l2=list(map(myfun,l1))
print(f"{l1}\n{l2}")