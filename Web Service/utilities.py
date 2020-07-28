from datetime import datetime

def get_time_in_seconds(time_as_string):

    date_time_obj = datetime.strptime(time_as_string, '%d/%m/%Y')

    return date_time_obj
