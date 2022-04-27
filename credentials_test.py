#!/usr/bin/env python3.8
import unittest

from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the Credentials class behaviour.
    args: 
    unittest.Testcase class that helps in creating test cases.
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials = Credentials("twitter", "Stella", "ABCDEFGH")

    def test_innit(self):
        """
        test_innit test case tests if the object is initialized properly.
        """
        self.assertEqual(self.new_credentials.website, "twitter")
        self.assertEqual(self.new_credentials.user_name, "Stella")
        self.assertEqual(self.new_credentials.password, "ABCDEFGH")

    def test_save_user_credentials(self):
        """
        test if user credentials are being saved properly
        """
        self.new_credentials.save_user_credentials() #saving the new users
        self.assertEqual(len(Credentials.existing_credentials), 1)

    def tearDown(self):
        """
        tearDown method that does cleanup after each test has run.
        """
        Credentials.existing_credentials = []
    
    def test_view_user_credentials(self):
        """
        method that tests whether we can display a users credentials
        """
        self.new_credentials.save_user_credentials()
        test_credentials = Credentials("Twitter", "Brian", "klmNOPQR")
        test_credentials.save_user_credentials()
        self.assertEqual(Credentials.view_user_credentials(), Credentials.existing_credentials)

    def test_view_account_details(self):
        """
        method thats tests if the user to view the details of a given account saved in the credentials list
        """
        self.new_credentials.view_account_details("Brian")
        test_credentials = Credentials("Twitter", "Brian", "klmNOPQR")
        test_credentials.view_account_details("Brian")
        self.assertEqual(Credentials.view_account_details(), Credentials.existing_credentials)

    def test_delete_credentials(self):

        """
        method that tests if a user can delete their credentials
        """

        self.new_credentials.save_user_credentials()
        test_credentials = Credentials ("Instagram", "Janice", "56789110") #create new credential

        test_credentials.save_user_credentials()
        self.new_credentials.delete_credentials() #Deleting a new credential
        self.assertEqual(len(Credentials.existing_credentials),1)





if __name__ == '__main__':
    unittest.main()