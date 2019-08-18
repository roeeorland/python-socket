import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

client.connect(('172.31.25.111', 8080))
i = 0
while True:  #i<100:
    client.send("I am CLIENT\n")
    from_server = client.recv(4096)
    print(i, ".from_server")
    i += 1
client.close()

