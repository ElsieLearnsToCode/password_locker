#!/usr/bin/env python3.8

"""
create a User class from which we will generate and save new user accounts
"""

class User:
    users_list = [] #empty list, which will hold all users
    """
    Method that defines the attributes of each user account.
    """
    def __init__(self, user_name, password ):
        self.user_name = user_name
        self.password = password