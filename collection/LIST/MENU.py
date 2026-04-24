# menu= """

# Menu
# 1.add new element
# 2.remove element
# 3.remove last element
# 4. remove index vise element
# 5.exit
# """
# l1=[]
# status =True

# while status:
#     print(menu)
#     choice= int(input("Enter choice :"))
#     if choice==1:
#         no=int(input("How many element to add :"))
#         for i in range(1,no+1):
#             print("Do you want int add  so yes:")
#             ch=input("yes or no ").upper()
#             if ch=="YES":
#                 no=int(input("Enter Number :"))
#                 l1.append(no)
#             else:
#                 str=input("Enter char or string :")
#                 l1.appen(str)
  
#         print("All ele added succesfully :")
#         print(l1)

#     elif choice==2:
#         print(l1)
#         remove_ele=int(input("Enter ehich ele you want remove :"))
#         l1.remove(remove_ele)
#===========================================================================================

menu="""\n
                            :MENU:
                    PRESS ~> 1. for adding new eliment in list 
                    PRESS ~> 2. for removing eliment
                    PRESS ~> 3. for removing last eliment
                    PRESS ~> 4. for removing spacific index eliment
                    PRESS ~> 5. EXIT
"""
status=True
l1=[]
while status:
    print(menu)
    ch=int(input("enter your choice :"))
    if ch==1:
        ren=int(input("enter how many eliment you wanted to add in list : "))
        for i in range(ren):
            eli=input(f"enter your eliment {i+1} :")
            l1.append(eli)
        print("~~~~~~~~~~adding succesfuly~~~~~~~~\n")
        print("\tELIMENTS\n")
        for i in l1:
            print(i,end=", ")
    elif ch==2:
        print("'''''ALL ELIMENT IN LIST'''''''\n")
        print(l1)
        rem=input("\nenter removing eliment :")
        l1.remove(rem)
        print(f"\n~~~~~~~~~~~:you removed <<{rem}>> succesfuly:~~~~~~~~~~~~\n")
        print("updated list |")
        print("             v")
        print("\t\t",end="")
        for i in l1:
            print(f"{i}",end=", ")
    elif ch==3:
        print(f"you deleted or removed last eliment <<{l1.pop()}>> from list.")
        print("updated list |")
        print("             v")
        print("\t\t",end="")
        for i in l1:
            print(f"{i}",end=", ")
    elif ch==4:
        print("your choice is remove spacific index eliment\n")
        inde=int(input("enter your index number :"))
        print(f"you deleted or removed last eliment <<{l1.pop(inde)}>> from list.")
        print(f"you removed succesfuly...\n")
        print("updated list |")
        print("             v")
        print("\t\t",end="")
        for i in l1:
            print(f"{i}",end=", ")
    elif ch==5:
        break