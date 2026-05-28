import pymysql
Jodo = pymysql.connect(host = "localhost",
user = "root" ,
password="root" ,
database="WholeSeller")

one_by_one=Jodo.cursor()
for i in range(3):
    name = input("Enter Name  :")
    id = int(input("Enter Id : "))
    q=("insert into apka_naye_table_name(name,id) values(%s,%s)")
    args= (name,id,)

    one_by_one.execute(q , args)
    Jodo.commit()
print("table inserted...............")