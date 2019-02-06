#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-22 14:17
#!@Filename:studyOfSys.py

import sys
print(sys.argv)#命令行参数List，第一个元素是程序本身路径
#sys.exit()#退出程序，正常退出时exit(0)
print(sys.version)#获取Python解释程序的版本信息
#print(sys.maxsize)
print(sys.platform)#返回操作系统平台名称
print(sys.path)#返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值