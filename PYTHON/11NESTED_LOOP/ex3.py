
for i in range(6):
    for j in range(i):#i ka first 0 hoga and j ka bhi first 0 hoga to first vala nhi jaega ander 0=0 X
        print("*",end="")
    print()

    """output-->
*
**
***
****
*****
      """  
for row in  range(1,6):
    for col in range(row):
            print(" * ",end=" ")
    print()
"""
 *  
 *   *  
 *   *   *
 *   *   *   *
 *   *   *   *   *
"""
for row in  range(1,6):
    for col in range(row):
            print(f"{col}",end=" ")
    print()
"""
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
"""
for row in  range(1,6):
    for col in range(row):
            print(f"{row}",end=" ")
    print()

"""
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4

"""

for row in  range(1,6):
    for col in range(row):
            print(f"{col+1}",end=" ")
    print()
"""
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4

"""

    

num=0
for i  in range(5):
        for j in range(i):
                num+=1
                print(num,end=" ")
        print()



"""
1
2 3
4 5 6
7 8 9 10
11121314 15

"""