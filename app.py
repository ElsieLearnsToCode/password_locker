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

def save_user(user):
    """
    Method that saves the newly created user account.
    """
    User.save_users(user)

def authenticate_user(user_name,password):
	"""
	Function that verifies the existance of the user before creating credentials
	"""
	check_user = Credentials.check_user(user_name, password)
	return check_user


def new_credential(website, user_name, password):
    """
    Method that lets a user create new credentials.
    """
    new_credential = Credentials(website, user_name, password)
    return new_credential

def save_credential():

    """
    Method that adds user-generated credentials to the empty credentials list.
    """
    Credentials.save_user_credentials

def display_credentials ():
    """
    Method that displays a user's credentials that are saved in their passlock accounts
    """
    return Credentials.existing_credentials

