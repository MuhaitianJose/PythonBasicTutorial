# -*-coding:gbk-*-
import re

from com.muhaitian.chapter_sixteen import DocTest

value = {'muhaitian': 'jose'}


def hello():
    print "Hello, world!"


def test():
    hello()


if __name__ == '__main__':
    print __name__
    test()

emkl=r'\*(.+)\*'
# r'<em>\1<em>'标签中间是数字1不然不能替换
re.sub(emkl,r'<em>\1<em>','*this*')