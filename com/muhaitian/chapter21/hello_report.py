# -*-coding:gbk-*-
from urllib import urlopen

from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing, String, PolyLine
from reportlab.lib import colors

data = [(2007, 8, 113.8, 114.0, 112.7),
        (2007, 9, 112.8, 115.0, 109.7),
        (2007, 10, 111.0, 115.8, 106.0),
        (2007, 11, 109.8, 116.8, 102.8),
        (2007, 12, 107.3, 115.3, 99.3),
        (2008, 1, 105.2, 114.2, 96.2),
        (2008, 2, 104.1, 114.1, 94.1),
        (2008, 3, 99.9, 110.9, 88.9),
        (2008, 4, 94.8, 106.8, 82.8),
        (2008, 8, 91.2, 104.2, 78.2)]


def writeToPdf():
    d = Drawing(100, 100)
    s = String(50, 50, 'Hello, world!', textAnchor='middle')
    d.add(s)
    renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')


def drawLines():
    d = Drawing(100, 100)
    d.add(PolyLine([(45, 45), (55, 55), (55, 45), (45, 55)], strokeColor=colors.blue))
    renderPDF.drawToFile(d, 'polyLine.pdf', 'A simple PDF file')


def drawSunspots():
    d = Drawing(200, 150)
    pred = [row[2] - 40 for row in data]
    high = [row[3] - 40 for row in data]
    low = [row[4] - 40 for row in data]
    times = [200 * ((row[0] + row[1] / 12.0) - 2007) - 110 for row in data]
    d.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
    d.add(PolyLine(zip(times, high), strokeColor=colors.red))
    d.add(PolyLine(zip(times, low), strokeColor=colors.green))
    d.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

    renderPDF.drawToFile(d, 'report.pdf', 'Sunspots')


# 写入文本信息在pdf文件中
# writeToPdf()
# 画折线图
# drawLines()
# 画太阳黑子折线
# drawSunspots()
URL = 'http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt'
print urlopen(URL).read()
