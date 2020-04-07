import connection

class Manager():
    ''' Class implementing the manager structure '''

    def __init__(self, manager_id=0, manager_name="", manager_contact_no=0):
        ''' Function for getting the values from the database. '''
        self._manager_id = manager_id
        self._manager_name = manager_name
        self._manager_contact_no = manager_contact_no

    # Setter & Getter Functions
    def set_manager_id(self, x):
        ''' set manager id '''
        self._manager_id = x

    def set_manager_name(self, x):
        ''' set manager name '''
        self._manager_name = x

    def set_manager_contact_no(self, x):
        ''' sett manager's contact number '''
        self._manager_contact_no = x

    def get_manager_id(self):
        ''' get manager id '''
        return self._manager_id

    def get_manager_name(self):
        ''' get manager name '''
        return self._manager_id

    def get_manager_contact_no(self):
        ''' get manager's contact number '''
        return self._manager_contact_no

    def create_session(self, cnx):
        ''' Creates sessions '''
        cursor = cnx.cursor()
        query = ("Insert into Session (sessionID, dateHeld, status, timing) values (%s, %s, %s, %s)")
        values = (7, '2019-03-18', 'scheduled', '12PM-2PM')
        cursor.execute(query,values)
        cnx.commit()

    def update_session(self, session_id, cnx):
        ''' Updates session information, currently updates session status '''
        cursor = cnx.cursor()        
        query = ("select * from Session where sessionId = %s")
        val = (sessionId, )
        cursor.execute(query, val)
        info = cursor.fetchone()
        print(info)
    
    def view_session_details(self, date, cnx):
        ''' Returns session information for a particular date '''
        cursor = cnx.cursor()        
        query = ("select * from Session where dateHeld = %s")
        val = (date, )
        cursor.execute(query, val)
        info = cursor.fetchall()
        print(info)

    def get_leave_report(self, trainee_id, cnx):
        ''' Returns all the leaves for a particular trainee '''
        cursor = cnx.cursor()        
        query = ("select * from LeaveDetails where traineeID = %s;")
        val = (trainee_id, )
        cursor.execute(query,val)
        info = cursor.fetchone()
        print(info)
    
    def getTraineeDetails(self, trainee_id, cnx):
        ''' Returns the trainee details for a particular trainee '''
        cursor = cnx.cursor()        
        query = ("select * from Trainee where traineeID = %s;")
        val = (trainee_id, )
        cursor.execute(query, val)
        info = cursor.fetchone()
        print(info)

# TO FIX
    def getAttendanceReport(self, session_id, cnx):
        ''' Returns the attendance for a particular session '''
        cursor = cnx.cursor()        
        query = ("select * from Session where sessionID = %s;")
        val = (session_id, )
        cursor.execute(query, val)
        info = cursor.fetchone()
        print(info)
