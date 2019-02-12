#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-26 13:54
#!@Filename:xmlOfDelect.py
'''
删除xml中的节点
'''
import xml.etree.ElementTree as ET
tree=ET.parse('xmlContent.xml')
root=tree.getroot()
for country in root.findall('country'):#找出所有的country标签
    rank=int(country.find('rank').text)#找出contry标签中的rank的文本
    if rank > 50:
        root.remove(country)
tree.write('output.xml')
