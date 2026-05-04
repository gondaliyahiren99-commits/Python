#jiski len 4 se jyada ho vhi save ho
l1=['java','python','flutter','Ai','php','android']
def myfun(num):
    if len(num)>4:
        return num
l2=list(filter(myfun,l1))
print(f"{l1}\n{l2}")



l3=list(filter(lambda nam: len(nam)>4,l1))
print(l3)