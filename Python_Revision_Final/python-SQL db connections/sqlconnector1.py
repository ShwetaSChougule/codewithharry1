
#pip install mysql-connector-python
# we use mysql.connector to connect Mysql db with python
import mysql.connector

# connecting from the server  - using .connect() method- used to set connection with mysql server
connection=mysql.connector.connect(host="localhost",user="root",password="root")
# host - it is location of mysql server, localhost if it is on same pc
if connection.is_connected():
    print("MySQL connected successfully")

################################Connection done#########################################

# creating database object.
# cursor is the workspace created in a system memory, when sql commands are excuted.
# This memory is temporary and cursor connection is only for that session
cursor=connection.cursor()
#########################create database################################################
# cursor.execute("CREATE DATABASE GEEKS")

######################table creation###################################################
cursor.execute("USE GEEKS")
# table creation:
# studentrecord = """CREATE TABLE STUDENT(
#                     NAME VARCHAR(50),
#                     BRANCH VARCHAR(50),
#                     ROLL INT NOT NULL,
#                     SECTION VARCHAR(50),
#                     AGE INT
#                     )"""
#
# cursor.execute(studentrecord)
# print('table created')
###########################inserting into table########################

# sql = "INSERT INTO STUDENT(NAME,BRANCH,ROLL,SECTION,AGE) VALUES(%s,%s,%s,%s,%s)"
# val = [("SHWETA","CS","01","A","30"),
#        ("SEETA","CS","02","A","30")]
# # to create single value use execute()
# # to create multiple values use executemany()
# cursor.executemany(sql,val)
# print(mycursor.rowcount, "details inserted")    #rowcount-number of rows
# connection.commit()


######################################FETCHING DATA FROM TABLE#########################

query = "SELECT NAME, ROLL FROM STUDENT"
cursor.execute(query)

result = cursor.fetchall()

for i in result:
    print(i)
connection.close()
# SIMILARLY WE CAN USE WHERE,OERDER BY,LIMIT,UPDATE,DELETE,DROP can be used
# in case of drop table , use DROP TABLE IF EXISTS TABLENAME else will give prog error
# update - update student set age=23 where roll=01
