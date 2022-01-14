import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
# Add a new column called dealers of type varchar(10), update the dealer column for all rows to ‘Unknown’
# Add new column
mycursor.execute("ALTER TABLE INTERIORS ADD COLUMN dealers VARCHAR(10)")
# Update the dealer column for all rows to ‘Unknown’
mycursor.execute("UPDATE INTERIORS SET dealers='Unknown'")
#  Display the total amount after deducting the discount amount for every item
mycursor.execute("SELECT ITEMNAME, PRICE, DISCOUNT, (PRICE- PRICE*DISCOUNT/100) FROM INTERIORS") # As I am not too sure about if this will work or not, I have decided to quit.
for x in mycursor.fetchall():
    print(x)
#  Display the items having ‘e’ in it’s name
mycursor.execute("SELECT ITEMNAME FROM INTERIORS WHERE ITEMNAME LIKE '%e%'")
for x in mycursor.fetchall():
    print(x)
