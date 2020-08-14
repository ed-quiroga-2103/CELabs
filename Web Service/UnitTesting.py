import unittest
import requests
from flask import jsonify
import time
from requests.auth import HTTPBasicAuth


def get_token():
    r = requests.post('http://127.0.0.1:5001/login', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                } 
        ,auth=HTTPBasicAuth('Op', 'Op'))

    token = r.json()['token']
    return token

# ------------ Reservation ------------------

def test_post_reservation(self):
        token = get_token()

        url = "http://127.0.0.1:5001/reservation"

        payload = {
    
            "description": "Espe",
            "subject": "Subject",
            "requesting_user":"Prof",
            "operator": "Op",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "request_date":"12/12/2020", 
            "requested_date":"13/12/2020",
            "lab": "F2-09"
            }
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("POST", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

def test_repeated_reservation(self):
    token = get_token()

    r = requests.post('http://127.0.0.1:5001/reservation', 
        headers={
            'Authorization': 'Basic QWRtaW46MTIzNDU=', 
            'Content-Type': 'application/json', 
            'x-access-token': token,
            },
        json = {
            "description": "Espe",
            "subject": "Subject",
            "requesting_user":"Prof",
            "operator": "Op",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "request_date":"12/12/2020", 
            "requested_date":"13/12/2020",
            "lab": "F2-09"
            } 
    )

    self.assertEqual('<Response [401]>', str(r))

def test_edit_reservation(self):
    token = get_token()

    r = requests.put('http://127.0.0.1:5001/reservation', 
        headers={
            'Authorization': 'Basic QWRtaW46MTIzNDU=', 
            'Content-Type': 'application/json', 
            'x-access-token': token,
            },
        json = {
            "old":{
                "description": "Espe",
                "subject": "Subject",
                "requesting_user":"Prof",
                "operator": "Op",
                "init_time": "12:12:12",
                "final_time": "13:00:00",
                "request_date":"12/12/2020", 
                "requested_date":"13/12/2020",
                "lab": "F2-09"
                },
            "new": {
                "description": "Espe",
                "subject": "Edit",
                "requesting_user":"Prof",
                "operator": "Op",
                "init_time": "12:12:12",
                "final_time": "13:00:00",
                "request_date":"12/12/2020", 
                "requested_date":"13/12/2020",
                "lab": "F2-09"
            }
            
            } 
    )
    self.assertEqual('<Response [200]>', str(r))

def test_delete_reservation(self):
        token = get_token()


        r = requests.request("DELETE", 'http://127.0.0.1:5001/reservation', 
            headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                },
            json = {
                "description": "Espe",
                "subject": "Edit",
                "requesting_user":"Prof",
                "operator": "Op",
                "init_time": "12:12:12",
                "final_time": "13:00:00",
                "request_date":"12/12/2020", 
                "requested_date":"13/12/2020",
                "lab": "F2-09"
                } 
        )

        self.assertEqual('<Response [200]>', str(r))

# ------------ All-Nighter ------------------


