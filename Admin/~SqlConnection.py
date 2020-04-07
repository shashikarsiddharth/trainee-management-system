import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user="siddharth", password="Tata@1234", database="TMS")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid Credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exists")
    else:
        print("Failed to Connect to DB error:",err)
else:            
    cnx.close()