
"""
solution :

type casting :
        convert to one data type into another datatype its called type casting

        e.g. int(value),
        string(value),
        float(value),

"""
num1 = input("Enter number 1 :")
num2 = input("Enter number 2 :")

ans = num1 + num2

print(ans)

'''
prblem 
enter number 1:4
enter nuber 2: 6
 --->output  46
 yaha par addition ki jagah concat ho raha he

'''
#soolution 
# 1)
print("====================")
#isme varible ko typcast karke dusre me store kar do
n1=int(num1)
n2=int(num2)
print(n1+n2)
 
#solution 
# 2)
#declare ke time hi variablr ko datatype de denge ki tarah store karenge
n1 = int(input(("Enter number 1 : ")))
n2 = int(input(("Enter number  2 : ")))

ans = n1 + n2

print(ans)


'''
-->output 
        enter n1 : 4
        enter n2 : 6
                        -->10   (now its addition)
                        
'''

"""
jab string ka bool me typcast karenge tab 


 empty string or agar string ki length more than 0 he to True ayega 

nahi  to False
"""
Name=""
print(bool(Name)) #empty string False

Name="False"
print(bool(Name)) #empty nahi he to true ayega