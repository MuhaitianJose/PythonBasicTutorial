# -*-coding:gbk-*-
import socket
from SocketServer import StreamRequestHandler, TCPServer, ForkingMixIn, ThreadingMixIn
from urllib import urlopen, urlretrieve, urlcleanup

import select
from twisted.internet.protocol import Protocol


def startSocketService():
    server = socket.socket()
    host = socket.gethostname()
    print host
    port = 1234
    server.bind((host, port))
    server.listen(5)
    while True:
        c, addr = server.accept()
        print 'Got connect from', addr
        c.send('Thank you for connecting')
        c.close()


def sendSomethingtoService():
    client = socket.socket()
    host = socket.gethostname()
    port = 1233
    client.connect((host, port))
    print client.recv(1024)
    print'over'


# muhaitian = urlopen('file:H:\PythonWorkSpace\muhaitian.txt')
# webpage = urlopen('http://www.python.org')
# print 'muhaitian', muhaitian.readlines()
# print 'webpage', webpage.readlines()
#
# urlretrieve('http://www.python.org', 'H:\PythonWorkSpace\muhaitian.html')
# urlcleanup()


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank You for connecting')


# Small server write by SocketServer
def startSocketServer():
    server = TCPServer(('ip', 1234), Handler)
    server.serve_forever()


# ==========================================================
class Server2(ForkingMixIn, TCPServer):
    pass


class Handler2(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connect from', addr
        self.wfile.write('Thank you for connecting ForkingMixIn')


class Server3(ThreadingMixIn, TCPServer):
    pass


class Handler3(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connect from', addr
        self.wfile.write('Thank you for connecting ThreadingMixIn')


def startSocketServer2():
    server = Server2(('ip', 1234), Handler2)
    server.serve_forever()


def startSocketServer3():
    server = Server3(('ip', 1234), Handler3)
    server.serve_forever()


# ʹ����select�ļ򵥷�����



def useSelect():
    ser = socket.socket()
    host = socket.gethostname()
    port = 1233
    ser.bind((host, port))
    ser.listen(5)
    inputs = [ser]
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is ser:
                c, addr = ser.accept()
                print 'Got connection from'
                inputs.append(c)
            else:
                try:
                    data = r.recv(1024)
                    disconnected = not data
                except socket, error:
                    disconnected = True
                if disconnected:
                    print r.getpeername(), 'disconnected'
                    inputs.remove(r)
                else:
                    print 'data'
# poll��ʹ�ã�window�²���ʹ�ã�
# POLLIN����ȡ�����ļ�������������
# POLLPRI����ȡ�����ļ��������Ľ�������
# POLLOUT���ļ��������Ѿ�׼�������ݣ�д��ʱ���ᷢ������
# POLLERR�����ļ��������йصĴ������
# POLLHUP���������Ӷ�ʧ
# POLLNVAL����Ч��������û�д�

# =======================================================================
# twisted����������
class SimpleLogger(Protocol):
    def dataReceived(self, data):
        print data

    def connectionLost(self, reason):
        print self.transport.client,'disconnected'

    def connectionMade(self):
       print 'Got connection from',self.transport.client