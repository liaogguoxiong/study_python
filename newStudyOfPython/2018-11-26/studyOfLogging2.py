#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-26 15:26
#!@Filename:studyOfLogging2.py
'''

'''
import logging
logging.basicConfig(filename='example2.log',level=logging.INFO,format='%(asctime)s %(message)s')
logging.warning("hello,i am warning")
logging.debug("this message should go to the log file")
logging.info("Hello ,i am info")