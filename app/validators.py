import re


class Validators:
    def validate_strings(self, *args):
        firstname = args[0]
        lastname = args[1]
        othernames = args[2]
        username = args[3]
        data = args[4]

        if not isinstance(firstname, str):
            return "firstname should be a string"

        elif not firstname or firstname.strip() == "":
            return "Enter firstname"

        if not isinstance(othernames, str):
            return "othernames should be a string"
        if not othernames or othernames.strip == "":
            data['othernames'] == 'none'

        elif not isinstance(lastname, str):
            return "lastname should be a string"
        elif not lastname.strip() or lastname.strip() == "":
            return "Enter lastname"

        if not isinstance(username, str):
            return "username should be a string"
        elif not username or username.strip() == "":
            return "Enter username"

    def validate_email(self, email):
        email_validation = re.compile(
            "(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)")
        if not email:
            return "Enter Email"
        elif not email_validation.match(email):
            return 'Invalid email, it should be in this format; kals@gma.com'

    def validat_numbers(self, phoneNumber):
        if not phoneNumber:
            return "Enter phone number"
        elif not isinstance(phoneNumber, int):
            return "phoneNumber should be made up of numbers"

        # if phoneNumber != 10:
        #     return "digits of the phone number should be 10"

    def validate_boolean(self, isAdmin):
        if isAdmin != 'false' and isAdmin != 'true':
            return "IsAdmin should either be true or false"

    def validate_password(self, password):
        if not password or password.strip == "":
            return "Enter password"
        if len(password) < 6:
            return "Increase the strength of your password"


    def validate_location(self, location):
        """Method where all validations are done"""
        geo_location = re.compile(
            "^[0-9]{2}(.)[0-9]{2}( )[0-9]{2}(.)[0-9]{2}$")

        if not location or location.isspace():
            return 'please enter the location of this redflag'

        elif not geo_location.match(location):
            string1 = 'invalid location, please enter the lat, long cordinates'
            string2 = 'in this formant, 25.22 56.22'
            return string1 + string2

    def validate_input(self, *args):
        """Method where all validations are done"""
        createdby = args[0]
        incident_type = args[1]
        status = args[2]

        if not createdby:
            return 'please enter the id of the creator of this redflag'
        elif not isinstance(createdby, int):
            return 'createdby should be an id of the creator of the redflag'
        elif not incident_type or incident_type.strip() == "":
            return 'Enter a incident type.'
        elif incident_type != "redflag" and incident_type != "intervention":
            return 'Incident type should either be a redflag or intervention.'
        elif status != "draft" and status != "underinvestigation" and status != "resolved" and status != "rejected":
            strg1 = 'status should either be draft'
            strg2 = 'underinvestigation, resolved or rejected'
            return strg1 + strg2

    def validate_coment(self, comment):
        """method which validates comment"""
        if not comment or comment.strip() == "":
            return 'Enter the comment'
        if isinstance(comment, int):
            return 'Comment should be a string'

#     def validate_user_details(self, *args):
#         """method which validates user_details"""
#         firstname = args[0]
#         lastname = args[1]
#         email = args[2]
#         username = args[3]
#         password = args[4]
#         phoneNumber = args[5]
#         isAdmin = args[6]
#         othernames = args[7]

#         email_validation = re.compile(
#             "(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)")

#         if not isinstance(firstname, str) or not isinstance(lastname, str)\
#                 or not isinstance(username, str) or \
#                 not isinstance(othernames, str):
#             return "Invalid input, Enter a string"
#         elif not firstname or firstname.isspace() or not lastname or\
#                 lastname.isspace() or not email or email.isspace() or \
#                 not username or username.isspace() or not password or \
#                 password.isspace()or not isAdmin or isAdmin.isspace():
#             return {"message": "Enter only valid data"}
#         elif type(phoneNumber) == str:
#             return "The phone number should be an integer"

#         elif isAdmin != 'false' and isAdmin != 'true':
#             return "IsAdmin should either be true or false"
#         elif not email_validation.match(email):
#             return 'Invalid email, it should be in this format; kals@gma.com'




# # import re


# # class Validators:

# #     def validate_location(self, location):
# #         """Method where all validations are done"""
# #         geo_location = re.compile(
# #             "^[0-9]{2}(.)[0-9]{2}( )[0-9]{2}(.)[0-9]{2}$")

# #         if not location or location.isspace():
# #             return 'please enter the location of this redflag'

# #         elif not geo_location.match(location):
# #             string1 = 'invalid location, please enter the lat, long cordinates'
# #             string2 = 'in this formant, 25.22 56.22'
# #             return string1 + string2

# #     def validate_input(self, *args):
# #         """Method where all validations are done"""
# #         createdby = args[0]
# #         incident_type = args[1]
# #         status = args[2]

# #         if not createdby:
# #             return 'please enter the id of the creator of this redflag'
# #         elif not isinstance(createdby, int):
# #             return 'createdby should be an id of the creator of the redflag'
# #         elif not incident_type or incident_type.isspace():
# #             return 'Enter a redflag.'
# #         elif incident_type != "redflag" and incident_type != "intervention":
# #             return 'Incident type should either be a redflag or intervention.'
# #         elif status != "draft":
# #             return 'status should either be draft,\
# #                 underinvestigation, resolved or rejected'

# #     def validate_coment(self, comment):
# #         if not comment or comment.isspace():
# #             return 'Enter the comment'
# #         if isinstance(comment, int):
# #             return 'Comment should be a string'

# #     def validate_user_details(self, *args):
# #         firstname = args[0]
# #         lastname = args[1]
# #         email = args[2]
# #         username = args[3]
# #         password = args[4]
# #         phoneNumber = args[5]
# #         isAdmin = args[6]
# #         othernames = args[7]

# #         email_validation = re.compile(
# #             "(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)")

# #         if not isinstance(firstname, str) or not isinstance(lastname, str)\
# #                 or not isinstance(username, str) or \
# #                 not isinstance(othernames, str):
# #             return "Invalid input, Enter a string"
# #         elif not firstname or firstname.isspace() or not lastname or\
# #                 lastname.isspace() or not email or email.isspace() or \
# #                 not username or username.isspace() or not password or \
# #                 password.isspace()or not isAdmin or isAdmin.isspace():
# #             return "Enter all items"
# #         elif type(phoneNumber) == str:
# #             return "The phone number should be an integer"

# #         elif isAdmin != 'false' and isAdmin != 'true':
# #             return "IsAdmin should either be true or false"
# #         elif not email_validation.match(email):
# #             return 'Invalid email, it should be in this format; kals@gma.com'
