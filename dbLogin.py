import getpass

def get_db_login_details():
    ''' Function that takes database login credentials. '''
    print("Enter Login Credentials for Database Connectivity")
    username = str(input("Enter username:"))
    password = getpass.getpass()
    database = str(input("Enter database:"))
    return (username, password, database)
