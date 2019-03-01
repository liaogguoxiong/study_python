#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-26 15:00
#!@Filename:studyOflogging.py
'''
学习logging模块，
'''
import logging
# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("service is down")

'''
，logging的日志可以分为 
debug(), info(), warning(), error() and critical() 
5个级别
'''
#
logging.basicConfig(filename='example.log',level=logging.INFO)
logging.debug("this message should go to the log file")
logging.info("Hello ,i am info")
logging.warning('hello,i am warnning')