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






if __name__ == '__main__':
    unittest.main()