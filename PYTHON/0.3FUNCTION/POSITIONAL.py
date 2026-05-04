# positiona arguments and keyword arguments
#position argument
def myfun(name,score):
    print(f"name = {name}")
    print(f"score = {score}")
myfun("mustved",76)
myfun(77,'mustved')#hum jo value age likhenge to vo age vale paramiter mai save hoi name me 77 or score me mustved dikhayega

#keyword argument

myfun(name='mustved',score=50)
myfun(score=92,name='mustved')# isme kuch bhi farac nhi hoga name me name vali hi value dikhaye ga or score me score