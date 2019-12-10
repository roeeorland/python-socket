import socket
import time
import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--port")
parser.add_argument("--host")
args = parser.parse_args()
HOST = args.host  # '127.0.0.1'  # The server's hostname or IP address
PORT = int(args.port)  #12345        # The port used by the server
print(f"host is: {HOST}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
   #     s.connect((HOST, PORT))
        time.sleep(random.randrange(15)
        with open('input.txt', 'rb') as f:
            l = f.read(4096)
            i = 1
            while l:
                s.send(l)
                print(f'sent part {i}')
                i += 1
                l = f.read(4096)
            #s.sendall(b'Hello, world')
            s.send(b'transfer complete')
            print('file transfer complete')
            time.sleep(15)
            #data = s.recv(1024)
        #print('client received')
       # s.close()

    print('Received', repr(data))
