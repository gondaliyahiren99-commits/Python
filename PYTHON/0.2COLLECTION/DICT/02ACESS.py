student={
    'name' : 'hiren',
    'age' : 25,
    'course': 'python'
}


#method :1
print(student["name"])
print(student["course"])
#print(student["city"])#show erroe



#method :2
#get error nahi deta
print(student.get("name"))
print(student.get("village")) #error nahi but none dikhyega
print(student.get("city","ahemdabad"))# agar nahi mila to default ayega 




#=================================================ExtraWork
dict={

}
for i in range(3):
    k=input("Enter Key :")
    v=input("Enter Value :")

    dict[k]=v
print(dict)