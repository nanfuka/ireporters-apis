# def test_signup(self):
#         response = self.test_client.post('/api/v1/signup', json=self.user)
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(
#             data['message'], "Successfully signedup with ireporter")
#         self.assertEqual(data['data']['firstname'], "debrah")
#         self.assertEqual(data['data']['othernames'], "Nsubuga")
#         self.assertEqual(data['data']['username'], "nanfuka")
#         self.assertEqual(data['data']['phoneNumber'], 777777)

#     def test_signup_with_invalid_firstname_type(self):
#         user = {"firstname": 123,
#                 "lastname": "kalungi",
#                 "othernames": "Nsubuga",
#                 "email": "kalungi2k6@yahoo.com",
#                 "PhoneNumber": 777777,
#                 "username": "nanfuka",
#                 "isAdmin": "true",
#                 "password": "secrets"
#                 }
#         response = self.test_client.post('/api/v1/signup', json=user)
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(data['error'], "Invalid input, Enter a string")

#     def test_signup_with_no_firstname(self):
#         user = {"firstname": " ",
#                 "lastname": "kalungi",
#                 "othernames": "Nsubuga",
#                 "email": "kalungi2k6@yahoo.com",
#                 "PhoneNumber": 777777,
#                 "username": "nanfuka",
#                 "isAdmin": "true",
#                 "password": "secrets"
#                 }
#         response = self.test_client.post('/api/v1/signup', json=user)
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(data['error'], {'message': 'Enter only valid data'})

#     def test_signup_with_no_lastname(self):
#         user = {"firstname": "frae",
#                 "lastname": " ",
#                 "othernames": "Nsubuga",
#                 "email": "kalungi2k6@yahoo.com",
#                 "PhoneNumber": 777777,
#                 "username": "nanfuka",
#                 "isAdmin": "true",
#                 "password": "secrets"
#                 }
#         response = self.test_client.post('/api/v1/signup', json=user)
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(data['error'], {'message': 'Enter only valid data'})

#     def test_login(self):
#         """method for testing the login"""
#         user = {"firstname": "debrah",
#                 "lastname": "kalungi",
#                 "othernames": "Nsubuga",
#                 "email": "kalungid2k6@yahoo.com",
#                 "PhoneNumber": 777777,
#                 "username": "nanfukas",
#                 "isAdmin": "true",
#                 "password": "secretss"
#                 }
#         response = self.test_client.post('/api/v1/signup', json=user)
#         login = {"username": "nanfukas",
#                  "password": "secretss"}
#         response = self.test_client.post('/api/v1/login', json=login)
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(
#             data[0], {'message': 'you have logged in successfully',
#                       'status': 201})

#         logins = {"username": "nanfuks",
#                   "password": "secres"}
#         response = self.test_client.post('/api/v1/login', json=logins)
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(
#             data, {"error": "user with such credentials does not exist",
#                    'status': 404})