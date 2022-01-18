import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
# To increase the price of all watches by 10% whose Qty_Store is less than 150.
mycursor.execute("UPDATE WATCHES SET Price=Price*1.1 WHERE Qty_Store<150")
mydb.commit()
# Disply different Types of Watches available in the given data;
mycursor.execute("SELECT DISTINCT Type FROM WATCHES")
for x in mycursor.fetchall():
    print(x)
# Change column name from Price to ItemPrice
mycursor.execute("ALTER TABLE WATCHES RENAME COLUMN Price TO ItemPrice")
