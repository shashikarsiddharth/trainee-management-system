import mysql.connector
from mysql.connector import errorcode

class connectDb():
    ''' Class for establishing python and Mysql connection. '''

    def __init__(self):
        ''' Function for initializing the connection variable. '''
        self.cnx = 0
        self.cursor = 0

    def set_connection(self, username, password, dbName):
        ''' Function that takes database username, password and dbName for establishing connection. '''
        self.username =  username
        self.password = password
        self.dbName = dbName

    def get_connection(self):
        ''' Function that establishes connection with the db. '''
        try:
            self.cnx = mysql.connector.connect(user=self.username, password=self.password, database=self.dbName)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid credentials")
                return None
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exists")
                return None
            else:
                print("Failed to connect to DB",err)
                return None
        return self.cnx
    
    def close_connection(self):
        ''' Function for breaking the db connection. '''
        self.cnx.close()

if __name__ == "__main__":
        obj = connectDb()
        obj.set_connection(<username>, <password>, <dbName>)
        obj.close_connection()

