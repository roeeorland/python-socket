import socket
import os
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--port")
args = parser.parse_args()

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = int(args.port) #65432     # Port to listen on (non-privileged ports are > 1023)
print(f"port is:{PORT}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()

        with conn:

            print('Receiving data', addr)
            # with open('received_file.txt', 'wb') as f:
                #f.seek(0)
            while True:
                data = conn.recv(4096)
                if not data:
                    print('removed')
                    break
                f = open('received_file.txt', 'ab')
                #f.seek(0)
                f.write(data)
                if data[0] == 116:
                    print('complete')
                    f.close()
                    time.sleep(25)
                    try:
                        # f.close()
                        os.remove('received_file.txt')
                        with open('received_file.txt', 'wb') as out:
                            out.seek(1024 - 1)
                            out.write(b"\0")
                        # with open('received_file.txt', 'wb') as f:
                        #     continue
                    except:
                        print('file not there')
                    #except:
                     #   continue
                #os.remove('received_file.txt')

                #conn.sendall(data)
            #conn.close()
