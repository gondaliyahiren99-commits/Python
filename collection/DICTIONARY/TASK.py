"""create a dict of 5 student """
student={}
status=True

while status:
    sub={}
    Name=input("Enter NAme :")
    if Name.isalpha():
        phy=int(input("ENter phy Marks :"))
        sci=int(input("ENter sci Marks :"))
        math=int(input("ENter math Marks :"))
        bio=int(input("ENter bio Marks :"))
        chem=int(input("ENter chem Marks :"))
        
        sub['phy']=phy
        sub['bio']=bio
        sub['math']=math
        sub['sci']=sci
        sub['chem']=chem

        flag=1
        for k,v in sub.items():
            if v<=35:
                flag=0
                break
        if flag==1:
            student[Name]=sub
        else:
            print(f"{Name} is {[k] }in fail")
      
    else:
        print("re-enter name :")
    print("do continue pres y or yes :")
    pres=input("Enter if you contint :").upper()
    if pres=="Y" or pres=="YES":
       pass
    else:
        status=False
        print(student)

    
       
   


    