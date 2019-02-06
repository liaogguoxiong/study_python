#时间：    2018/11/23 22:59
#作者：    lgx
#文件名：  studyOfXml

'''
今天来学习xml相关知识
xml协议在各个语言里的都 是支持的，在python中可以用以下模块操作xml 　　
'''
import xml.etree.ElementTree as ET
tree=ET.parse('xmlContent.xml')
root=tree.getroot()
print(root)#获取xml文件的内存地址
print(root.tag)#获取xml的根

'''
遍历xml文档
'''

for child in root:
    print(child.tag,child.attrib)#tag为标签,attrib为参数
    for i in child:
        print(i.tag,i.text,i.attrib)#text为内容

'''
遍历节点
'''

for node in root.iter('gdppc'):
    print(node.tag,node.text)
