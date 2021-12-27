import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Sports_Master"
)

# create cursor
mycursor = mydb.cursor()
# To display the details of the table in the decreasing order of Event_date.
mycursor.execute("SELECT * FROM Sports_Master ORDER BY Event_date DESC")
for x in mycursor.fetchall():
    print(x)
# To count the number of events based on their category.
mycursor.execute("SELECT Category, COUNT(*) FROM Sports_Master GROUP BY Category")
for x in mycursor.fetchall():
    print(x)
# To delete the record where the No_in_team is more than 10.
mycursor.execute("DELETE FROM Sports_Master WHERE No_in_team>10")
for x in mycursor.fetchall():
    print(x)
