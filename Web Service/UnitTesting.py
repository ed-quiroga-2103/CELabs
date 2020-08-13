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
        test_delete_allnighter(self)

    

if __name__ == '__main__':
    unittest.main()
