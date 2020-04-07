import mysql.connector
from mysql.connector import errorcode
from loginPrompt import get_login_details 
from hashutils import make_pwd_hash, check_pwd_hash

try:
    cnx = mysql.connector.connect(user=<username>, password=<password>, database=<dbname>)
    cursor = cnx.cursor()

    n = int(input("Enter number of associates in DB:\n"))
    
    for i in range(n):
        #username for trainee is: t1234
        #username for manager is: m1245
        username, password = get_login_details()
        add_credentials = ("Insert into Credentials (username, password) values (%s, %s)")
        val = (username, make_pwd_hash(password))
        cursor.execute(add_credentials, val)
        cnx.commit()
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid Credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exists")
    else:
        print("Failed to Connect to DB error:",err)
else:            
    cnx.close()