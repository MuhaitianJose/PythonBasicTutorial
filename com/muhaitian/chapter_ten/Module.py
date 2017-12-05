from com.muhaitian.chapter_sixteen import DocTest

value = {'muhaitian': 'jose'}


def hello():
    print "Hello, world!"


def test():
    hello()


if __name__ == '__main__':
    print __name__
    test()