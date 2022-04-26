import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the User class behaviour.
    args: 
    unittest.Testcase class that helps in creating test cases.
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("ElsieAkoth", "12345678")
