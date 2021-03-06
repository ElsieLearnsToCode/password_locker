#!/usr/bin/env python3.8

class Credentials:
    
    existing_credentials = []

    """
    Method that defines the attributes of each credential that a user creates
    """

    def __init__(self, website, user_name, password):
        
        self.website = website
        self.user_name = user_name
        self.password = password

    def save_user_credentials(self):
        """
        Method that saves the user's credentials
        """  

        Credentials.existing_credentials.append(self)
    
    def view_user_credentials(self):
        """
        This method allows a user to view how their details are saved on the app 
        """
        return Credentials.existing_credentials

    def view_account_details(self, website):
        """
        This method allows the user to view the details of a given account saved in the credentials list
        """
        for credential in Credentials.existing_credentials:
            if (credential.website == website):
                return credential

    def delete_credentials(self):
        """
        Method that allows a user to delete their credentials from the app
        """
        Credentials.existing_credentials.remove(self)

    @classmethod
    def view_user_credentials(cls):
        """
        function that displays user credentials
        """
        return cls.existing_credentials
    
    @classmethod
    def verify_user(cls, user_name, password):
        """
        function that checks if the name and password of a user match entries in the users list
        """
        existing_user = ""
        for user in Credentials.existing_credentials:
            if (user.user_name == user_name and user.password ==password):
                existing_user = user.user_name
                return existing_user
		            