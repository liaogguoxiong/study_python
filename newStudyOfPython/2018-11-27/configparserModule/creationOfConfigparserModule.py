#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-27 9:52
#!@Filename:creationOfConfigparserModule.py

'''

今天来学习configparser模块,此模块用来编写配置文件的

'''

import configparser

config=configparser.ConfigParser()
#相当于字典
config['DEFAULT']={ 'ServiceAliveInterval':'45',
                    'Compression':'yes',
                    'CompressionLevel':'9'
}
config['bitbucket.org']={}
config['bitbucket.org']['User']='hg'#key：User  values：hg
config['topsecret.server.com']={}
topsecret=config['topsecret.server.com']
topsecret['Host Port']='50002'
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini','w') as configfile:#打开配置文件，写模式，如果不存在则创建
    config.write(configfile)#把写好的配置写入配置文件