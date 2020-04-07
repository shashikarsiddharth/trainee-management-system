def trainee_option(option, trainee_obj, param_list):
    ''' Menu driven switcher for trainee '''
    # Assuming paramList as follows = [cursor, sessionId, date, traineeId]  
    switcher = {
        0: trainee_obj.view_session_details(paramList[2]),
        1: trainee_obj.join_session(paramList[1]),
        2: trainee_obj.session_feedback(paramList[1]),
        3: trainee_obj.leave_application(paramList[1]),
    }
    return switcher.get(option, "nothing") 
