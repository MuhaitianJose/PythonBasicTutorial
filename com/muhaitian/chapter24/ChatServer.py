# -*-coding:gbk-*-
import asyncore
from asyncore import dispatcher


class ChatServer(dispatcher): pass


def testSample_01():
    s = ChatServer()
    asyncore.loop()


class ChatServer_02(dispatcher):
    