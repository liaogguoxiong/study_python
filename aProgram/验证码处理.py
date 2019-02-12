#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-18 13:51
#!@Filename:验证码处理.py

from PIL import Image,ImageEnhance


def get_bin_table(threshold=115):
	'''
	获取灰度转二值的映射table
	0表示黑色,1表示白色
	'''
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table



#二值化图片
image=Image.open('C:/Users/xiao/Desktop/picture/pic0.png')
imgry=image.convert('L')#转为灰度图
table=get_bin_table()
binary=imgry.point(table,'1')
binary.save('C:/Users/xiao/Desktop/picture/binary.png')
