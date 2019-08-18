import socket

HOST = '172.31.25.111'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
s.close()
