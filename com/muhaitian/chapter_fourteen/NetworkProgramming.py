import socket


def startSocketService():
    server = socket.socket()
    host = socket.gethostname()
    print host
    port = 1234
    server.bind((host, port))
    server.listen(5)
    while True:
        c,addr= server.accept()
        print 'Got connect from',addr
        c.send('Thank you for connecting')
        c.close()
def sendSomethingtoService():
    client = socket.socket()
    host = socket.gethostname()
    port = 1234
    client.connect((host,port))
    print client.recv(1024)
    print'over'