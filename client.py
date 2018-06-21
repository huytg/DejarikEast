import socket

HOST = '10.8.101.56'
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(5)
s.sendall(b'hi Banks')
