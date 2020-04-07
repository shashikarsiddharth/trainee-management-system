import connection
import traineeClass
import managerClass
import managerSwitcher
import traineeSwitcher
from loginPrompt import get_login_details 
from dbLogin import get_db_login_details
from hashutils import make_pwd_hash, check_pwd_hash

try:
    #Establish DB connection
    connect_obj = connection.connectDb()
    username, password, database = get_db_login_details()
    connect_obj.set_connection(username, password, database)
    cnx = connect_obj.get_connection()

    if cnx != None:
        #Validate login credentials
        username, password = get_login_details()
        fetch_credentials = ("select * from Credentials where username = %s")
        val = (username, )
        cursor = cnx.cursor()
        cursor.execute(fetch_credentials, val)
        credentials = cursor.fetchone() 

        if credentials != None: 
            if checkPwdHash(password, credentials[1]):
                print("Login Successful")
                if username[0] == 't':
                    # Invoke Trainee Class functions
                    print("Welcome {0} to Trainee Management System".format(username))

                elif username[0] == 'm':
                    print("Welcome {0} to Trainee Management System".format(username))
                    # Invoke Manager Menu driven function
                    param_list = [cnx, 1, '2019-03-11', 't1671712']
                    manager_obj = managerClass.Manager()
                    managerSwitcher.manager_option(0, manager_obj, param_list)

            else:
                print("Invalid Password")
        else:
                print("Invalid Username")
    else:
        print("Sorry failed to connect to DB.")
        exit()

except ValueError as err:
    print("Unsupported input type", err)
    
else:
    connect_obj.close_connection()