def test_post_allnighter(self):
        token = get_token()

        url = "http://127.0.0.1:5001/allnighter"

        payload = {
            "description": "Espe",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "request_date":"12/12/2020", 
            "requested_date":"13/12/2020",
            "lab": "F2-09"
        }

        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("POST", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

def test_repeated_allnighter(self):
    token = get_token()

    r = requests.post('http://127.0.0.1:5001/allnighter', 
        headers={
            'Authorization': 'Basic QWRtaW46MTIzNDU=', 
            'Content-Type': 'application/json', 
            'x-access-token': token,
            },
        json = {
            "description": "Espe",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "request_date":"12/12/2020", 
            "requested_date":"13/12/2020",
            "lab": "F2-09"
        }
    )

    self.assertEqual('<Response [401]>', str(r))

def test_edit_allnighter(self):
    token = get_token()

    r = requests.put('http://127.0.0.1:5001/allnighter', 
        headers={
            'Authorization': 'Basic QWRtaW46MTIzNDU=', 
            'Content-Type': 'application/json', 
            'x-access-token': token,
            },
        json = {
                "old":{
                "description": "Espe",
                "init_time": "12:12:12",
                "final_time": "13:00:00",
                "request_date":"12/12/2020", 
                "requested_date":"13/12/2020",
                "lab": "F2-09"
            },
                "new": {
                "description": "Edit",
                "init_time": "12:12:12",
                "final_time": "13:00:00",
                "request_date":"12/12/2020", 
                "requested_date":"13/12/2020",
                "lab": "F2-09"
            }
            
            } 
    )
    self.assertEqual('<Response [200]>', str(r))

def test_edit_state_allnighter(self):
    token = get_token()

    url = "http://127.0.0.1:5001/allnighter/state"

    payload = {
        "id_allnighter": 1,
        "status": "Denied"
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("PUT", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_delete_allnighter(self):
        token = get_token()


        r = requests.request("DELETE", 'http://127.0.0.1:5001/allnighter', 
            headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                },
            json = {
                "description": "Edit",
                "init_time": "12:12:12",
                "final_time": "13:00:00",
                "request_date":"12/12/2020", 
                "requested_date":"13/12/2020",
                "lab": "F2-09"
            }
 
        )

        self.assertEqual('<Response [200]>', str(r))


# ------------ Worklog ------------------

def test_post_worklog(self):
    token = get_token()

    url = "http://127.0.0.1:5001/worklog"

    payload = {
        "description": "Espe",
        "init_time": "12:12:12",
        "final_time": "13:00:00",
        "date_time":"12/12/2020", 
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("POST", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_repeated_worklog(self):
    token = get_token()

    url = "http://127.0.0.1:5001/worklog"

    payload = {
        "description": "Espe",
        "init_time": "12:12:12",
        "final_time": "13:00:00",
        "date_time":"12/12/2020", 
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("POST", url, headers=headers, json = payload)

    self.assertEqual('<Response [401]>', str(r))

def test_put_worklog(self):
    token = get_token()

    url = "http://127.0.0.1:5001/worklog"

    payload = {
        "old":{
            "description": "Espe",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "date_time":"12/12/2020",
            "status": "Pending"
        },
        "new":{
            "description": "Edit",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "date_time":"12/12/2020",
            "status": "Pending"

        }
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("PUT", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_delete_worklog(self):
    token = get_token()

    url = "http://127.0.0.1:5001/worklog"

    payload = {
        "description": "Edit",
        "init_time": "12:12:12",
        "final_time": "13:00:00",
        "date_time":"12/12/2020",
        "id_worklog" : 1 
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("DELETE", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_edit_state_worklog(self):
    token = get_token()

    url = "http://127.0.0.1:5001/worklog"

    payload = {
        "old":{
            "description": "Edit",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "date_time":"12/12/2020",
            "status": "Pending",
            "id_worklog" : 1 
        },
        "new":{
            "description": "Edit",
            "init_time": "12:12:12",
            "final_time": "13:00:00",
            "date_time":"12/12/2020",
            "status": "Completed",
            "id_worklog" : 1 

        }
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("PUT", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))


# ------------ Events ------------------
def test_post_event(self):
    token = get_token()

    url = "http://127.0.0.1:5001/event"

    payload = {
    "description": "Espe",
    "init_time": "12:12:12",
    "final_time": "13:00:00",
    "week_day": "K,J",
    "is_repeatable": "1",
    "lab": "F2-09",
    "date":""
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("POST", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_delete_event(self):
    token = get_token()

    url = "http://127.0.0.1:5001/event"

    payload = {
    "description": "Espe",
    "init_time": "12:12:12",
    "final_time": "13:00:00",
    "week_day": "K,J",
    "is_repeatable": "1",
    "lab": "F2-09",
    "date":""
    }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("DELETE", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))



# ------------ Tests ------------------

class TestStringMethods(unittest.TestCase):
    
    def test_good_login(self):

        r = requests.post('http://127.0.0.1:5001/login', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                } 
        ,auth=HTTPBasicAuth('Op', 'Op'))
        self.assertEqual('<Response [200]>', str(r))        


    def test_bad_login(self):

        r = requests.post('http://127.0.0.1:5001/login', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                } 
        ,auth=HTTPBasicAuth('Op', 'Error'))
        self.assertEqual('<Response [401]>', str(r))        

    def test_get_reservation(self):
        token = get_token()

        r = requests.get('http://127.0.0.1:5001/reservation', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                } 
        )
        self.assertEqual('<Response [200]>', str(r))       

    def test_get_its_reservation(self):
        token = get_token()

        r = requests.get('http://127.0.0.1:5001/reservation/user', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                } 
        )
        self.assertEqual('<Response [200]>', str(r))


    def test_reservation(self):
        test_post_reservation(self)
        test_repeated_reservation(self)
        test_edit_reservation(self)
        test_delete_reservation(self)
    
    def test_get_allnighter(self):
        token = get_token()

        r = requests.get('http://127.0.0.1:5001/allnighter', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                } 
        )
        self.assertEqual('<Response [200]>', str(r))

    def test_allnighter(self):
        test_post_allnighter(self)
        test_repeated_allnighter(self)
        test_edit_state_allnighter(self)
        test_delete_allnighter(self)

    def test_get_all_worklog(self):   
        token = get_token()

        r = requests.get('http://127.0.0.1:5001/worklog', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                } 
        )
        self.assertEqual('<Response [200]>', str(r))    

    def test_get_pending_worklog(self):   
        token = get_token()

        r = requests.get('http://127.0.0.1:5001/worklog/pending', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                } 
        )
        self.assertEqual('<Response [200]>', str(r))

    def test_get_user_worklog(self):   
        token = get_token()

        r = requests.get('http://127.0.0.1:5001/worklog/pending', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                } 
        )
        self.assertEqual('<Response [200]>', str(r))


    def test_worklog(self):
        test_post_worklog(self)
        test_repeated_worklog(self)
        test_put_worklog(self)
        test_edit_state_worklog(self)
        test_delete_worklog(self)
    
    def test_post_evaluation(self):
        token = get_token()

        url = "http://127.0.0.1:5001/evaluation"

        payload = {
            "comment": "Nice",
            "score": "5"
        }

        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("POST", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

    def test_get_evaluation(self):
        token = get_token()

        url = "http://127.0.0.1:5001/evaluation"

        payload = {
            "comment": "Nice",
            "score": "5"
        }

        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("GET", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

    def test_get_events(self):
        token = get_token()

        url = "http://127.0.0.1:5001/evaluation"
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("GET", url, headers=headers)

        self.assertEqual('<Response [200]>', str(r))

    def test_events(self):
        test_post_event(self)
        test_delete_event(self)

    def test_post_course(self):
        token = get_token()

        url = "http://127.0.0.1:5001/course"

        payload = {
            "code": "CE-9999",
            "name": "Curso",
            "group": "10"
        }

        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("POST", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

    def test_get_events(self):
        token = get_token()

        url = "http://127.0.0.1:5001/course"
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("GET", url, headers=headers)

        self.assertEqual('<Response [200]>', str(r))


if __name__ == '__main__':
    unittest.main()
