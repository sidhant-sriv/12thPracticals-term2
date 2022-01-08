import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Bank_database"
)

# create cursor
mycursor = mydb.cursor()

# There are two tables CUSTOMER_INFO and  TRANSACTION_DETAIL
mycursor.execute("SELECT Cust_Name, Trans_Id, TRANSACTION_DETAIL.Acc_No, Transaction_Type, Amount FROM CUSTOMER_INFO JOIN TRANSACTION_DETAIL ON CUSTOMER_INFO.Acc_Name = TRANSACTION_DETAIL.Acc_Name WHERE CUSTOMER_INFO.Name='Ram'")
for x in mycursor.fetchall():
    print(x)
# Display the account details and total number of transactions for each account located in “New Delhi”
mycursor.execute("SELECT Cust_Name, COUNT(Trans_Id) FROM CUSTOMER_INFO JOIN TRANSACTION_DETAIL ON CUSTOMER_INFO.Acc_Name = TRANSACTION_DETAIL.Acc_Name WHERE CUSTOMER_INFO.Add= 'New Delhi'")
for x in mycursor.fetchall():
    print(x)
# Display all records from both the tables using cross join
mycursor.execute("SELECT * FROM CUSTOMER_INFO CROSS JOIN TRANSACTION_DETAIL")
for x in mycursor.fetchall():
    print(x)
