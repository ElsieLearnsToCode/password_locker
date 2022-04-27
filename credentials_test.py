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






if __name__ == '__main__':
    unittest.main()