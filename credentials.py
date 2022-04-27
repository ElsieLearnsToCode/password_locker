
class Credentials:
    
    existing_credentials = []

    """
    Method that defines the attributes of each credential that a user creates
    """

    def __init__(self, website, user_name, password):
        
        self.website = website
        self.user_name = user_name
        self.password = password

        