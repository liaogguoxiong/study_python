#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-26 11:36
#!@Filename:xmlOfUpdate.py\
'''
更新xml操作
'''
import xml.etree.ElementTree as ET
tree=ET.parse('xmlContent.xml')#传入xml，获取树
root=tree.getroot()#获取树的根节点
for node in root.iter('year'):#循环输出year，然后改变year
    year=int(node.text) + 1
    print(year)
    node.text=str(year)
    node.set('updated','not')

tree.write('xmlContent.xml')#把改变的结果写入xml中，只有读入才起作用