# connect the mysql databses to the python code

import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",        
    user="root",            
    password="India@11",     
)

my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")

databases = my_cursor.fetchall()

for db in databases:
    print(db)

my_cursor.execute("USE newDB1")

mydb.close()
