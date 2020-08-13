import unittest
import requests
from flask import jsonify
from requests.auth import HTTPBasicAuth

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


if __name__ == '__main__':
    unittest.main()
