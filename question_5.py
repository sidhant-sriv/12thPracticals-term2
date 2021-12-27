import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Coach"
)

# create cursor
mycursor = mydb.cursor()
# Display the average fees of karate
mycursor.execute("SELECT AVG(Fee) FROM Coach WHERE Sport='Karate'")
for x in mycursor.fetchall():
    print(x)
# Count the number of coaches in each sport
mycursor.execute("SELECT Sport, COUNT(*) FROM Coach GROUP BY Sport")
for x in mycursor.fetchall():
    print(x)
# To display details of all coaches where DOJ year is 1988
mycursor.execute("SELECT * FROM Coach WHERE DOJ LIKE '%1988%'")
for x in mycursor.fetchall():
    print(x)
