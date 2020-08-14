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

def get_token2():
    r = requests.post('http://127.0.0.1:5001/login', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                } 
        ,auth=HTTPBasicAuth('Prof', 'Prof'))

    token = r.json()['token']
    return token

# ------------ User ------------------
def test_create_user(self):
        token = get_token()

        url = "http://127.0.0.1:5001/user"

        payload = {

                    "name": "Oscar",
                    "lastname1": "González",
                    "lastname2": "Alfaro",
                    "id_number": "1-1750-XXXX",
                    "password": "password",
                    "email": "racso08@email.com",
                    "phone_number": "831072XX",
                    "university_id": "20171215XX",
                    "user_type": "2"
                }
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("POST", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

def test_create_user2(self):
        token = get_token()

        url = "http://127.0.0.1:5001/user"

        payload = {

                    "name": "Oscar",
                    "lastname1": "González",
                    "lastname2": "Alfaro",
                    "id_number": "1-1750-XXXX",
                    "password": "password",
                    "email": "administrativo@email.com",
                    "phone_number": "831072XX",
                    "university_id": "20171215XX",
                    "user_type": "4"
                }
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("POST", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

def test_login(self):
        token = get_token()

        url = "http://127.0.0.1:5001/login"

        payload = {}
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("POST", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

def test_disable_this_user(self):
        token = get_token2()

        url = "http://127.0.0.1:5001/user/disable"

        payload = {}
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("PUT", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

def test_edit_this_user(self):
        token = get_token2()

        url = "http://127.0.0.1:5001/user"

        payload =   {
                    "name": "Racso",
                    "lastname1": "Gonzalez",
                    "lastname2": "Alfaro ",
                    "id_number": "1-1750-0XXX",
                    "phone_number": "831072XX",
                    "university_id": "2020215XXX"
                    }
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("PUT", url, headers=headers, json = payload)

        self.assertEqual('<Response [200]>', str(r))

# ------------ Reservation ------------------

def test_post_reservation(self):
        token = get_token()

        url = "http://127.0.0.1:5001/reservation"

        payload = {
    
            "description": "Espe",
            "subject": "Subject",
            "requesting_user":"administrativo@email.com",
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
            "requesting_user":"administrativo@email.com",
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
                "id_allnighter":"1"
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

# ------------ Inventory Report ------------------

def test_create_inventory_report(self):
    token = get_token()

    url = "http://127.0.0.1:5001/inventory"

    payload =   {
                    "complete_computers": "5",
                    "incomplete_computers": "4",
                    "number_projectors": "3",
                    "number_chairs": "2",
                    "number_fire_extinguishers": "1",
                    "lab":"F2-09",
                    "description":"Me encontre un paragüas"
                }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("POST", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_delete_this_inventoryreport(self):
    token = get_token()

    url = "http://127.0.0.1:5001/inventory"

    payload =   {
                    "id_report" : "1"
                }
    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("DELETE", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_edit_this_inventoryreport(self):
    token = get_token()

    url = "http://127.0.0.1:5001/inventory"

    payload =   {
                    "old":{
                        "id_report":"1"
                        },
                    "new":{
                        "complete_computers": "5",
                        "incomplete_computers": "4",
                        "number_projectors": "3",
                        "number_chairs": "2",
                        "number_fire_extinguishers": "3",
                        "lab":"F2-10",
                        "description":"Me encontre un celular",
                        "status":"Completed"
                        }
                }
    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("PUT", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

# ------------ Fault Report ------------------

def test_create_fault_report(self):
    token = get_token()

    url = "http://127.0.0.1:5001/fault"

    payload =   {
                    "id_fault_part": "Maquina No. 5",
                    "description": "No enciende",
                    "lab":"F2-09"
                }

    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("POST", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_delete_this_faultreport(self):
    token = get_token()

    url = "http://127.0.0.1:5001/fault"

    payload =   {
                    "id_report" : "1"
                }
    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("DELETE", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_edit_this_faultreport(self):
    token = get_token()

    url = "http://127.0.0.1:5001/fault"

    payload =   {
                    "old":{
                        "id_report":"1"
                        },
                    "new":{
                        "id_fault_part": "Maquina No.6",
                        "description": "Panatallazo azul",
                        "lab":"F2-09",
                        "status":"Completed"
                        }
                }
    
    headers = {
    'Authorization': 'Basic QWRtaW46MTIzNDU=',
    'Content-Type': 'application/json',
    'x-access-token': token
    }

    r = requests.request("PUT", url, headers=headers, json = payload)

    self.assertEqual('<Response [200]>', str(r))

def test_edit_state_faultreport(self):
    token = get_token()

    url = "http://127.0.0.1:5001/fault/state"

    payload =   {
                    "old":  {
                            "id_report" : "1"
                            },
                    "new":  {
                            "status":"Completed"
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

#----------------------------------User-----------------------------------------------
    def test_get_this_user(self):
        token = get_token()

        r = requests.get('http://127.0.0.1:5001/user', 
        headers={
                'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                'Content-Type': 'application/json', 
                'x-access-token': token,
                } 
        )
        self.assertEqual('<Response [200]>', str(r)) 
      
    def test_user(self):
        test_create_user(self)
        test_edit_this_user(self)
        test_disable_this_user(self)

#----------------------------------Reservation---------------------------------------
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
        test_create_user2(self)
        test_post_reservation(self)
        test_repeated_reservation(self)
        test_edit_reservation(self)
        test_delete_reservation(self)

#----------------------------------All-Nighter---------------------------------------
    
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

#----------------------------------Worklog---------------------------------------

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

#---------------------------------- Inventory----------------------------------------
    def test_get_all_inventory(self):  
            token = get_token()

            r = requests.get('http://127.0.0.1:5001/inventory', 
            headers={
                    'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                    'Content-Type': 'application/json', 
                    'x-access-token': token,
                    } 
            )
            self.assertEqual('<Response [200]>', str(r)) 

    def test_get_its_inventory(self):   
            token = get_token()

            r = requests.get('http://127.0.0.1:5001/inventory/user', 
            headers={
                    'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                    'Content-Type': 'application/json', 
                    'x-access-token': token,
                    } 
            )
            self.assertEqual('<Response [200]>', str(r)) 

    def test_inventory(self):
            test_create_inventory_report(self)
            test_edit_this_inventoryreport(self)
            test_delete_this_inventoryreport(self)

#----------------------------------Fault Report---------------------------------------

    def test_get_all_fault(self):   
            token = get_token()

            r = requests.get('http://127.0.0.1:5001/fault', 
            headers={
                    'Authorization': 'Basic QWRtaW46MTIzNDU=', 
                    'Content-Type': 'application/json', 
                    'x-access-token': token,
                    } 
            )
            self.assertEqual('<Response [200]>', str(r)) 

    def test_faults(self):
            test_create_fault_report(self)
            test_edit_this_faultreport(self)
            test_edit_state_faultreport(self)
            test_delete_this_faultreport(self)   


#----------------------------------Evaluation---------------------------------------
    
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

#----------------------------------Events---------------------------------------

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

#----------------------------------Course---------------------------------------

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

    def test_get_course(self):
        token = get_token()

        url = "http://127.0.0.1:5001/course"
        
        headers = {
        'Authorization': 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        'x-access-token': token
        }

        r = requests.request("GET", url, headers=headers)

        self.assertEqual('<Response [200]>', str(r))

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
