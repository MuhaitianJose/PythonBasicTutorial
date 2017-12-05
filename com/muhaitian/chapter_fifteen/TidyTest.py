from HTMLParser import HTMLParser
from subprocess import Popen, PIPE
from urllib import urlopen

import BeautifulSoup as BeautifulSoup


def testtidy():
    text = open('messy.html').read()
    tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    tidy.stdin.write(text)
    tidy.stdin.close()

    print tidy.stdout.read()


class Scraper(HTMLParser):
    in_h3 = False
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3':
            self.in_h3 = True
        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False
        if tag == 'a':
            if self.in_h3 and self.in_link:
                print '%s (%s)' % (''.join(self.chunks), self.url)
            self.in_link = False

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)


def testHTMLParser():
    text = urlopen(r'http://python.org/community/jobs').read()
    print text
    parser = Scraper()
    parser.feed(text)
    parser.close()


def testBeautifulSoup():
    text = urlopen(r'http://python.org/community/jobs').read()
    soup = BeautifulSoup(text)
    jobs = set()
    for header in soup('h3'):
        links = header('a', 'reference')
        if not links: continue
        link = links[0]
        jobs.add('%s (%s)' % (link.string, link['href']))
    print '\n'.join(sorted(jobs, key=lambda s: s.lower))
