import pymysql
Con = pymysql.connect(host="localhost",user="root",passwd="pasword ")

Cursor = Con.cursor()
Cursor.execute("crete database if not exists python_db_practice")
Con.commit()


Con = pymysql.connect(host="localhost",user = "root",password="user pasword",database="python_db_practice")
Cursor=Con.cursor()
Cursor.execute("create table if not exists student (id in primery key,auto_increment,name varchar(20),subject varchar(20),score int)")
Con.commit()

