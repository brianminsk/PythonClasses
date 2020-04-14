import socket
import sys

try:
    port = int(sys.argv[1])
except IndexError:
    print("Please include a port number, eg: python serve.py 50000")
    exit(-1)

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", port))

while True:
    try:
        response = client_socket.recv(4096).decode()
    except ConnectionAbortedError:
        print("Connection closed by host.")
        break

    print(response)

    if response.startswith("OK! Goodbye"):
        exit(-1)

    my_message = input("> ").encode('utf-8') + b'\n'
    client_socket.sendall(my_message)
