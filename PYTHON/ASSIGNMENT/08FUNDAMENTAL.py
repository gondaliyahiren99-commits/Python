"""
********************************************************8. Control Statements (Break, Continue, Pass)************************************************

1)BREAK : break keyword use for stop loop  immediately, even if iterations are left.
            SYNTAX :
                    break

            e.g.   :
                for i in range(1 , 10) :
                    if i == 6 :
                        break
                    print(i , end = "")  
                    
        ~~>Output :  1  2   3  4   5
                    yaha per iteration 6 pr aate hi loop break hoga.age ke iteration pr jayega hi nahi.


2)CONTINUE : continue keyword use for skip the current iteration.
            and move next one.
            SYNTAX :
                    continue

            e.g.   :
                for i in range(1 , 10) :
                    if i == 6 :
                        continue
                    print(i , end = "")
         ~~>Output :  1  2  3  4  5  6  7  8  9
                    yaha pr jab iteration 6 pr ayega to wo skip karke wo aage ke iteration ko print karega.

"""


#==============================================================Lab Exercise=============================================================
#==================================================================(1)================================================================
#Write a Python program to skip 'banana' in a list using the continue
l1 =  ['apple', 'mango' , 'banana', 'grapes ' , 'cherry'] 
for i in l1 :
    if i == 'banana':
        continue
    else:
        print(i,end =" ")


#==================================================================(2)================================================================
#Write a Python program to stop the loop once 'banana' is found using
#the break statement.
l1 =  ['apple', 'mango' , 'banana', 'grapes ' , 'cherry']
for i in l1 :
    if i == "banana":
        break
    else:
        print(i , end = " ")