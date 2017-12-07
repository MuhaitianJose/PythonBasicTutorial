# -*-coding:gbk-*-
from xml.sax.handler import ContentHandler

from xml.sax import parse

import os


class TestHandler(ContentHandler):
    in_headline = False

    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, content):
        if self.in_headline:
            self.data.append(content)


def printWebsite():
    headlines = []
    parse('website.xml', TestHandler(headlines))
    print 'The following <h1> elements were found:'
    for h in headlines:
        print h


class PageMaker(ContentHandler):
    passthrough = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>%s</title>\n' % attrs['title'])
            self.out.write('</head><body>\n')
        elif self.passthrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' %s="%s"' % (key, val))
            self.out.write('>')

    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</%s>' % name)

    def characters(self, content):
        if self.passthrough: self.out.write(content)


def writeHtmlFile():
    parse('website.xml', PageMaker())


# writeHtmlFile()


class Dispatcher:
    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs)

    def endElement(self, name):
        self.dispatch('end', name)

    def dispatch(self, prefix, name, attrs=None):
        mname = prefix + name.capitalize()
        dname = 'default' + prefix.capitalize()
        method = getattr(self, mname, None)
        # print "fdfgfdgdfg",method
        if callable(method):
            args = ()
        else:
            method = getattr(self, dname, None)
            args = name,
        if prefix == 'start':
            print args
            args += attrs,
        if callable(method):
            print method,args
            method(*args)


# class TestHandler(Dispatcher, ContentHandler):
#     def startPage(self, attrs):
#         print 'Beginning page', attrs['name']
#
#     def endPage(self):
#         print 'Ending page'
#
#     def writeHeader(self, title):
#         self.out.write("<html>\n <head>\n  <title>")
#         self.out.write(title)
#         self.out.write("</title>\n  </head>\n <body>\n")
#
#     def writeFooter(self):
#         self.out.write("\n   </body>\n</html>\n")


class WebsiteConstructor(Dispatcher, ContentHandler):
    passthrough = False

    def __init__(self, directoty):
        self.directoty = [directoty]
        self.ensureDirectoty()

    def ensureDirectoty(self):
        path = os.path.join(*self.directoty)
        if not os.path.isdir(path): os.makedirs(path)

    def characters(self, content):
        if self.passthrough: self.out.write(content)

    def defaultStart(self, name, attrs):
        if self.passthrough:
            self.out.write('<' + name)
            try:
                for key, val in attrs.items():
                    self.out.write(' %s="%s"' % (key, val))
            except AttributeError:
                print 'NoneType'
            self.out.write('>')

    def defaultEnd(self, name):
        if self.passthrough:
            self.out.write('</%s>' % name)

    def startDirectory(self, attrs):
        self.directoty.append(attrs['name'])
        self.ensureDirectoty()

    def endDirectory(self):
        self.directoty.pop()

    def startPage(self, attrs):
        filename = os.path.join(*self.directoty + [attrs['name'] + '.html'])
        self.out = open(filename, 'w')
        self.writeHeader(attrs['title'])
        self.passthrough = True

    def endPage(self):
        self.passthrough = False
        self.writeFooter()
        self.out.close()

    def writeHeader(self, title):
        self.out.write("<html>\n <head>\n  <title>")
        self.out.write(title)
        self.out.write("</title>\n  </head>\n <body>\n")

    def writeFooter(self):
        self.out.write("\n   </body>\n</html>\n")


def writeByMix():
    parse('website.xml', WebsiteConstructor('public_html'))


writeByMix()
