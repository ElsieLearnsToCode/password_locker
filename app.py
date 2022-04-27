#!/usr/bin/env python3.

import random

from user import User

from credentials import Credentials

def create_user(user_name, password):

    """
    Method that lets a user create a new user account from the User class.
    """
    new_user = User(user_name, password)
    return new_user

def generate_random_password():
    """
    Method that generates a password on behalf of the user
    """
    suggested_password = User.generate_password()
    return suggested_password

