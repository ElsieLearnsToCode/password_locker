#!/usr/bin/env python3.

import random

from user import User

from credentials import Credentials

def create_user(user_name, password):

    """
    Method that lets a user create a new user account from the User class.
    """
    new_user = User(user_name, password)
    return new_user

def generate_random_password():
    """
    Method that generates a password on behalf of the user
    """
    suggested_password = User.generate_password()
    return suggested_password

def save_user(user):
    """
    Method that saves the newly created user account.
    """
    User.save_users(user)

def authenticate_user(user_name,password):
	"""
	Function that verifies the existance of the user before creating credentials
	"""
	check_user = Credentials.check_user(user_name, password)
	return check_user


def new_credential(website, user_name, password):
    """
    Method that lets a user create new credentials.
    """
    new_credential = Credentials(website, user_name, password)
    return new_credential

def save_credential():

    """
    Method that adds user-generated credentials to the empty credentials list.
    """
    Credentials.save_user_credentials

def display_credentials ():
    """
    Method that displays a user's credentials that are saved in their passlock accounts
    """
    return Credentials.existing_credentials

#The main function that allows us to call all the functions in the app.
def main():
    print("Dear User, Welcome to PasswordLocker... What is your name?")
    user_name = input("Enter your name: ")
    print(f"Hello {user_name},What would you like to do today?")
    print("\n")

    while True:
            print("Please choose and enter a shortcode: \n ca - create an account \n si - sign in to existing account \n ex - exit PasswordLocker")
            print("\n")


            user_choice = input("Enter short code:")
            if user_choice == "ca":
                print("~" *50)
                print("create an account")
                print("~" *50)

                print("Enter user_name")
                user_name = input()
                print("*" *50)

                print("Enter password")
                password = input()
                print("*" *10)

                save_user(create_user(user_name, password)) #create and save new user


                print ('\n')
                print(f"New Account {user_name} {password} successfully created")
                print ('\n')

            elif user_choice  == 'si':
                print("Please enter your Username and Password to log in:")
                user_name = input("Enter Your Username: ")
                password = input("Enter Your Password: ")
                current_user = authenticate_user(user_name,password)
                if current_user == user_name:
                    print(f"Hello, {user_name}. Welcome to your Password Locker account")
            
            else:
                print("We hate to see you leave.")
                break


            while True:
                print("Use these short codes:\n cn - Create a new credential \n ds - Display My Credentials \n ex - Exit Password Locker \n")
                user_choice = input("Enter a shortcode to proceed")

                if user_choice == "cn":
                    print("You have chosen to create a new credential")
                    print("Please enter the website for which to create credentials")
                    website = input("Enter the name of the website: ")
                    print("Please enter the username that you use on the website above")
                    user_name = input("")
                    print("Please enter the password that you use on the website above")
                    password = input()

                    save_credential(new_credential(website, user_name, password)) #create and save new credential
                    print('\n')
                    print(f"New Credential consiting of {website}, {user_name}, and {password} created successfully")
                    print ('\n')

                elif user_choice == "ds":
                    if display_credentials():
                        print("This is the list of all the websites that you have saved with Password Locker: ")
            
                    for website in display_credentials():
                        print(f" website:{website} \n User Name:{user_name}\n Password:{password}")
                    
                    else:
                        print("Sike! There are no credentials to view yet :-(")
                

                else:
                    if user_choice == "ex":
                        print("We are sad to see you leave. We hope to see you soon!")
                        break
            

            


                            





            

    

if __name__ == '__main__':
    main()