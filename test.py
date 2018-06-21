import socket
import sys
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
port = 1000
#host_ip = socket.gethostbyname('www.google.com')
host_ip = '10.101.44.47'
s.connect((host_ip, port))
print ("the socket has successfully connected to google \
on port == %s" %(host_ip))
print()s
