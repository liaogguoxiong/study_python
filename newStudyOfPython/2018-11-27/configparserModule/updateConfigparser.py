#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-27 14:01
#!@Filename:updateConfigparser.py
'''

configparser增删改查语法

'''
import configparser
config=configparser.ConfigParser()
config.read('example.ini')

# ###########读##############
secs=config.sections()
print(secs)#输出配置名称

options=config.options('topsecret.server.com')
print(options)#输出配置的属性以及默认的配置属性

item_list=config.items('topsecret.server.com')
print(item_list)#把自身属性以及默认的配置以及值读出来

val=config.get('topsecret.server.com','servicealiveinterval')#获取属性的值
print(val)

#############改写#############

rm=config.remove_section('bitbucket.org')#删除某个配置
config.write(open('example.ini','w'))

# #sec=config.has_section('wupeiqi')
# sec=config.add_section('wupeiqi')#增加配置名称
# config.write(open('example.ini','w'))#写入配置文件才可以生效

# config.set('wupeiqi','k1','222222')#添加对应的配置的属性和值
# config.write(open('example.ini','w'))

config.remove_option('wupeiqi','k1')
config.write(open('example.ini','w'))#删除对应的配置的属性和值