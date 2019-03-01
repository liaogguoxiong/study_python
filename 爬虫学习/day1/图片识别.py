#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-18 15:53
#!@Filename:图片识别.py
import pytesseract
from PIL import Image
#打开图片
image=Image.open('6.jpg')
#识别图片中的文字,转化为字符串
print(pytesseract.image_to_string(image))
