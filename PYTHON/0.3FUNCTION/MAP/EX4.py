#sub dictionary ka key or value l2 me save kiya 
d={'student1':{'name':'mustvde','score':67,'subject':'python'},
   'student2':{'name':'aaa','score':50,'subject':'java'},
   'student3':{'name':'bbb','score':78,'subject':'php'},
   'student4':{'name':'ccc','score':93,'subject':'flutter'}
}
l1=list(map(lambda num: num,d.values()))
print(l1)
l2=[]
for i in l1:
    for j in i:
        l2.append(j)
print(l2)