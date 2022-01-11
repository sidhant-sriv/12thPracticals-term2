# use mysql connector to connect to mysql database
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
# Count the total number of kids travelling from Anand travels
mycursor.execute("SELECT SUM(Noofstud) FROM School_Bus WHERE Transporter='Anand Travels'")
for x in mycursor.fetchall():
    print(x)
# Increase the charges by 3000 where distance is greater than 25
mycursor.execute("UPDATE School_Bus SET Charges=Charges+3000 WHERE Distance>25")
for x in mycursor.fetchall():
    print(x)
# To show transporter wise average no of students traveling
mycursor.execute("SELECT Transporter, AVG(Noofstud) FROM School_Bus GROUP BY Transporter")
for x in mycursor.fetchall():
    print(x)
