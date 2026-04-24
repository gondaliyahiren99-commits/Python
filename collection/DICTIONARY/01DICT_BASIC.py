# student={
#     'name' : 'hiren',
#     'age' : 25,
#     'course': 'python'
# }

# print(student)

# print(student.keys())#key fetch

# print(student.values())#value fetch

# from PYTHON.01_BASIC.VARIABLE import surname
# studen1={
#     'name':'hiren',
#     'course':'python',
#     'age':25
# }
# studen1["look"]="awesome"

# for k in studen1.keys():
#     print(k)

# for v in studen1.values():
#     print(v)

# for i,j in studen1.items():
#     print(f"{i}={j}")

# for i in range(5):
#     i=input("Enter a Key :")
#     k=input("Enter Value :")
#     studen1[i]=k
# print(studen1.values()) 
# from collection.DICTIONARY.TASK import student
# main_dict={}
# dict={}
# for i in range(3)


student={}
fail={}
num=int(input("Enter How Much Student :"))
for i in range(num):
    Marks={}
    f_name=input("Enter Name :")
    math=int(input("Enter Maths Marks :"))
    scince=int(input("Enter Scince Marks :"))
    bio=int(input("Enter Bio Marks :"))
    Phy=int(input("Enter Physics Marks :"))
    chem=int(input("Enter Chemestry Marks :"))

    Marks["MATH"]=math
    Marks["SCINCE"]=scince
    Marks["BIO"]=bio
    Marks["PHYSICs"]=Phy
    Marks["CHEMESTRY"]=chem

    student[f_name]=Marks
for key,val in student.items():
    for k,v in val.items():
        if v<35:
            fail[f_name]=Marks

print(fail)
 
if fail[f_name]==student[f_name]:
    del student[f_name]

print(student)