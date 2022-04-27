#!/usr/bin/env python3.8

from user import User

from credentials import Credentials

def create_user(user_name, password):

    """
    Method that lets a user create a new user account from the User class.
    """
    new_user = User(user_name, password)
    return new_user