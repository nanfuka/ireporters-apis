# import unittest
# from app.views.views import app
# import json
# import datetime


# class Basetest(unittest.TestCase):

#     def setUp(self):
#         """Method for innitialising app for testing"""
#         self.app = app

#         self.test_client = app.test_client()

#         self.report = {"createdby": 2,

#                        "location": "22.98 33.25",
#                        "status": "draft",
#                        "images": "imagelocation",
#                        "videos": "videolocation",
#                        "comment": "this is over recurring",
#                        "incident_type": "redflag"
#                        }

#         self.user = {"firstname": "debrah",
#                      "lastname": "kalungi",
#                      "othernames": "Nsubuga",
#                      "email": "kalungi2k6@yahoo.com",
#                      "PhoneNumber": 777777,
#                      "username": "nanfuka",
#                      "isAdmin": "true",
#                      "password": "secrets"
#                      }, {
#                      "firstname": "debrah",
#                      "lastname": "kalungi",
#                      "othernames": "Nsubuga",
#                      "email": "kalungji2k6@yahoo.com",
#                      "PhoneNumber": 777777,
#                      "username": "nanjfuka",
#                      "isAdmin": "true",
#                      "password": "sejhcrets"
#                      }
#         self.login = {"username": "nanfuka",
#                       "password": "secrets"}