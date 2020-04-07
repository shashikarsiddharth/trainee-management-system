import getpass

def get_login_details():
    ''' Function that takes login credentials. '''
    print("Enter Login Credentials")
    username = str(input("Enter username:"))
    password = getpass.getpass()
    return (username, password)
