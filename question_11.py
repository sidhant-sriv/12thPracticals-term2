import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
# To increase the price of all Stationary by 4
mycursor.execute("UPDATE Stationary SET Price=Price+4")
# To display the max and min price of companies with name not CAM
mycursor.execute("SELECT MAX(Price), MIN(Price) FROM Stationary WHERE Company NOT LIKE 'CAM'")
for x in mycursor.fetchall():
    print(x)
# To display all StationaryNames that end in Pen
mycursor.execute("SELECT StationaryName FROM Stationary WHERE StationaryName LIKE '%Pen'")
for x in mycursor.fetchall():
    print(x)
