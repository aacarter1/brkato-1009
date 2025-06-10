# write a method to get the username and password from a user with security built in
import getpass


def get_username_password():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    return username, password