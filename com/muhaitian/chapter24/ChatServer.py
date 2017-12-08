# -*-coding:gbk-*-
import asyncore
import socket
from asynchat import async_chat
from asyncore import dispatcher


class ChatServer(dispatcher): pass


def testSample_01():
    s = ChatServer()
    asyncore.loop()


class ChatServer_02(dispatcher):
    def handle_accept(self):
        conn, addr = self.accept()
        print 'Connection attempt from', addr[0]


def testSample_02():
    s = ChatServer_02()
    s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 5005))
    s.listen(5)
    asyncore.loop()


PORT = 5005


class ChatServer_03(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        print 'Connection attempt from', addr[0]


def testSample_02():
    s = ChatServer_03(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


class ChatSession(async_chat):
    def __init__(self, sock):
        async_chat.__init__(self, sock)
        self.set_terminator("\r\n")
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        print line


class ChatServer_04(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn))


def testChatSession():
    s = ChatServer_04(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print


NAME = 'TestChat'


class ChatSession_05(async_chat):
    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\r\n')
        self.data = []
        #         �ʺ���
        self.push('Welcome to %s\r\n' % self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        """
        �������һ����ֹ����Ҳ����ζ�Ŷ�����һ���������У�����㲥��ÿ���ˡ�
        :return:
        """
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)


class ChatServer_06(dispatcher):
    """
    �������Ӳ��Ҳ��������Ự���࣬�����ᴦ�������Ự�Ĺ㲥
    """

    def __init__(self, port, name):
        #  Standard setup tasks
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession_05(self, conn))


def testChatSession():
    s = ChatServer_06(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print


class CommandHandler:
    """
    �����ڱ�׼����cmd��Cmd�ļ���������
    """

    def unknown(self, session, cmd):
        session.push('Unknown command:%s\r\n' % cmd)

    def handle(self, session, line):
        if not line.strip(): return
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        meth = getattr(self, 'do_' + cmd, None)
        try:
            meth(session, line)
        except TypeError:
            self.unknown(session, cmd)


class EndSession(Exception): pass


class Room(CommandHandler):
    """
    ���԰���һ�������û����Ự���ķ��ͻ���������������������͹㲥��
    """

    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        self.sessions.append(session)

    def remove(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line)

    def do_logout(self, session, line):
        raise EndSession


class LoginRoom(Room):
    """
    Ϊ�ո������ϵ��û�׼���ķ���
    """

    def add(self, session):
        Room.add(self, session)
        # ���û�����ʱ���ʺ���������
        self.broadcast('Welcome to %s\r\n' % self.server.name)

    def unknown(self, session, cmd):
        # ����δ֪�������login ����logout���һ�У�
        # �ᵼ��һ������
        session.push('Please log in\nUse"login <nick>"\r\n')

    def do_login(self, session, line):
        name = line.strip()
        # ȷ���û����������֣�
        if not name:
            session.push('Please enter a name\r\n')
        # ȷ���û���û�б�ʹ��
        elif name in self.server.users:
            session.push('The name "%s" is taken.\r\n' % name)
        else:
            # ����û�����⡣���Դ洢�ڻỰ�У�����
            # ���û��ƶ�����������
            session.name = name
            session.enter(self.server.main_room)


class ChatRoom(Room):
    """
    Ϊ���û��໥����׼������
    """

    def add(self, session):
        # ���������������û����룺
        self.broadcast(session.name + 'has entered the room.\r\n')
        self.server.users[session.name] = session
        Room.add(self, session)

    def remove(self, session):
        Room.remove(self, session)
        # �������������û��뿪��
        self.broadcast(session.name + 'has left the room.\r\n')

    def do_say(self, session, line):
        self.broadcast(session.name + ':' + line + '\r\n')

    def do_look(self, session, line):
        """����look������������ڲ鿴˭�ڷ�����"""
        session.push('The following are in this room:\r\n')
        for other in self.sessions:
            session.push(other.name + '\r\n')

    def do_who(self, session, line):
        """����who�������������˭��¼��"""
        session.push('The following are logged in:\r\n')
        for name in self.server.users:
            session.push(name + '\r\n')


class LogoutRoom(Room):
    """
    Ϊ���û�׼���ļ򵥷��䣬ֻ���ڽ��û����ӷ������Ƴ���
    """

    def add(self, session):
        # ���Ự���û�������Ҫɾ����LogoutRoomʱ
        try:
            del self.server.users[session.name]
        except KeyError:
            pass


class ChatSession_06(async_chat):
    """
    ���Ự������͵��û�ͨ�š�
    """

    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    def enter(self, room):
        # �ӵ�ǰ�����Ƴ�����self��,���ҽ�������ӵ�
        # ��һ������......
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:
            self.room.handle(self, line)
        except EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))


class ChatServer_07(dispatcher):
    """
    ֻ��һ����������������
    """

    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession_06(self, conn)


def testChatServer_07():
    s = ChatServer_07(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print
