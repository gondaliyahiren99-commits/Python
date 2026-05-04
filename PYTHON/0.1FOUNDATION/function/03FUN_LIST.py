list=[]
def create():
    n=int(input("Enter How much enter Ele :"))
    for i in range(n): 
        ele=input("enter ele:")
        if ele.isnumeric():
            ele=int(ele)
            list.insert(i,ele)
        else:
            list.insert(i,ele)
    return f'succefuly crea a list'

def show():
   return f"{print(list)}"

def remove():
    i_or_v=input("Enter your ch you eant to remove with index press i otherwise press v").upper()
    status =True
    while status:
        if i_or_v=="I":
            I=int(input("Enter index :"))
            list.pop(I)
            break
        elif i_or_v=="V":
            V=int(input("Enter Value :")).upper()
            remove(V)
            break
        else:
            return"invalid ! re-enter :"
def adding():
    status=True
    while status:
        enter=input(" do you wantAdd an ele  yes or no:").lower()
        if enter=='yes'or enter=='y':
            ele=input("Enter ELE")
            if ele.isnumeric():
                ele=int(ele)
                list.append(ele)
            elif ele.isalpha():
                if ele.capitalize()=="True" or ele.capitalize()=="False":
                    ele=bool(ele)
                    list.append(ele)

                else:
                    list.append(ele)
            elif ele.isalnum():
                if ele.startswith('-'):
                    ele=int(ele)
                    list.append(ele)
                else:
                    list.append(ele)
        elif enter =='no' or enter=='n':
            status=False

        else:
            print("Re-Enter y or n.....")




MENU= """
        1)creat
        2)add
        3)show
        4)add
        5)exit

        """

status=True
while status:
    print(MENU)
    ch=int(input("enter choice :"))
    if ch==1:
        print(create())
    elif ch==2:
       print( show())
    elif ch==3:
        print(remove())
    elif ch==4:
        print(adding())
    elif ch==5:
        status=False
    else:
        print("Re-Enter:")


