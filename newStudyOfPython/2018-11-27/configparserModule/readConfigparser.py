#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-27 13:43
#!@Filename:readConfigparser.py
'''
读configparser配置文件
'''
import configparser
config=configparser.ConfigParser()#
print(config.sections())#没解析之前没东西
print(config.read('example.ini'))#解析配置文件，读出配置文件，默认配置不打印
print(config.sections())#
print('bitbucket.org' in config)#判断某个配置在不在配置文件中
print('hello' in config)
print(config['bitbucket.org']['User'])#读出属性的值
topsecret=config['topsecret.server.com']
print(topsecret['host port'])
print("================")
for i  in config['DEFAULT']:#循环输出某个配置文件的属性
    print(i,config['DEFAULT'][i])
