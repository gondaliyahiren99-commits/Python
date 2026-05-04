"""                                                                    
                                                     *=*=*=*= 5. Looping (For, While)  =*=*=*=*
Theory:
• Introduction to for and while loops.
1) FOR LOOP : for loop jo bhi itrable hota he uske har object ko acess karata he

        syntax:

                for <vairable> in sequence:
                    statement

        range() : range function is used to represent sequence
                range(start , stop , step )


2) while loop : Jab hume pata nahi hota ke loop kitne time chalana he tab while loop ko use karte he.
        while loop entry control loop he jo pehle condition check karega .
        agar conditiom true hogi to loop ka code execute
        will execute if condition gose false loop will tarminate.

            syntax:

                initlization
                while condition:
                    statement
                    updation (increment or dicrement)

#================================================================================================================================================

• How loops work in Python.

    FOR LOOP :
            step  : For loop is iterator-based . Wo list ,tuple ya string ke har ek object ko one by one acess karega.
            for loop se collection ki har ek element acess  kar sakte he.
            No need condition . 


    WHILE LOOP :
        step 1 : it s check condition
        step 2 : if condition is true . the code will be execute
        step 3 : after execution check comdition again
        step 4 : loop will stop when condition is false


#================================================================================================================================================

• Using loops with collections (lists, tuples, etc.).

    --> IN LIST :

            l1 = ['hiren' , 3.14 , 92 , True , 'B']

            for i in l1 :
                print(i, ,end = "")   # hiren 3.14 92 True B


    --> IN TUPLE :

            t = (1 , 'hiren' , True , 3.14 , ''A)

            for i in t :
                print(i , end = "")  # 1 hiren True 3.14 A


"""
#======================================================= Lab Exercise :  =============================================================
#============================================================(1)===================================================================
#Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']
l1 = ['apple' , 'banana' , 'grapes' , 'mango' , 'cherry']
for i in l1 :
    print(f"{i}",end = " ")
print("")


#============================================================(2)===================================================================
# Write a Python program to find the length of each string in List1.
l1 = ['apple' , 'banana' , 'grapes' , 'mango' , 'cherry']
l2=[]

for i in l1 :
    l2.append(f"{i} len is : {len(i)}")
print(l2)


#============================================================(3)===================================================================
#Write a Python program to find a specific string in the list using a simple for loop and if condition.
l1 = ['apple' , 'banana' , 'grapes' , 'mango' , 'cherry']
for i in range(len(l1)) :
    if l1[i] == 'grapes' :
        print(f"{l1[i]} index is {i} :")


#============================================================(4)===================================================================
# Print this pattern using nested for loop:
for i in range(1 , 6) :
    for j in range(i) :
        print(" * ",end = " ")
    print(" ")