# -*-coding:gbk-*-
import logging
from ConfigParser import ConfigParser


def useConfig():
    CONFIGFILE = 'python.txt'
    config = ConfigParser()
    config.read(CONFIGFILE)
    # ��ӡ�ʺ���
    print config.get('message', 'greeting')
    # ʹ�������ļ���һ�������ȡ�뾶��
    radius = input(config.get('message', 'question'))
    # ��ӡ�����ļ��еĽ����Ϣ
    # �Զ��Ž���������ͬһ����ʾ
    print config.get('message', 'result_message')
    # getfloat()��configֵת��Ϊfloat����
    print config.getfloat('numbers', 'pi') * radius ** 2


def useLogging():
    logging.basicConfig(level=logging.INFO)
    logging.info('start program')
    logging.info('Trying to divide 1 by 0')
    print 1 / 0
    logging.info('The division succeeded')
    logging.info('Ending program')


useLogging()
