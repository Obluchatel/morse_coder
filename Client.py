import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input('Input your message: ')
    s.sendall(message.encode())
    data = s.recv(1024)

print('Received' + (data.decode()))
