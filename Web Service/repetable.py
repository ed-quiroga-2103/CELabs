import datetime 

def array_days(dias):
    
    today = datetime.date.today()
    #Se debe verificar la fecha
    finaliza_semestre = "2020-12-18"
    final_sem = datetime.datetime.strptime(finaliza_semestre, "%Y-%m-%d").date()
    days = abs((final_sem - today).days)
    dates = []

    for i in range(days+1):
        result = today + datetime.timedelta(days= i)
        for x in dias:
            if result.weekday() == x:
                dates.append(result.strftime("%Y-%m-%d"))

    return dates


def modify_days(days):
    result = []
    for i in days:
        if i == "L":
            result.append(0)
        elif i == "K":
            result.append(1)
        elif i == "M":
            result.append(2)
        elif i == "J":
            result.append(3)
        elif i == "V":
            result.append(4)
        elif i == "S":
            result.append(5)
        elif i == "D":
            result.append(6)

    return (result)