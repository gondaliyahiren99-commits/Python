student={
    'name' : 'hiren',
    'age' : 25,
    'course': 'python'
}

print(student["name"])
print(student["course"])
#print(student["city"])#show erroe

#get error nahi deta
print(student.get("name"))
print(student.get("city","ahemdabad"))# agar nahi mila to default ayega 

dict={

}
for i in range(3):
    k=input("Enter Key :")
    v=input("Enter Value :")

    dict[k]=v
print(dict)