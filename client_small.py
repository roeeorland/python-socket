import socket
import time
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65437        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
   #     s.connect((HOST, PORT))
        time.sleep(5)
        s.sendall(b'Hello, world')
        print('client sent')
        data = s.recv(1024)
        print('client received')
       # s.close()

    print('Received', repr(data))
