import socket
import os
import re
import time

PROJECT_ROOT = './Root_dir'
Host = '127.0.0.1'
PORT = 4444
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:

            s.bind((Host, PORT))
            throw_error("Server Binded")

        except socket.error as msg:
            throw_error(str(msg))
            return 1
        s.listen()
        throw_error("Server Listening")

        con,addr=s.accept()
        with con:
            throw_error("Server Connected with {} {}".format(con,addr))
            while True:
                data = client.recv(4096)
                print(data.decode())
                if not data:break
                sdata = ("Hi we are the server ".encode())
                data = client.recv(4096)
                print(data.decode())


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
start_server()