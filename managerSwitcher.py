def manager_option(option, manager_obj, param_list):
    # Assuming paramList as follows = [cursor, session_id, date, trainee_id]
    ''' Menu driven switcher for manager '''
    switcher = {
        0: manager_obj.create_session(paramList[0]),
        1: manager_obj.update_session(paramList[1], paramList[0]),
        2: manager_obj.view_session_details(paramList[2], paramList[0]),
        3: manager_obj.get_leave_report(paramList[3], paramList[0]),
        4: manager_obj.get_trainee_details(paramList[3],paramList[0]),
        5: manager_obj.get_attendance_report(paramList[1], paramList[0]),
    }
    return switcher.get(option, "nothing") 

    