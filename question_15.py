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
mycursor.execute("SELECT CUSTOMER_INFO.Cust_Name, TRANSACTION_DETAIL.Trans_Id, TRANSACTION_DETAIL.Acc_No,TRANSACTION_DETAIL.Transaction_Type,TRANSACTION_DETAIL.Amount FROM CUSTOMER_INFO, TRANSACTION_DETAIL WHERE CUSTOMER_INFO.Acc_Name = TRANSACTION_DETAIL.Acc_Name AND WHERE CUSTOMER_INFO.Name='Ram'")
for x in mycursor.fetchall():
    print(x)
# Display the account details and total number of transactions for each account located in “New Delhi”
mycursor.execute("SELECT CUSTOMER_INFO.Cust_Name, COUNT(TRANSACTION_DETAIL.Trans_Id) FROM CUSTOMER_INFO, TRANSACTION_DETAIL WHERE CUSTOMER_INFO.Acc_Name = TRANSACTION_DETAIL.Acc_Name AND WHERE CUSTOMER_INFO.Add= 'New Delhi'")
for x in mycursor.fetchall():
    print(x)
# Display all records from both the tables using cross join
mycursor.execute("SELECT * FROM CUSTOMER_INFO CROSS JOIN TRANSACTION_DETAIL")
for x in mycursor.fetchall():
    print(x)
