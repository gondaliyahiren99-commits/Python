
import pymysql


Con = pymysql.connect(host="localhost",
user="root",
password="root")   # jab bhi hum programe startkare  tab sql ke sath connect karne ke liye likhte he 

cursor = Con.cursor() # database comnection 
# cursor object 

cursor.execute("create database  if not exists dbms_python")
Con.commit()  #save

Con = pymysql.connect(host="localhost",
user="root",
password="root",
database ="dbms_python" )

cursor = Con.cursor()

cursor.execute("create table if not exists Python_student  (name varchar(20),age int ,courese varchar(20))")
Con.commit()

def addStudent():
    cursor = Con.cursor()

    name = input("Enter Student Name :")
    age  = int(input("Enter Student id :"))
    course = input("Enter course :")

    q= "insert into Python_student(name,age,courese) values('%s','%s','%s')"
    args = (name, age , course)

    cursor.execute(q % args)

    Con.commit()
    print("succes")

def ShowDetail():
    cursor = Con.cursor()
    cursor.execute("select * from  python_student")
    data = cursor.fetchall()
    print(data)

def deleteStudent():
    cursor = Con.cursor()
    name = input('Enter Name : ')

    q= "delete from python_student where name = %s"
    args = (name)

    cursor.execute(q,args)
    Con.commit()
    print("Dleted..........")


def UpdateDetail():
    cursor = Con.cursor()
    name = input("Enter Name :")
    new_name = input("enter  new name : ")

    q="update python_student set name = %s  where name = %s"
    ar= (new_name , name)


    cursor.execute(q ,ar)
    Con.commit()
    print("Uodated")

def viewSingle():
    c =Con.cursor()
    name = input("Enter Name : ")
    q= "select * from python_student where name = %s"
    a = name
    c.execute(q, a)
    data =c.fetchall()
    print(data)



MENU = """

                        1 for add srudent
                        2 for show student detail 
                        3 update student detail
                        4 for remove student
                        5 singe shoew detail
                        6 Exite

""".upper()

status = True 
while status :
    print(MENU)
    ch = int(input("Enter Choice :"))
    if ch == 1:
        addStudent()
    elif ch ==2:
        ShowDetail()   
    elif ch ==3:
        UpdateDetail()
    elif ch==4 :
        deleteStudent()
    elif ch== 5 :
        viewSingle()
    elif ch>6 or ch <0 :
        print("Re-Enter Choice :")
    else :
        status = False
