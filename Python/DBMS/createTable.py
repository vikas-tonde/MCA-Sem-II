import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="MCA_classmates"
)
cur=db.cursor()
cur.execute("create table student (sid int primary key, sname varchar(30))")