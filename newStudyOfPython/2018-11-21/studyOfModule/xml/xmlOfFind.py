#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-26 9:14
#!@Filename:xmlOfFind.py

'''
读xml文件
'''
import xml.etree.ElementTree as ET
tree=ET.parse('xmlContent.xml')
root=tree.getroot()
print(root)# return root's memory address
print(root.tag)# return root's label
# loop tree's child node，遍历子节点
for child in root:
    print(child.tag,child.attrib)
    #loop the content of child node
    for i in child:
        print(i.tag,i.text,i.attrib)# tag===>content's label
#只遍历子节点
for node in root.iter('rank'):
    print(node.attrib,node.text)