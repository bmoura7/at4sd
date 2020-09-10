import socket
import sys
from generate_json import create_json

json_str = create_json()
print(json_str)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    sock.sendall(json_str.encode())


finally:
    print('closing socket')
    sock.close()