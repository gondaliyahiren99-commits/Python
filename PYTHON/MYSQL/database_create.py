import pymysql
import pymysql
Conect = pymysql.connect(host = "localhost",
user = "root" ,
password="root")

c =Conect.cursor()
c.execute("create database WholeSeller")

Conect.commit()

print("succee to create ")

