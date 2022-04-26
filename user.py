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
    
    def save_users(self):
        """
        This method stores the details of each user to the empty users list
        """
        User.users_list.append(self)
    
    def view_user_exists(self):
        """
        This method allows a user to view how their details are saved on the app 
        """
        return User.users_list

    def delete_users(self):
        """
        This method deletes a user's account from the app
        """
        User.users_list.remove(self)

    
    