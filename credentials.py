
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
                
