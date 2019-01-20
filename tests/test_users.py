import datetime
from tests import BaseTestCase
import json

class TestUsers(BaseTestCase):

    def test_signup(self):
        response = self.test_client.post('/api/v1/signup', json=self.users)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            data['message'], "Successfully signedup with ireporter")
        self.assertEqual(data['data']['firstname'], "deb")
        self.assertEqual(data['data']['othernames'], "mercy")
        self.assertEqual(data['data']['username'], "jhku")
        self.assertEqual(data['data']['phoneNumber'], 1111111111)


    def test_signup_with_no_firstname(self):
        user = {"firstname": " ",
                "lastname": "kalungi",
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Enter firstname')

    def test_signup_with_Iinvalid_firstname(self):
        user = {"firstname": 4546,
                "lastname": "kalungi",
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'firstname should be a string')

    def test_signup_with_no_lastname(self):
        user = {"firstname": "frae",
                "lastname": " ",
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Enter lastname')

    def test_signup_with_Iinvalid_lastname(self):
        user = {"firstname": "4546",
                "lastname": 4564,
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'lastname should be a string')

    def test_login(self):
        """method for testing the login"""
        user = {"firstname": "4546",
                "lastname": "4564",
                "othernames": "Nsubuga",
                "email": "kalungi2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfuka",
                "isAdmin": "true",
                "password": "secrets"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        login = {"username": "nanfuka",
                 "password": "secrets"}
        response = self.test_client.post('/api/v1/login', json=login)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        # self.assertEqual(
        #     data[, {'message': 'you have logged in successfully',
        #               'status': 201})

        # logins = {"username": "nanfuks",
        #           "password": "secres"}
        # response = self.test_client.post('/api/v1/login', json=logins)
        # data = json.loads(response.data)
        # self.assertEqual(response.status_code, 404)
        # self.assertEqual(
        #     data, {"error": "user with such credentials does not exist",
        #            'status': 404})