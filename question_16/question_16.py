import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="grade_12_db"
)

# create cursor
mycursor = mydb.cursor()
# There are two tables FLIGHTS and FARES
# To display flight number, source, airlines of those flights where fare is less than Rs. 10000.
mycursor.execute("SELECT FLIGHTS.FNO, SOURCE, AIRLINES, FARE FROM FLIGHTS JOIN FARES ON FLIGHTS.FNO = FARES.FNO WHERE FARES.FARE < 10000")
for x in mycursor.fetchall():
    print(x)
# To count total no of Indian Airlines flights starting from various cities
mycursor.execute("SELECT SOURCE, COUNT(AIRLINES) FROM FLIGHTS JOIN FARES ON FLIGHTS.FNO = FARES.FNO WHERE AIRLINES = 'Indian Airlines' GROUP BY SOURCE")
for x in mycursor.fetchall():
    print(x)
# Display all the details where DEST is Varanasi
mycursor.execute("SELECT FLIGHTS.FNO, SOURCE, DEST, AIRLINES, FARE FROM FLIGHTS JOIN FARES ON FLIGHTS.FNO = FARES.FNO WHERE FLIGHTS.DEST = 'Varanasi'")
for x in mycursor.fetchall():
    print(x)
