with open("hii.txt","r") as f :
    s=f.read()
    print(s)

with open("hii.txt","r") as f :
    print(f.readlines())  #sab line read as a list
    j=f.read()
    print(j)
#one time pr sab line read hone ke bad file close ho jati he isiliye 
#second time kuchh print nahi hota
# with open("hii.txt","r") as f :
#     print(f.readline(10)) 
#     #agar perameter me kuch dede to wo utne character 
#     #return karega
#     print(f.readline(10)) 
#     print(f.readline(10))
#['hello my name is hiren\n', 'welcome to python1\n', 'my name is hiren2']    
"""hello my n (first time readline call)
ame is hir    (second time readline call)
en             (third time readline call)       
 means file one time pe ek hi read karta he bad e wo remain pe chalta he cursor ki tarah
 isiliye age ke function readlines ke call ke time print nahi kar raha

   """         

f = open("hii.txt","r") 
print(len(f.readlines()))


#txt file ki sr no wo index hoti he isiliye index se print
f = open("hii.txt","r") 
print(f.readlines()[1])