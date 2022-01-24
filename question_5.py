import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
# Display the average fees of karate
mycursor.execute("SELECT AVG(Fee) FROM Coach WHERE Sports='Karate'")
for x in mycursor.fetchall():
    print(x)
# Count the number of coaches in each sport
mycursor.execute("SELECT Sports, COUNT(*) FROM Coach GROUP BY Sports")
for x in mycursor.fetchall():
    print(x)
# To display details of all coaches where DOJ year is 1988
mycursor.execute("SELECT * FROM Coach WHERE YEAR(DOJ) = 1998")
for x in mycursor.fetchall():
    print(x)
