from app.models.users import Ti, users
from flask import Flask, jsonify, request, json
import re
from functools import wraps
import jwt

userkey = 'amauser'

class User():

    def __init__(self):
        """This method initialises the list in which all user details will \
        be kept. Innitially, the list is empty
        """
        self.user_list = []

    def signup(self, *args):
        """This method innitialises all the attributes that will be used in \
        the creation of a user"""
        self.firstname = args[0]
        self.lastname = args[1]
        self.othernames = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.isAdmin = args[6]
        self.password = args[7]

        ti = Ti(*args)
        newuser = ti.get_dictionary()

        users.append(ti.get_dictionary())
        return newuser

    def login(self, username, password):
        """method for logging in the registered none admin-user"""
        for user in users:
            if user['username'] == username and user['password'] == password:
                return {"status": 201,
                        "message": "you have logged in successfully"}

    def adminlogin(self):
        """method for logging in the adminstrator"""
        for user in users:
            if user['username'] == 'admin' and user['password'] == 'ohpriz':
                return {"status": 201,
                        "message": "you have successfully logged in as the adminstrator"}


    def check_repitition(self, username, email, password):
        """This method checks through the list for values to avoid a user 
            from regestering twice
        """
        for user in users:
            if user['username'] == username:
                return "Username already exists, choose another one"
            elif user['email'] == email:
                return "Email already exists, choose another one"
            elif user['password'] == password:
                return "password already exists, choose another one"
            elif len(password) < 4:
                return "password strength is too weak"

    def customer_token(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 404
            try:
                jwt.decode(token, userkey)
            except:
                return jsonify({'message': 'Token is invalid'}), 404
            return f(*args, **kwargs)
        return decorated
