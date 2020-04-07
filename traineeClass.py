import connection

class Trainee():
    ''' Class implementing the trainee structure '''

    def __init__(self, trainee_id=0, trainee_name="", trainee_contact_no=0):
        ''' Function for getting the values from the database. '''
        self._trainee_id = trainee_id
        self._trainee_name = trainee_name
        self._trainee_contact_no = trainee_contact_no

    # Setter & Getter Functions
    def set_trainee_id(self, x):
        ''' set trainee id '''
        self._trainee_id = x

    def set_trainee_name(self,x):
        ''' set trainee name '''
        self._trainee_name = x

    def set_trainee_contact_no(self, x):
        ''' set trainee's contact number '''
        self._trainee_contact_no = x

    def get_trainee_id(self):
        ''' get trainee id '''
        return self._trainee_id

    def get_trainee_name(self):
        ''' get trainee name '''
        return self._trainee_id

    def get_trainee_contact_no(self):
        ''' get trainee's contact number '''
        return self._trainee_contact_no

    # Doing Responsibility
    def view_session_details(self, date):
        ''' Returns session information for a particular date '''
        pass

    def join_session(self, session_id):
        ''' Marks trainee attendance for a particular session '''
        pass
    
    def session_feedback(self, session_id):
        ''' Add feedback for a particular session id '''
        pass

    def leave_application(self, session_id):
        ''' Apply leave application '''
        pass