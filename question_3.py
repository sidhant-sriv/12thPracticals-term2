# use mysql connector to connect to mysql database
import mysql.connector

# connect to database Hospital
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Hospital"
)

# create cursor
mycursor = mydb.cursor()
# List the names of all the females in the orthopedic department
mycursor.execute("SELECT * FROM Hospital WHERE Department='Orthopedic' AND Sex='F'")
for x in mycursor.fetchall():
    print(x)

# To count the number of patients with age greater than 30.
mycursor.execute("SELECT COUNT(AGE) FROM Hospital WHERE AGE>30")
for x in mycursor.fetchall():
    print(x)
#To show all information about the patients of cardiology department
mycursor.execute("SELECT * FROM Hospital WHERE Department='Cardiology'")
for x in mycursor.fetchall():
    print(x)


