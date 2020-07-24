import unittest
import requests
from flask import jsonify
from requests.auth import HTTPBasicAuth

class TestStringMethods(unittest.TestCase):

    def test_good_login(self):

        r = requests.get('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('Admin', 'admin'))
        self.assertEqual('<Response [200]>', str(r))        


    def test_bad_login(self):

        r = requests.get('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('Admin', 'error'))
        self.assertEqual('<Response [401]>', str(r))        


if __name__ == '__main__':
    unittest.main()
