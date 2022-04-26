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
        Set up method to run before each test case.
        """
        self.new_user = User("ElsieAkoth", "12345678")
    
    def test_innit(self):
        """
        test_innit test case tests if the object is initialized properly.
        """
        self.assertEqual(self.new_user.user_name, "ElsieAkoth")
        self.assertEqual(self.new_user.password, "12345678")
    
    def test_save_users(self):
        """
        test if users are being saved properly
        """
        self.new_user.save_users() #saving the new users
        self.assertEqual(len(User.users_list), 1)
