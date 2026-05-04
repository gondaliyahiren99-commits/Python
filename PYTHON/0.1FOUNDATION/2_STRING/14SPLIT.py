"""
splite()

syntax:-
    string_name=var.splite()
"""
name="im hiren"
print(len(name))#10
print(name.split())#['im', 'hiren']

name=name.split()
print(name)#['im', 'hiren']
print(len(name))#2


n1,n2=name#['im', 'hiren'] isne dono ko alag alag vareable mai split kar diya  
print(n1)#im
print(n2)#hiren

name="python@java"
n1,n2=name.split("@")# agar hum isme kuch nhi likhenge to ye space se split kar dega 
print(n1)#python
print(n2)#java