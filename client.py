import socket
from main import throw_error
port = 4444
host = '127.0.0.1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
throw_error("Intialised")

client.connect((host, port))
throw_error("sent req" )
client.send("Hi i am Artticus".encode('utf-8'))
client.recv(4096)
sdata = client.recv(4096)
print(sdata.decode('utf-8'))
client.send(input(" send message ").encode('utf-8'))