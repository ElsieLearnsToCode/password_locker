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

    def tearDown(self):
        """
        tearDown method that does cleanup after each test has run.
        """
        User.users_list = []
    
    def test_save_multiple_user(self):
        """
        Checking if there are multiple users
        """
        self.new_user.save_users()
        test_user = User ("James", "87654321") #assign new user

        test_user.save_users()
        self.assertEqual(len(User.users_list), 2)
    
    def test_delete_user(self):
        """
        test to see if we can remove a user from the users list
    
        """

        self.new_user.save_users()
        test_user = User ("James", "87654321") #assign new user

        test_user.save_users()
        self.new_user.delete_users()
        self.assertEqual(len(User.users_list), 1)
    
    def test_find_user_by_user_name(self):
        """
        test if we can find a user by their username
        """
        self.new_user.save_users()
        test_user = User ("James", "87654321") #assign new user

        test_user.save_users()
        found_user = User.find_by_user_name("James")
        self.assertEqual(found_user.user_name, test_user.user_name)

    
