#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-22 15:06
#!@Filename:studyOflogging.py

import logging

logging.basicConfig(filename='log.log',
                    format='%(asctime)s - %(name)s -%(levelname)s -%(module)s -%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %P',
                    level=10

)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10,'log')