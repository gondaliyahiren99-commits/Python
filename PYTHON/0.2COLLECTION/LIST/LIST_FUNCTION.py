l1 =[56,15,34,-89,98,3.14,55,78]   
#numeric number ke sath hi max min or sum work karega
#  if string  no accepted errr throgh karega
print("max :",max(l1))
print("min :",min(l1))
print("sum :",sum(l1))



l1 = [15,"45",78,-95,'hiren','python',True,3.25,"81"]
l1.reverse()
print("reverse :",l1)
print("reverse :",l1.reverse()) #print karenge to none return karega


l1 =[56,15,34,-89,98,-45,3.14,48.53,55,78] 
l2=[]
l2=l1.sort()  #hum dusre variable ka use karke usme add nahi kar sakte
print(f"simple : {l1}")
print(f"Sort : {l2}") #none 

l1.sort()   #for accending order
print(l1)


l1 =[56,15,34,-89,98,-45,3.14,48.53,55,78] 
l1.sort(reverse=True)   #for decending order
print(l1)


l1 = [1,5,4,2,-5,4,1,2,1,-5,5,2]
print(f"H much time repeat : {l1.count(1)}")


print(l1.index(5,+2))  # 5 jo dusri index pr he uska index batayega

l2 = l1
l2.append(45)
print(l1)
print(l2)
#45 he jo dono me add hoaga or remove karenge to done me se remove hoga


#solutution : copy()
l2 = l1.copy()
l2.append("hello")
#sirf l2 me append hoga

l2.remove("hello") #hello remove from l2
print(l2)
