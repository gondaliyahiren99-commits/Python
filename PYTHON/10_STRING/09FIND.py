s1 = "hiren@gmail.com"

print(s1.find("@"))#index value return karega -->5

if "@" in s1 and "." in s1:
    print("valid")
else:
    print("invalid email!")




name="a b c d e o p e d w a s t a b e"
print(name.find("a")) #0
'''
{ye frst a kaha pe hai uska index btayega par aga mujhe jann ahai ki dusra (a) kaha pe hai to 
first vale ki jo index iyi hogi mughe uski ek plus kar ke likhna hoga jese agar first a 0 
position pe hai to mujhe find("a",+1) likhna hoga agar mujhe janna hai ki third (a) kaha pe hai 
to sem second ka jo index aya hai uska ek plus kar ke likhna hoga }

'''

print(name.find("a",+1))#20
# third a
print(name.find("a",+21))#26
#or hoga to 27 likh ke vo bhi pta chal jaye ga agar nhi hoga to -1 likha aye ga 
print(name.find("a",+27))#-1
         
                                        
'''                                         _______________________________
        NOTE:                              |esa hi index() me bhi hota hai|
                                           -------------------------------
'''
