import socket
import winsound
import time


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Input your message: ')
        if message == '!':
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received' + (data.decode()))
        sound = str(data.decode())
        print(sound)
        for i in data.decode():
            print(i)
            if i == '.':
                winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
                time.sleep(0.1)
            elif i == '-':
                winsound.Beep(1000, 600)  # Beep at 1000 Hz for 100 ms
                time.sleep(0.1)
            elif i == ' ':
                pass

        # winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
        # winsound.Beep(1000, 400)  # Beep at 1000 Hz for 100 ms




