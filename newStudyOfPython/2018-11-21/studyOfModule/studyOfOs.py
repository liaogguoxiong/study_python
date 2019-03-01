#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-21 16:26
#!@Filename:studyOfOs.py

'''
os模块，提供对操作系统进行调用的接口
'''
import os
print(os.getcwd())#获取当前工作目录，即当前python脚本工作的目录路径
print(os.curdir)#返回当前目录（'.'）
print(os.pardir)#返回当前目录的父目录字串：（'..'）
#os.makedirs('test1/test2')#生成多层递归目录
#os.removedirs(dirname)#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
#os.mkdir('test3')#生成单级目录
#os.rmdir('test3')#删除单级空目录，若目录不为空则无法删除，报错，相当于shell中的rmdir dirname
#print(os.listdir('test1'))#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方法打印
#os.remove('hello')#删除一个文件
#os.rename('test1','test')#删除一个文件
print(os.stat('test'))#获取文件/目录的信息
print(os.sep)#输出操作系统特定的路径分隔符，win下为“\\”,Linux下为“\n”
print(os.linesep)#输出操作系统的终止符，其实有输出
print(os.pathsep)#输出分割文件路径的字符串
print(os.name)#输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.environ)#获取系统的环境变量
print(os.path.abspath('studyOfOs'))#返回path规范化的绝对路径
print(os.path.split('studyOfOs'))#返回path规范化的绝对路径
print(os.path.dirname(os.path.abspath('studyOfOs')))#返回path的目录，其实就是os.path.split（path）的第一个元素
print(os.path.basename('studyOfOs'))#返回最后的文件名
print(os.path.exists(''))#如果path存在，返回True，否则返回False
print(os.path.isabs('studyOfOs'))#如果path是绝对路径，返回True，否则返回False
print(os.path.isfile('studyOfOs.py'))#如果是文件，则返回True，否则返回False
print(os.path.isdir('test'))#如果是一个目录，则返回True，否则返回False
#os.path.join(path1[, path2[, ...]]) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime('studyOfOs.py'))#返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime('studyOfOs.py'))#返回path所指向的文件或者目录的最后修改时间