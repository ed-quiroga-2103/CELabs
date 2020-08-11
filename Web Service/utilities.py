from datetime import datetime

ONE_DAY = 86400

def get_date_in_seconds(date_as_string):

    date_obj = datetime.strptime(date_as_string, '%d/%m/%Y')

    return (date_obj - datetime.strptime('01/01/1970', '%d/%m/%Y') ).total_seconds()

def get_datetime_in_seconds(datetime_as_string):

    datetime_obj = datetime.strptime(datetime_as_string, '%d/%m/%Y %H:%M:%S')

    return (datetime_obj - datetime.strptime('01/01/1970 00:00:00', '%d/%m/%Y %H:%M:%S')).total_seconds()

def get_time_in_seconds(time_as_string):

    date_obj = datetime.strptime(time_as_string, '%H:%M:%S')

    return (date_obj - datetime.strptime('00:00:00', '%H:%M:%S') ).total_seconds()


def get_date_from_seconds(seconds):

    seconds += ONE_DAY
    date = datetime.fromtimestamp(seconds).strftime('%d/%m/%Y')

    return date

def get_datetime_from_seconds(seconds):
    
    seconds += ONE_DAY/4
    date = datetime.fromtimestamp(seconds).strftime('%d/%m/%Y %H:%M:%S')

    return date

def get_time_from_seconds(seconds):
    seconds += ONE_DAY/4
    time = datetime.fromtimestamp(seconds).strftime('%H:%M:%S')

    return time
