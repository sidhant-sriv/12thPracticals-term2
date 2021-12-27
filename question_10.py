import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Items"
)

# create cursor
mycursor = mydb.cursor()
# To display all the ItemName whose name starts with “S” or ends with “a’.
mycursor.execute("SELECT ItemName FROM Items WHERE ItemName LIKE 'S%' OR ItemName LIKE '%a'")
for x in mycursor.fetchall():
    print(x)
# To count the number of items whose cost is more than 10000.
mycursor.execute("SELECT COUNT(*) FROM Items WHERE CostPerItem>10000")
for x in mycursor.fetchall():
    print(x)
# To display the details of the costliest Item.
mycursor.execute("SELECT * FROM Items WHERE Cost=(SELECT MAX(Cost) FROM Items)")
