## see the data present in the table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="India@11",
)

my_cursor = mydb.cursor()

my_cursor.execute("USE newDB1")

my_cursor.execute("SELECT * FROM courses")
result = my_cursor.fetchall()

for row in result:
    print(row)

mydb.close()
