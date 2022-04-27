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







if __name__ == '__main__':
    unittest.main()