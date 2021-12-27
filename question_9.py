import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Employee"
)

# create cursor
mycursor = mydb.cursor()
# To display the name of the only Female employees
mycursor.execute("SELECT * FROM Employee WHERE Sex='F'")
for x in mycursor.fetchall():
    print(x)
# To display the total number of employees department wise.
mycursor.execute("SELECT Deptid, COUNT(*) FROM Employee GROUP BY Deptid")
for x in mycursor.fetchall():
    print(x)
# To display the Name that begin with ‘H’.
mycursor.execute("SELECT Name FROM Employee WHERE Name LIKE 'H%'")
for x in mycursor.fetchall():
    print(x)