import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
# Find the average price of the movies where rating is not G
mycursor.execute("SELECT AVG(Price) FROM MOVIE WHERE Rating!='G'")
for x in mycursor.fetchall():
    print(x)
#  Increase the Price of ‘Drama’ type of books by 10%
mycursor.execute("UPDATE MOVIE SET Price=Price*1.1 WHERE Type='Drama'")
for x in mycursor.fetchall():
    print(x)
#  Delete the column ‘Stars from the given table.
mycursor.execute("ALTER TABLE MOVIE DROP COLUMN Stars")
for x in mycursor.fetchall():
    print(x)
