# insert the data in table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="India@11",
)

my_cursor = mydb.cursor()

my_cursor.execute("USE newDB1")

# Insert data into the 'courses' table
my_cursor.execute('INSERT INTO courses VALUES (4, "devops", 9, 60000)')
# my_cursor.execute("DELETE FROM courses WHERE course_id = 4")
mydb.commit()

my_cursor.execute("SELECT * FROM courses")
result = my_cursor.fetchall()

for row in result:
    print(row)

mydb.close()
