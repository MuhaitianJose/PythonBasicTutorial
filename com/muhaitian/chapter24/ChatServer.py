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
        #         问候语
        self.push('Welcome to %s\r\n' % self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        """
        如果发现一个终止对象，也就意味着读入了一个完整的行，将其广播给每个人。
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
    接受连接并且产生单个会话的类，它还会处理其他会话的广播
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
    类似于标准库中cmd，Cmd的简单命令处理程序
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
    可以包括一个或多个用户（会话）的泛型环境，它负责基本的命令处理和广播。
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
    为刚刚连接上的用户准备的房间
    """

    def add(self, session):
        Room.add(self, session)
        # 当用户进入时，问候他或者她
        self.broadcast('Welcome to %s\r\n' % self.server.name)

    def unknown(self, session, cmd):
        # 所有未知命令（除了login 或者logout外的一切）
        # 会导致一个警告
        session.push('Please log in\nUse"login <nick>"\r\n')

    def do_login(self, session, line):
        name = line.strip()
        # 确保用户输入了名字：
        if not name:
            session.push('Please enter a name\r\n')
        # 确保用户名没有被使用
        elif name in self.server.users:
            session.push('The name "%s" is taken.\r\n' % name)
        else:
            # 名字没有问题。所以存储在会话中，并且
            # 将用户移动到主聊天室
            session.name = name
            session.enter(self.server.main_room)


class ChatRoom(Room):
    """
    为多用户相互聊天准备房间
    """

    def add(self, session):
        # 告诉所有人有新用户进入：
        self.broadcast(session.name + 'has entered the room.\r\n')
        self.server.users[session.name] = session
        Room.add(self, session)

    def remove(self, session):
        Room.remove(self, session)
        # 告诉所有人有用户离开：
        self.broadcast(session.name + 'has left the room.\r\n')

    def do_say(self, session, line):
        self.broadcast(session.name + ':' + line + '\r\n')

    def do_look(self, session, line):
        """处理look命令，该命令用于查看谁在房间内"""
        session.push('The following are in this room:\r\n')
        for other in self.sessions:
            session.push(other.name + '\r\n')

    def do_who(self, session, line):
        """处理who命令，该命令用于谁登录了"""
        session.push('The following are logged in:\r\n')
        for name in self.server.users:
            session.push(name + '\r\n')


class LogoutRoom(Room):
    """
    为单用户准备的简单房间，只用于将用户名从服务器移除。
    """

    def add(self, session):
        # 当会话（用户）进入要删除的LogoutRoom时
        try:
            del self.server.users[session.name]
        except KeyError:
            pass


class ChatSession_06(async_chat):
    """
    单会话，负责和单用户通信。
    """

    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    def enter(self, room):
        # 从当前房间移除自身（self）,并且将自身添加到
        # 下一个房间......
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
    只有一个房间的聊天服务器
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
