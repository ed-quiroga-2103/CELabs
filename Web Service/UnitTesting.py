import unittest
import requests
from flask import jsonify
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



if __name__ == '__main__':
    unittest.main()
