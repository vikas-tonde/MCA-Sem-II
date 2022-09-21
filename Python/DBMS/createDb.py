import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="root"
)
cur=db.cursor()
cur.execute("create database MCA_classmates")