"""" by default loop will start from 0 to 4
range(start, end ,step)
agar  start nahi denge to start 0 lega

"""

for i in range(5):#
    print(i)

print()#for new line

for i in range(1,7):#: hear 1 is start point and 6 is end point loop will run total 5 time
                    #1 2  3  4  5(6 ko include nahi karega wo endpoint
    print(i)


"""

end : end perameter :
 
by  default print function end with new line but

using of end peremeter we can start new line with spacifivc value wise

"""
print("Hello",end =" ")
print("Welcome")




print("\n")

for i in range(1,7):
    print(f"({i}) hello",end=" ")

print("\n")

for i in range(5,0,-1):#reverse number
    print(f"({i}) hello",)