import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
#List different voters whose age falls in the range 20 to 25 in descending order of their names.
mycursor.execute("SELECT * FROM Voter WHERE Age BETWEEN 20 AND 25 ORDER BY VName DESC")
for x in mycursor.fetchall():
    print(x)
# Count the number of voters by grouped by age
mycursor.execute("SELECT Age, COUNT(*) FROM Voter GROUP BY Age")
for x in mycursor.fetchall():
    print(x)
# Display the total number of voters who belong to the address ends with ‘i’
mycursor.execute("SELECT COUNT(*) FROM Voter WHERE Address LIKE '%i'")
for x in mycursor.fetchall():
    print(x)
