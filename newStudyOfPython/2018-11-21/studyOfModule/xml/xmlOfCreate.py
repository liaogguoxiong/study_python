#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-26 14:29
#!@Filename:xmlOfCreate.py
'''
创建一个xml文件
'''
import xml.etree.ElementTree as ET
new_xml=ET.Element('namelist')#创建根节点
personInfo=ET.SubElement(new_xml,"personInfo",attrib={"enrolled":'yes'})#创建根节点下的子节点
name=ET.SubElement(personInfo,'name',attrib={"checked":"no"})
name.text='lgx'
age=ET.SubElement(personInfo,'age',attrib={"checked":"no"})
age.text='22'
sex=ET.SubElement(personInfo,'sex')
sex.text='廖国雄'
et=ET.ElementTree(new_xml)
et.write("test.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)#打印生成的格式