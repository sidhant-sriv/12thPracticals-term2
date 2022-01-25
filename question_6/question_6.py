import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()

# Display the names of the workers whose names end with the letter a
mycursor.execute("SELECT * FROM Worker WHERE Name LIKE '%a'")
for x in mycursor.fetchall():
    print(x)
# To total the number of employees in each category of PLevel
mycursor.execute("SELECT PLevel, COUNT(*) FROM Worker GROUP BY PLevel")
for x in mycursor.fetchall():
    print(x)
# To sort the data in the descending order of DOB
mycursor.execute("SELECT * FROM Worker ORDER BY DOB DESC")
for x in mycursor.fetchall():
    print(x)
