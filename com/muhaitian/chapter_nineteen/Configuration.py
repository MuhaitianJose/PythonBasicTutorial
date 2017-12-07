# -*-coding:gbk-*-
import logging
from ConfigParser import ConfigParser


def useConfig():
    CONFIGFILE = 'python.txt'
    config = ConfigParser()
    config.read(CONFIGFILE)
    # 打印问候语
    print config.get('message', 'greeting')
    # 使用配置文件的一个问题读取半径：
    radius = input(config.get('message', 'question'))
    # 打印配置文件中的结果信息
    # 以逗号结束，以在同一行显示
    print config.get('message', 'result_message')
    # getfloat()将config值转换为float类型
    print config.getfloat('numbers', 'pi') * radius ** 2


def useLogging():
    logging.basicConfig(level=logging.INFO)
    logging.info('start program')
    logging.info('Trying to divide 1 by 0')
    print 1 / 0
    logging.info('The division succeeded')
    logging.info('Ending program')


useLogging()
