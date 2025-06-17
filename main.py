import socket
import os
import re
import time

PROJECT_ROOT = './Root_dir'


def initialise_user(userr,password,email,limit):
    userr = user(userr,password,email,limit)
    print("User created Successfully")
    return user
def throw_error(text):
    print('-'*len(text))
    print(text)
    print('-'*len(text))




class user:
    def __init__(self,username,password,email,limit):
        if re.fullmatch(r'^[A-Za-z0-9_]@[A-Za-z0-9]+\.(com|org|edu)$',email) :
            throw_error("Invalid Email for user: {}".format([username,email]))
            raise(ValueError("Invalid Email for user: {}".format([username,email])))
        self.user = username
        self.password = password
        self.email = email
        self.allocation = limit
        print(f"{user} has been created with {[username,password,email,limit]}")
        current_user_dir = os.path.join(PROJECT_ROOT, 'Users_Data', 'Root_dir-{}'.format(self.user))
        os.makedirs(current_user_dir,exist_ok=True)






initialise_user("Artticus","Niggarmaarda","artticus9@gmail.com",50)