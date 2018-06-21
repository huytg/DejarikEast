import socket

HOST = '10.8.101.16'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(5)
s.sendall(b'hi Banks')
