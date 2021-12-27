import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Planes_database"
)

# create cursor
mycursor = mydb.cursor()
# There are two tables FLIGHTS and FARES
# To display flight number, source, airlines of those flights where fare is less than Rs. 10000.
mycursor.execute("SELECT FLIGHTS.FNO, FLIGHTS.SOURCE, FLIGHTS.AIRLINES, FARES.FARE FROM FLIGHTS, FARES WHERE FLIGHTS.FNO = FARES.FNO AND FARES.FARE < 10000")
for x in mycursor.fetchall():
    print(x)
# To count total no of Indian Airlines flights starting from various cities
mycursor.execute("SELECT FLIGHTS.SOURCE, COUNT(FLIGHTS.AIRLINES) FROM FLIGHTS WHERE FLIGHTS.AIRLINES = 'Indian Airlines' GROUP BY FLIGHTS.SOURCE")
for x in mycursor.fetchall():
    print(x)
# Display all the details where DEST is Varanasi
mycursor.execute("SELECT FLIGHTS.FNO, FLIGHTS.SOURCE, FLIGHTS.DEST, FLIGHTS.AIRLINES, FARES.FARE FROM FLIGHTS, FARES WHERE FLIGHTS.FNO = FARES.FNO AND FLIGHTS.DEST = 'Varanasi'")
for x in mycursor.fetchall():
    print(x)
