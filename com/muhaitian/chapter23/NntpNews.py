# -*-coding:gbk-*-
from nntplib import  NNTP
server = NNTP('news.foo.bar')
print server.group('comp.lang.python.announce')[1]