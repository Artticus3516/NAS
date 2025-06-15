import socket
import os
import re
import time

def throw_error(text):
    print('-'*len(text))
    print(text)
    print('-'*len(text))
def gen_statements(text,obns):
    print('-'*len(text))
    print(text,'for user: {}'.format([obns.user]))
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
        gen_statements("User created",self)
    def allot_space(self,allocation):
        os.mkdir('./Root_dir_{}'.format(self.user))


new_user = user("Artticus","Niggarmaarda","artticus9@gmail.com",50)