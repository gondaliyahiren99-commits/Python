
import pymysql
Jodo = pymysql.connect(host = "localhost",
user = "root" ,
password="root" ,
database="WholeSeller")

one_by_one=Jodo.cursor()
one_by_one.execute( "create table apka_naye_table_name(name text, id int , course text) ")

Jodo.commit()
print("table created .........")